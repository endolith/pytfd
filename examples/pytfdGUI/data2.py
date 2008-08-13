from __future__ import division
from pylab import *
from numpy import *

N = 1024
T = 32

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
