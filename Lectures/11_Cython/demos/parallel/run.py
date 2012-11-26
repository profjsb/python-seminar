import contextlib
import time
import numpy as np

import prange_demo

# Utilities borrowed from Dag
def format_time(t):
    if t > 1 or t == 0:
        units = 's'
    elif t > 1e-3:
        units = 'ms'
        t *= 1e3
    elif t > 1e-6:
        units = 'us'
        t *= 1e6
    else:
        units = 'ns'
        t *= 1e9
    return '%.1f %s' % (t, units)

@contextlib.contextmanager
def take_time(desc):
    t0 = time.time()
    yield
    dt = time.time() - t0
    print '%s took %s' % (desc, format_time(dt))

# ----------------------------------------------------------

M, N, P, Q = 500, 250, 250, 500
A = np.random.random((M, N))
B = np.random.random((P, Q))
out = np.zeros((M, Q))
expected = np.dot(A, B)

with take_time('Cython Dot'):
    prange_demo.dot(A, B, out)
    np.testing.assert_allclose(out, expected)

with take_time('Cython Dot with prange'):
    prange_demo.pdot(A, B, out)
    np.testing.assert_allclose(out, expected)

with take_time('NumPy Dot'):
    out = np.dot(A, B)

try:
    import numba
except:
    pass
else:
    import numba_dot
    with take_time('Numba Dot:'):
        numba_dot.ndot(A, B, out)
        np.testing.assert_allclose(out, expected)

# ----------------------------------------------------------
