import numpy as np
cimport numpy as cnp

cnp.import_array()

cimport cython
from cython.parallel cimport prange

@cython.boundscheck(False)
@cython.wraparound(False)
def dot(double[:, ::1] A,
        double[:, ::1] B,
        double[:, ::1] out):

    cdef:
        size_t rows_A, cols_A, rows_B, cols_B
        size_t i, j, k
        double s

    rows_A, cols_A = A.shape[0], A.shape[1]
    rows_B, cols_B = B.shape[0], B.shape[1]

    # Take each row in A
    for i in range(rows_A):

        # And multiply by every column in B
        for j in range(cols_B):
            s = 0
            for k in range(cols_A):
                s = s + A[i, k] * B[k, j]

            out[i, j] = s


@cython.boundscheck(False)
@cython.wraparound(False)
def pdot(double[:, ::1] A,
         double[:, ::1] B,
         double[:, ::1] out):

    cdef:
        size_t rows_A, cols_A, rows_B, cols_B
        size_t i, j, k
        double s

    rows_A, cols_A = A.shape[0], A.shape[1]
    rows_B, cols_B = B.shape[0], B.shape[1]

    with nogil:

        # Take each row in A
        for i in prange(rows_A):

            # And multiply by every column in B
            for j in prange(cols_B):
                s = 0
                for k in range(cols_A):
                    s = s + A[i, k] * B[k, j]

                out[i, j] = s
