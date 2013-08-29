import numpy as np

def foo(double[:, ::1] arr):

    cdef size_t i, j
    cdef double[:, ::1] out = np.zeros_like(arr)

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            out[i, j] = arr[i, j] + 10

    return np.asarray(out)
