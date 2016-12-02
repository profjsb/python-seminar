from __future__ import division

def f(double x):
    return x**4 - 3 * x

def types_integrate_f(double a, double b, int N):
    """Rectangle integration of a function.

    Parameters
    ----------
    a, b : ints
        Interval over which to integrate.
    N : int
        Number of intervals to use in the discretisation.

    """
    cdef:
        double s = 0
        double dx = (b - a) / N
        int i

    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx