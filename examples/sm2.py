from __future__ import division
from pylab import *
from numpy import *
from numpy.fft import *
from pytfd import sm
#from pytfd.sm import *

N = 2048
T = 64

t_max = 5
t = linspace(0, t_max, N)
fs = N/t_max
f = linspace(0, fs, N)

t1 = t[:N//2]
t2 = t[N//2:]

x1 = sin(2*pi*30*t1)
x2 = sin(2*pi*10*t2)
x3 = sin(2*pi*5*(t + t_max)**2)
x4 = sin(2*pi*5*(-t + 2*t_max)**2)

y1 = concatenate([x2[:N//4], x1, x2[N//4:]]) + x3
y2 = concatenate([x1, x2]) + x4

w = ones(T)
P = ones(3)
for i in (1, 2):
    figure()
    y = globals()['y%d'%i]
    subplot(2, 1, 1)
    plot(t, y)
    Y = abs(fft(y))
    subplot(2, 1, 2)
    plot(f[:N//2], Y[N//2:])
    savefig('2sin_linear_FM_%d_signal_FT'%i)
    figure()
    Y_sm = sm.sm(y, w, P)
#    contour(t, f[:N//2], abs(Y_sm)[N//2:])
    imshow(abs(Y_sm)[N//2:])
    xlabel("Time")
    ylabel("Frequency")
    title(r"SM T = %d$T_s$"%T)
    savefig('2sin_linear_FM_%d_sm'%i)
