# cython: cdivision=True

# ^^^ Could also use @cython.cdivision(True) decorator

cdef double f(double x):
    return x*x*x*x - 3 * x

def integrate_f(double a, double b, int N):
    cdef:
        double s = 0
        double dx = (b - a) / N
        size_t i

    for i in range(N):
        s += f(a + i * dx)

    return s * dx
