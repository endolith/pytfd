from __future__ import division
import pytfd.plot
from test_data1 import *
from pytfd.sm import sm
from pytfd import windows

#from enthought.mayavi import mlab as M


for i, T in enumerate([32, 64]):
    w = windows.rectangular(T) # Rectangular window
    P = windows.hanning(2 + 1)
    #P = array([0, 1, 0])
    delta1 = zeros(N)
    delta1[N//4] = 5
    delta2 = zeros(N)
    delta2[3*N//4] = 5
    y = sin(2*pi*10*t) + sin(2*pi*30*t) + delta1 + delta2
    Y_sm = sm(y, w, P)
    pytfd.plot.contour(abs(Y_sm)[N//2:])
    #x, y = meshgrid(t, f)
    #x, y = mgrid[0:256, 0:256]
    #M.surf(x, y, abs(Y_sm))
    #M.surf(x, y, lambda x,y:sin(x**2 + y**2))
    #M.axes()
    #M.title('Demoing mlab.surf')
#     figure()
#     contour(t, f[:N//2], abs(Y_sm)[N//2:])
#     xlabel("Time")
#     ylabel("Frequency")
#     title(r"SM T = %d$T_s$"%T)
#     savefig('sin_delta_T%d'%T)
