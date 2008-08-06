from __future__ import division
from test_data1 import *
from pytfd.stft import *
from pytfd import windows

for i, T in enumerate([32, 64, 128]):
    w = windows.rectangular(T) # Rectangular window
    delta1 = zeros(N)
    delta1[N//4] = 5
    delta2 = zeros(N)
    delta2[3*N//4] = 5
    y = sin(2*pi*10*t) + sin(2*pi*30*t) + delta1 + delta2
    Y_stft = stft(y, w)
    figure()
    contour(t, f[:N//2], abs(Y_stft)[N//2:])
    xlabel("Time")
    ylabel("Frequency")
    title(r"STFT T = %d$T_s$"%T)
    savefig('sin_delta_T%d'%T)
