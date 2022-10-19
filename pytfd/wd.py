from __future__ import division

from numpy import *
from numpy.fft import fft
from pytfd import helpers as h

def wd(x):
    N = len(x)
    x_ = x.conj()
    WD = [fft(h.subset(x, n, N)*h.subset(x_, n, N)[::-1]) for n in range(len(x))]
    WD = array(WD).transpose()
    return WD

