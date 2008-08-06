"""This file defines the some helper functions/variables
needed for implementation of TFDs.
"""
from __future__ import division

from numpy import *

def subset(x, i, N):
    if i < N//2:
        x_subset = x[:i + N//2]
        x_subset = concatenate([zeros(N//2 - i), x_subset])
    else:
        x_subset = x[i - N//2 : i + N//2]
    if len(x_subset) < N:
        x_subset = concatenate([x_subset, zeros(N - len(x_subset))])
    return x_subset

def zeropad(w, N):
    T = len(w)
    w_zeros = zeros(N//2 - T//2)
    w = concatenate([w_zeros, w, w_zeros])
    return w

