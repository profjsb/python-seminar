import numpy as np

from numba.decorators import jit
from numba import float64, int32

@jit(arg_types=[float64[:, :], float64[:, :], float64[:, :]])
def ndot(A, B, out):
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    # Take each row in A
    for i in range(rows_A):

        # And multiply by every column in B
        for j in range(cols_B):
            s = 0.0
            for k in range(cols_A):
                s = s + A[i, k] * B[k, j]

            out[i, j] = s
