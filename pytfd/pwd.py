from __future__ import division

from numpy import *
from numpy.fft import fft
from pytfd import helpers as h


def pwd(x, w):
#     temp = []
#     prev = x[0]
#     for i in x:
#         temp.append(i)
#         temp.append((i + prev)/2)
#         prev = i
#     x = array(temp)
    N = len(x)
    w = h.zeropad(w, N)
    X_pwd = []
    points = range(0, N)
    for i in points:
        x_subset = h.subset(x, i, N)
        fft_subset = fft(w * w[::-1].conj() * x_subset * x_subset[::-1].conj())
        X_pwd.append(fft_subset)
    X_pwd = array(X_pwd).transpose()
    return X_pwd
