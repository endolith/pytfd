from numpy import *

def rect_win(T):
    return ones(T)

def hann_win(T):
    T = T//2
    t = linspace(-T, T, 2*T)
    w = 1/2 * (1 + cos(t*pi/T))
    return w

def gauss_win(T, a=1):
    T = T//2
    t = linspace(-T, T, 2*T)
    N = T//2
    w = exp(-((t)/(a*N))**2)
    return w

def black_win(T):
    T = T//2
    t = linspace(-T, T, 2*T)
    w = 0.42 + 0.5*cos(t*pi/T) + 0.08*cos(2*t*pi/T)
    return w

def kaiser_win(T):
    T = T//2
    t = linspace(-T, T, 2*T)
    w = 0.42 + 0.5*cos(t*pi/T) + 0.08*cos(2*t*pi/T)
    return w
