import numpy
from numpy import hamming, hanning, blackman

def rectangular(T):
    return numpy.ones(T)

def gaussian(T, a=1):
    L = T//2
    t = numpy.linspace(-L, L, T)
    N = L//2
    w = numpy.exp(-((t)/(a*N))**2)
    return w

def kaiser(T):
    T = T//2
    t = numpy.linspace(-T, T, 2*T)
    w = 0.42 + 0.5*numpy.cos(t*pi/T) + 0.08*numpy.cos(2*t*pi/T)
    return w

__all__ = [
    "hanning",
    "hamming",
    "rectangular",
    "gaussian",
    "kaiser",
    "blackman",
]
