from __future__ import division

from pylab import *

N = 256
t_max = 10
t = linspace(0, t_max, N)
fs = N/t_max
f = linspace(0, fs, N)

# Signals
delta1 = zeros(N)
delta1[N//4] = 5
delta2 = zeros(N)
delta2[3*N//4] = 5
y = sin(2*pi*10*t) + sin(2*pi*30*t) + delta1# + delta2
