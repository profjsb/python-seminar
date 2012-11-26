cdef extern from "Circle.h" namespace "geom":
     cdef cppclass Circle:
          Circle(double, double, double)
          double getX()
          double getY()
          double getRadius()
          double getArea()
          void setCenter(double, double)
          void setRadius(double)

cdef class PyCircle:
    """Python Circle wrapper.

    Parameters
    ----------
    x : float
       Center x position.
    y : float
       Center y position.
    r : float
       Radius.

    """

    cdef Circle *thisptr

    def __cinit__(self, double x, double y, double r):
        self.thisptr = new Circle(x, y, r)

    def __dealloc__(self):
        del self.thisptr

    @property
    def area(self):
        return self.thisptr.getArea()

    @property
    def radius(self):
        return self.thisptr.getRadius()

    def set_radius(self, r):
        self.thisptr.setRadius(r)

    @property
    def center(self):
        return (self.thisptr.getX(), self.thisptr.getY())

    def set_center(self, x, y):
        self.thisptr.setCenter(x, y)
