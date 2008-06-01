from __future__ import division
from pylab import *
from numpy import *
from numpy.fft import *
# from pytfd import stft
from pytfd.stft import *

N = 4096
T = 64

for window_name in ('ones', 'hanning', 'gaussian', 'blackman'):
    window_function = globals()[window_name]
    w = window_function(T)
    W = fft(zeropad(w, N))
    figure()
    subplot(1, 2, 1)
    title(window_name)
    plot(zeropad(w, 2*T))
    axis([0, 2*T, 0, 2])
    subplot(1, 2, 2)
    title("FT(%s)"%window_name)
    plot(linspace(0, 2*pi, N), fftshift(log10(abs(W)+1)))
    savefig(window_name)
