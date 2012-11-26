cdef extern from "math.h":
    double cos(double x)
    double sin(double x)
    double tan(double x)

    double M_PI

def test_trig():
    print 'Some trig functions from C:', cos(0), cos(M_PI)

