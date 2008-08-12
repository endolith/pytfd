"""This file defines the some helper functions/variables
needed for implementation of TFDs.
"""
from __future__ import division

import numpy

def subset(x, i, N, padding='zeros'):
    assert padding in ('zeros', 'circular')
    assert N <= len(x)
    if padding == 'zeros':
        if i < N//2:
            x_subset = x[:i + N//2]
            x_subset = numpy.concatenate([numpy.zeros(N//2 - i), x_subset])
        else:
            x_subset = x[i - N//2 : i + N//2]
            if len(x_subset) < N:
                x_subset = numpy.concatenate([x_subset, numpy.zeros(N - len(x_subset))])
    elif padding == 'circular':
        temp = numpy.concatenate([x, x, x])
        center = len(x) + i
        x_subset = temp[center-N//2:center+N//2]
    return x_subset

def zeropad(w, N):
    T = len(w)
    w_zeros = numpy.zeros(N//2 - T//2)
    w = numpy.concatenate([w_zeros, w, w_zeros])
    if len(w) == N + 1:
        w = w[:-1]
    return w

__all__ = ["subset", "zeropad"]
