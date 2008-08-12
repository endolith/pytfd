'''Plot data supporting the __array_interface__ (e.g. numpy arrays, PIL images, etc.).
>>> import numpy
>>> height,width,depth = 25, 25, 4
>>> arr = numpy.arange( width*height*depth, dtype=numpy.uint8)
>>> arr.shape = height,width,depth
>>> display(arr)
'''
import numpy

from pyglet.gl import *
from pyglet import window
from pyglet import image
from pygarrayimage.arrayimage import ArrayInterfaceImage

from sympy.plotting.managed_window import ManagedWindow



class WindowArray(ManagedWindow):
    def __init__(self, **win_args):
        self.array = win_args.pop('array')
        self.aii = ArrayInterfaceImage(self.array)
        super(WindowArray, self).__init__(**win_args)

    def draw(self):
        self.aii.texture.blit(0, 0, 0)

    def setup(self):
        img = self.aii.texture

        self.width = img.width
        self.height = img.height
        self.set_visible()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


def display(arr):
    w = WindowArray(visible=False, resizable=True, array=arr)


def contour(arr):
    if arr.dtype != 'uint8':
        arr = numpy.uint8(arr/arr.max()*255)
    display(arr)


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
