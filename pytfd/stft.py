"""This file defines the Short-Time Fourier Transfor (STFT)
or more precisely the Discrete Time and Frequency STFT.
"""
from __future__ import division

from numpy import *
from numpy.fft import fft

from pytfd import helpers as h

def stft(x, w, L=None):
    # L is the overlap, see http://cnx.org/content/m10570/latest/
    N = len(x)
    #T = len(w)
    if L is None:
        L = N
    # Zerro pad the window
    w = h.zeropad(w, N)
    X_stft = []
    points = range(0, N, N//L)
    for i in points:
        x_subset = h.subset(x, i, N)
        fft_subset = fft(x_subset * w)
        X_stft.append(fft_subset)
    X_stft = array(X_stft).transpose()
    return X_stft

def spec(x, w):
    return abs(stft(x, w))

spectogram = spec

__all__ = ['stft', 'spec', 'spectogram']
