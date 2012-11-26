import numpy as np

def my_poly(double[:] x):
    cdef int i, L
    cdef double[:] out = np.zeros_like(x)

    L = x.shape[0]

    for i in range(L):
        out[i] = x[i] * x[i] * x[i] - 4 * x[i] + 2

    return np.asarray(out)
