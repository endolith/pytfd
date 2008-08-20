"""
Demonstrates how to convert mathtext to a wx.Bitmap for display in various
controls on wxPython.
"""
from __future__ import division

import matplotlib
matplotlib.use("WxAgg")
#from numpy import arange, sin, pi, cos, log
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx

IS_GTK = 'wxGTK' in wx.PlatformInfo
IS_WIN = 'wxMSW' in wx.PlatformInfo
IS_MAC = 'wxMac' in wx.PlatformInfo

############################################################
# This is where the "magic" happens.
from matplotlib.mathtext import MathTextParser
mathtext_parser = MathTextParser("Bitmap")
def mathtext_to_wxbitmap(s):
    ftimage, depth = mathtext_parser.parse(s, 150)
    return wx.BitmapFromBufferRGBA(
        ftimage.get_width(), ftimage.get_height(),
        ftimage.as_rgba_str())
############################################################

from pytfd import windows
from pytfd.distributions import *
from signals_test import signals

# Windows
T = 64
w = windows.hanning(T) # Rectangular window
P = windows.hanning(2 + 1)


def _abs(X):
    return abs(X)[X.shape[0]//2:]

distributions = [
    (r'STFT'                 , lambda x: _abs(stft(x, w))),
    (r'S-method'             , lambda x: _abs(sm(x, w, P))),
    (r'PWD'                 , lambda x: _abs(pwd(x, w))),
    (r'WD'                 , lambda x: _abs(wd(x))),
]

class CanvasFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(550, 350))
        self.SetBackgroundColour(wx.NamedColor("WHITE"))

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.distribution = distributions[0][1]
        self.signal = signals[0][1]
        self.process()

        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.add_buttonbars()
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.add_toolbar()  # comment this out for no toolbar

        menuBar = wx.MenuBar()

        # File Menu
        menu = wx.Menu()
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this simple sample")
        self.Bind(wx.EVT_MENU, self.OnExit)
        menuBar.Append(menu, "&File")

        if IS_GTK or IS_WIN:
            # Signals menu
            menu = wx.Menu()
            for i, (mt, signal) in enumerate(signals):
                bm = mathtext_to_wxbitmap(mt)
                item = wx.MenuItem(menu, 2000 + i, "")
                item.SetBitmap(bm)
                menu.AppendItem(item)
                self.Bind(wx.EVT_MENU, self.OnChangeSignal, item)
            menuBar.Append(menu, "&Signals")

            # Equation Menu
            menu = wx.Menu()
            for i, (mt, dist) in enumerate(distributions):
                bm = mathtext_to_wxbitmap(mt)
                item = wx.MenuItem(menu, 1000 + i, "")
                item.SetBitmap(bm)
                menu.AppendItem(item)
                self.Bind(wx.EVT_MENU, self.OnChangeDistribution, item)
            menuBar.Append(menu, "&Distributions")

        self.SetMenuBar(menuBar)

        self.SetSizer(self.sizer)
        self.Fit()

    def add_buttonbars(self):
        # Signals
        self.signal_bar = wx.Panel(self)
        self.sizer.Add(self.signal_bar, 0, wx.LEFT | wx.TOP | wx.GROW)

        self.signal_bar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self.signal_bar, label="Izaberite distribuciju:")
        self.signal_bar_sizer.Add(label, 1, wx.GROW)
        for i, (mt, dist) in enumerate(signals):
            bm = mathtext_to_wxbitmap(mt)
            button = wx.BitmapButton(self.signal_bar, 1000 + i, bm)
            self.signal_bar_sizer.Add(button, 1, wx.GROW)
            self.Bind(wx.EVT_BUTTON, self.OnChangeSignal, button)

        self.signal_bar.SetSizer(self.signal_bar_sizer)

        # Distributions
        self.distribution_bar = wx.Panel(self)
        self.sizer.Add(self.distribution_bar, 0, wx.LEFT | wx.TOP | wx.GROW)

        self.distribution_bar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self.distribution_bar, label="Izaberite distribuciju:")
        self.distribution_bar_sizer.Add(label, 1, wx.GROW)
        for i, (mt, dist) in enumerate(distributions):
            bm = mathtext_to_wxbitmap(mt)
            button = wx.BitmapButton(self.distribution_bar, 1000 + i, bm)
            self.distribution_bar_sizer.Add(button, 1, wx.GROW)
            self.Bind(wx.EVT_BUTTON, self.OnChangeDistribution, button)

        self.distribution_bar.SetSizer(self.distribution_bar_sizer)


    def add_toolbar(self):
        """Copied verbatim from embedding_wx2.py"""
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        if IS_MAC:
            self.SetToolBar(self.toolbar)
        else:
            tw, th = self.toolbar.GetSizeTuple()
            fw, fh = self.canvas.GetSizeTuple()
            self.toolbar.SetSize(wx.Size(fw, th))
            self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()

    def OnPaint(self, event):
        self.canvas.draw()

    def OnChangeDistribution(self, event):
        self.change_distribution(event.GetId() - 1000)

    def change_distribution(self, dist_number):
        self.distribution = distributions[dist_number][1]
        self.process()

    def OnChangeSignal(self, event):
        self.change_signal(event.GetId() - 2000)

    def change_signal(self, signal_number):
        self.signal = signals[signal_number][1]
        self.process()

    def process(self):
        s = self.distribution(self.signal)
        self.axes.clear()
        self.axes.imshow(s)
        self.Refresh()

    def OnExit(self, event):
        self.Close()


class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

app = MyApp()
app.MainLoop()

