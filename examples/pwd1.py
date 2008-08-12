from __future__ import division
from pylab import *
from pytfd.pwd import pwd
from pytfd import windows

N = 2048
f_max = 30
# PWD sampling frequency has to be at least two times greater than normal fs
fs = 2 * f_max
f = linspace(0, f_max, N)
Ts = 1/fs
t_max = N * Ts
t = linspace(0, t_max, N)


for i, T in enumerate([64, 128]):
    w = windows.rectangular(T) # Rectangular window
    delta1 = zeros(N)
    delta1[N//4] = 5
    delta2 = zeros(N)
    delta2[3*N//4] = 5
    y = sin(2*pi*10*t) + sin(2*pi*30*t) + delta1 + delta2
    Y_pwd = pwd(y, w)
    figure()
    #contour(t, 2*f[:N//2], abs(Y_pwd)[N//2:])
    imshow(abs(Y_pwd)[N//2:])
    xlabel("Time")
    ylabel("Frequency")
    title(r"PWD T = %d$T_s$"%T)
    savefig('sin_delta_T%d'%T)
