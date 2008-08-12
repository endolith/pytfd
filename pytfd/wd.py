from __future__ import division

from numpy import *
from numpy.fft import fft
from pytfd import helpers as h

def wd(x):
    N = len(x)
    x_ = x.conj()
    WD = []
    for n in range(len(x)):
        WD.append(fft(h.subset(x, n, N)*h.subset(x_, n, N)[::-1]))
        #WD.append(fft(h.subset(x, n, N, padding='circular')*h.subset(x_, n, N, padding='circular')))
    WD = array(WD).transpose()
    return WD

