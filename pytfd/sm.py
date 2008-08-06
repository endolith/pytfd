from __future__ import division

from numpy import *
#from numpy.fft import fft

from pytfd.stft import stft

def sm(x, w, P):
    assert len(P)%2 != 0 # The P window has to be odd
    L = (len(P)-1)//2
    F = stft(x, w)
    SM = zeros_like(F)
    N = F.shape[0]
    for i in range(-L, L + 1):
        if i > 0:
            SM[:, i:N-i] += P[i + L] * F[:, 2*i:N] * F[:,:N-2*i].conjugate()
        else:
            i = abs(i)
            SM[:, i:N-i] += P[-i + L] * F[:,:N-2*i] * F[:, 2*i:N].conjugate()
    return SM
