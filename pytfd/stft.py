"""This file defines the Short-Time Fourier Transfor (STFT)
or more precisely the Discrete Time and Frequency STFT.
"""
from __future__ import division

import numpy
from numpy import *

def fft(*args, **kwargs):
    res = numpy.fft.fft(*args, **kwargs)
    return res
    #N = len(res)
    #return concatenate([res[N//2:], res[:N//2]])

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

def stft(x, w, L=None):
    # L is the overlap, see http://cnx.org/content/m10570/latest/
    N = len(x)
    T = len(w)
    if L is None:
        L = N
    # Zerro pad the window
    w = zeropad(w, N)
    X_stft = []
    points = range(0, N, N//L)
    for i in points:
        x_subset = subset(x, i, N)
        fft_subset = fft(x_subset * w)
        X_stft.append(fft_subset.transpose())
    X_stft = array(X_stft)
    return X_stft

__all__ = ['stft']
