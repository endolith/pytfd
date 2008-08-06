'''Plot data supporting the __array_interface__ (e.g. numpy arrays, PIL images, etc.).

'''
import numpy

from pyglet.gl import *
from pyglet import window
from pyglet import image
from pygarrayimage.arrayimage import ArrayInterfaceImage


#pyglet.app.run()

def update(dt):
    print "Hello"
pyglet.clock.schedule_interval(update, 0.1)


def display(arr):
    w = window.Window(visible=False, resizable=True)

    aii = ArrayInterfaceImage(arr)

    img = aii.texture

    w.width = img.width
    w.height = img.height
    w.set_visible()

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    @w.event
    def on_draw():
        w.dispatch_events()
        w.clear()
        img.blit(0, 0, 0)

    event_loop = pyglet.app.EventLoop()

    @event_loop.event
    def on_window_close(window):
        print len(pyglet.app.windows)

    event_loop.run()


        #  while not w.has_exit:
#         w.dispatch_events()
#         img.blit(0, 0, 0)
#         w.flip()


def contour(arr):
    display(numpy.uint8(arr))


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
