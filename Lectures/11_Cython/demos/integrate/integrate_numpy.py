from __future__ import division

import numpy as np

def f(x):
    return x**4 - 3 * x

def integrate_f(a, b, N):
    dx = (b - a) / N
    return np.sum(f(np.linspace(a, b, N, endpoint=False))) * dx
