"""
Geometric warp correction via homography estimation.

Stefan van der Walt <stefan@sun.ac.za>
July 2010

Updated with new skimage imports, 2012/02

"""

X_OUT, Y_OUT = 200, 200

import os

import numpy as np

import matplotlib.pyplot as plt

import skimage
from skimage import io as sio
from skimage import transform as tf
from skimage import data, color

img = data.camera()

theta = np.deg2rad(30)
c = np.cos(theta)
s = np.sin(theta)
a = 0.4
b = 0.4


H = np.array([[a*c, -b*s,   130],
              [a*s,  b*c,   20],
              [1e-4, -5e-4, 1]])

img_tf = tf.homography(img, H)

plt.subplot(121)
plt.grid()
plt.axis('image')
plt.xlim(0, X_OUT)
plt.ylim(0, Y_OUT)
ax = plt.gca()
ax.invert_yaxis()

plt.subplot(122)
plt.imshow(img_tf, cmap=plt.cm.gray, interpolation='nearest')

plt.suptitle('Dewarping\nSelect 4 points on the left grid, then 4 in the right '
             'image.')

# Source coordinates
sc = np.array(plt.ginput(n=4))
sx = sc[:, 0]
sy = sc[:, 1]

print "Source coordinates:"
print sc

# Target coordinates
tc = np.array(plt.ginput(n=4))
tx = tc[:, 0]
ty = tc[:, 1]

print "Target coordinates:"
print tc

A = np.zeros((8, 9))
A[::2, 0] = -sx
A[::2, 1] = -sy
A[::2, 2] = -1
A[::2, 6] = tx * sx
A[::2, 7] = tx * sy
A[::2, 8] = tx

A[1::2, 3] = -sx
A[1::2, 4] = -sy
A[1::2, 5] = -1
A[1::2, 6] = ty * sx
A[1::2, 7] = ty * sy
A[1::2, 8] = ty

u, s, v = np.linalg.svd(A)
v = v.T

print "Smallest singular value:", s[-1]
h = v[:, -1].reshape((3, 3))

print "Estimated H matrix:"
print h

img_unwarp = tf.homography(img_tf, np.linalg.inv(h),
                           output_shape=(Y_OUT, X_OUT))

plt.figure()
plt.imshow(img_unwarp, cmap=plt.cm.gray, interpolation='nearest')

plt.show()
