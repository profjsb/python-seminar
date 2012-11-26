cdef extern from "math.h":
    double sin(double)

def integrate_sinsq(double a, double b, int N):
    cdef double s = 0
    cdef double dx = (b-a)/N
    cdef int i
    for i in range(N):
        s += sin((a+i*dx)**2)
    return s * dx
