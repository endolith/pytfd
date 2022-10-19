import numpy
from numpy import hamming, hanning, blackman

def rectangular(T):
    return numpy.ones(T)

def gaussian(T, a=1):
    L = T//2
    t = numpy.linspace(-L, L, T)
    N = L//2
    return numpy.exp(-((t)/(a*N))**2)

def kaiser(T):
    T = T//2
    t = numpy.linspace(-T, T, 2*T)
    return 0.42 + 0.5*numpy.cos(t*pi/T) + 0.08*numpy.cos(2*t*pi/T)

__all__ = [
    "hanning",
    "hamming",
    "rectangular",
    "gaussian",
    "kaiser",
    "blackman",
]
