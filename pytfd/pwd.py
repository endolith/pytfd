from __future__ import division

from numpy import *
from numpy.fft import fft
from pytfd import helpers as h


def pwd(x, w):
    N = len(x)
    w = h.zeropad(w, N)
    w_ = w[::-1].conj()
    X_pwd = []
    points = range(0, N)
    for i in points:
        x_subset = h.subset(x, i, N)
        fft_subset = fft(w * w_ * x_subset * x_subset[::-1].conj())
        X_pwd.append(fft_subset)
    X_pwd = array(X_pwd).transpose()
    return X_pwd
