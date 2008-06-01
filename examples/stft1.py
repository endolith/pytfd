from __future__ import division

from pylab import *
from pytfd.stft import *

N = 2048
t_max = 10
t = linspace(0, t_max, N)
fs = N/t_max
f = linspace(0, fs, N)

for i, T in enumerate([64, 128]):
    w = ones(T) # Rectangular window
    delta1 = zeros(N)
    delta1[N//4] = 5
    delta2 = zeros(N)
    delta2[3*N//4] = 5
    y = sin(2*pi*10*t) + sin(2*pi*30*t) + delta1 + delta2
    Y_stft = stft(y, w)
    figure()
    contour(t, f[:N//2], abs(Y_stft).transpose()[N//2:])
    xlabel("Time")
    ylabel("Frequency")
    title(r"STFT T = %d$T_s$"%T)
    savefig('sin_delta_T%d'%T)
