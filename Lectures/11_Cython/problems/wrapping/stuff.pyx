import numpy as np
cimport numpy as np

from cython cimport view

cdef extern from "stuff.h":
    void compute(int n, double *input, double *output)

def do_compute(double[::1] input_array):
    cdef double[::1] result = np.zeros_like(input_array)
    compute(input_array.shape[0],
            &input_array[0],
            &result[0])

    return result
