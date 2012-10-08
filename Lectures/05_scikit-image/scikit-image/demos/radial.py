"""Remove radial distortion.

Author: Stefan van der Walt
Date: 2006
"""

import scipy as S
import scipy.optimize
import scipy.ndimage

import pylab as P
import numpy as N
import math
import sys

class RadialDistortionInterface:
    """Mouse interaction interface for radial distortion removal.
    
    """
    def __init__(self, img):
      imshape = img.shape
      self.figure = P.imshow(img, extent=(0,imshape[1],imshape[0],0))
      P.title('Removal of radial distortion')
      P.xlabel('Select sets of three points with left mouse button,\nclick right button to process.')
      
      P.connect('button_press_event', self.button_press)
      P.connect('motion_notify_event', self.mouse_move)

      self.img = N.atleast_3d(img)
      self.points = []
      self.centre = ((N.array(self.img.shape)-1)/2.)[:2][::-1]
      self.height = imshape[0]
      self.width = imshape[1]
      
      self.make_cursorline()
      self.figure.axes.set_autoscale_on(False)

      P.show()
      P.close()
      
    def make_cursorline(self):
        self.cursorline, = P.plot([0],[0],'r:+',
                                  linewidth=2,markersize=15,markeredgecolor='b')

    def button_press(self,event):
        """Register mouse clicks.
        
        """
        if (event.button == 1 and event.xdata and event.ydata):
            self.points.append((event.xdata,event.ydata))
            print "Coordinate entered: (%f,%f)" % (event.xdata, event.ydata)
            
            if len(self.points) % 3 == 0:
                P.gca().lines.append(self.cursorline)
                self.make_cursorline()

        if (event.button != 1 and len(self.points) >= 3):
            print "Removing distortion..."
            P.gca().lines = []
            P.draw()
            self.remove_distortion()
            self.points = []
            
    def mouse_move(self,event):
        """Handle cursor drawing.
        
        """
        pt_sets,pts_last_set = divmod(len(self.points),3)
        pts = N.zeros((3,2))
        if pts_last_set > 0:
            # Line follows up to 3 clicked points:
            pts[:pts_last_set] = self.points[-pts_last_set:]
            # The last point of the line follows the mouse cursor
        pts[pts_last_set:] = [event.xdata,event.ydata]
        self.cursorline.set_data(pts[:,0],pts[:,1])
        P.draw()

    def stackcopy(self,a,b):
        """a[:,:,0] = a[:,:,1] = ... = b"""
        if a.ndim == 3:
            a.transpose().swapaxes(1,2)[:] = b
        else:
            a[:] = b
                        
    def remove_distortion(self,reshape=True):
        def radii_tf(x,y,p):
            """Radially distort coordinates.
            
            Given a coordinate (x,y), apply the radial distortion defined by
            
            L(r) = 1 + p[2]r + p[3]r^2 + p[4]r^3
            
            where

            r = sqrt((x-p[0])^2 + (y-p[1])^2)
            
            so that
            
            x' = L(r)x   and   y' = L(r)y
            
            Inputs:
                x,y -- Coordinate
                p[0],p[1] -- Distortion centre
                p[2],p[3],p[4] -- Distortion parameters
                
            Outputs:
                x', y'
                
            """
            x = x - p[0]
            y = y - p[1]
            r = N.sqrt(x**2 + y**2)
            f = 1 + p[2]*r + p[3]*r**2 + p[4]*r**3                
            return x*f + p[0], y*f + p[1]

        def height_difference(p):
            """Measure deviation of distorted data points from straight line.
            
            """
            out = 0
            for sets in 3*N.arange(len(self.points)/3):
                pts = N.array(self.points[sets:sets+3])
                x,y = radii_tf(pts[:,0],pts[:,1],p)

                # Find point on line (point0 <-> point2) closest to point1 (midpoint)
                u0 = ((x[0]-x[2])**2 + (y[0]-y[2])**2)
                if u0 == 0:
                    return 1

                u = ((x[1]-x[0])*(x[2]-x[0]) + (y[1] - y[0])*(y[2] - y[0]))/u0

                # Intersection point
                ip_x = x[0] + u*(x[2]-x[0])
                ip_y = y[0] + u*(y[2]-y[0])

                # Distance between line and midpoint
                out += (ip_x - x[1])**2 + (ip_y - y[1])**2
                
            return out

        # Find the distortion parameters for which the data points lie on a straight line
        rc = S.optimize.fmin(height_difference,[self.centre[0],self.centre[1],0.,0.,0.])

        # Determine inverse coefficient
        x = N.linspace(0,self.width)
        y = N.linspace(0,self.height)
        def inv_min(p):
            xt, yt = radii_tf(*(radii_tf(x,y,rc) + (p,)))
            return N.sum((x-xt)**2 + (y-yt)**2)
        rci = S.optimize.fmin(inv_min,[rc[0],rc[1],0.,0.,0.])

        # Perform reverse transformation on coordinates
        oshape = N.array(self.img.shape)        
        if reshape:
            top_corner = N.array(radii_tf(0.,0.,rc))
            bottom_corner = N.array(radii_tf(self.width-1,self.height-1,rc))
            oshape[:2][::-1] = bottom_corner - top_corner

        y,x = N.mgrid[0:oshape[0],0:oshape[1]]

        if reshape:
            x = x + top_corner[0]
            y = y + top_corner[1]
            rc[0] -= top_corner[0]
            rc[1] -= top_corner[1]
            
        # Calculate reverse coordinates
        x,y = radii_tf(x,y,rci)

        coords = N.empty(N.r_[3,oshape],dtype=float)
        
        # y mapping
        self.stackcopy(coords[0,...],y)

        # x mapping
        self.stackcopy(coords[1,...],x)

        # colour band mapping
        coords[2,...] = range(self.img.shape[2])

        restored_img = S.ndimage.map_coordinates(self.img,coords,order=1,prefilter=False).squeeze()

        P.figure()
        P.imshow(restored_img)

        # Plot forward and reverse transforms        
        x = N.linspace(self.width/2,self.width)
        y = N.linspace(self.height/2,self.height)
        r = N.sqrt((x-self.centre[0])**2 + (y-self.centre[1])**2)
        xr,yr = radii_tf(x,y,rc)
        xri,yri = radii_tf(x,y,rci)
        rf = N.sqrt(xr**2 + yr**2)
        rr = N.sqrt(xri**2 + yri**2)

        a = P.axes([0.15,.15,.15,.15])
        P.plot(r,rf,label='Forward mapping')
        P.plot(r,rr,':',label='Reverse mapping')
        P.grid()
        #P.xlabel('Input radius')
        #P.ylabel('Transformed radius')
        #P.legend()
        P.setp(a,xticks=[],yticks=[])
        
        P.show()

imread = S.misc.pilutil.imread

if len(sys.argv) != 2:
    print "Usage: %s <image-file>" % sys.argv[0]
else:
    img = imread(sys.argv[1])
    rdi = RadialDistortionInterface(img)
