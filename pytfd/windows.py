from numpy import *
#from numpy import hamming, hanning

def rectangular(T):
    return ones(T)

def gaussian(T, a=1):
    L = T//2
    t = linspace(-L, L, T)
    N = L//2
    w = exp(-((t)/(a*N))**2)
    return w

def kaiser_win(T):
    T = T//2
    t = linspace(-T, T, 2*T)
    w = 0.42 + 0.5*cos(t*pi/T) + 0.08*cos(2*t*pi/T)
    return w

__all__ = [
    "hanning",
    "hamming",
    "rectangular",
    "gaussian",
    "kaiser",
    "blackman",
]
