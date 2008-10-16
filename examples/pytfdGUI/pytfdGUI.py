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

DIST_CACHE = {}

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

        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.add_choices()
        #self.add_button_plot()
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.add_toolbar()  # comment this out for no toolbar

        menuBar = wx.MenuBar()

        # File Menu
        menu = wx.Menu()
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this simple sample")
        self.Bind(wx.EVT_MENU, self.OnExit)
        menuBar.Append(menu, "&File")

        #~ if IS_GTK or IS_WIN:
            #~ # Signals menu
            #~ menu = wx.Menu()
            #~ for i, (mt, signal) in enumerate(signals):
                #~ bm = mathtext_to_wxbitmap(mt)
                #~ item = wx.MenuItem(menu, 2000 + i, "")
                #~ item.SetBitmap(bm)
                #~ menu.AppendItem(item)
                #~ self.Bind(wx.EVT_MENU, self.OnChangeSignal, item)
            #~ menuBar.Append(menu, "&Signals")

            #~ # Equation Menu
            #~ menu = wx.Menu()
            #~ for i, (mt, dist) in enumerate(distributions):
                #~ bm = mathtext_to_wxbitmap(mt)
                #~ item = wx.MenuItem(menu, 1000 + i, "")
                #~ item.SetBitmap(bm)
                #~ menu.AppendItem(item)
                #~ self.Bind(wx.EVT_MENU, self.OnChangeDistribution, item)
            #~ menuBar.Append(menu, "&Distributions")

        self.SetMenuBar(menuBar)

        self.SetSizer(self.sizer)
        self.Fit()

        # Initial plot
        self.distribution_name = distributions[0][0]
        self.signal_name = signals[0][0]
        self.process()


    def add_choices(self):
        # Signals
        self.signal_bar = wx.Panel(self)
        self.sizer.Add(self.signal_bar, 0, wx.LEFT | wx.TOP | wx.GROW)

        self.signal_bar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self.signal_bar, label="Izaberite signal:")
        self.signal_bar_sizer.Add(label, 1, wx.GROW)

        listbox = wx.Choice(self.signal_bar, choices=[i[0] for i in signals])
        listbox.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.OnChangeSignal, listbox)
        self.signal_bar_sizer.Add(listbox, 1, wx.GROW)

        self.signal_bar.SetSizer(self.signal_bar_sizer)

        # Distributions
        self.distribution_bar = wx.Panel(self)
        self.sizer.Add(self.distribution_bar, 0, wx.LEFT | wx.TOP | wx.GROW)

        self.distribution_bar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self.distribution_bar, label="Izaberite distribuciju:")
        self.distribution_bar_sizer.Add(label, 1, wx.GROW)

        listbox = wx.Choice(self.distribution_bar, choices=[i[0] for i in distributions])
        listbox.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.OnChangeDistribution, listbox)
        self.distribution_bar_sizer.Add(listbox, 1, wx.GROW)

        self.distribution_bar.SetSizer(self.distribution_bar_sizer)

    #~ def add_button_plot(self):
        #~ self.button_plot = wx.Button(self, label="Plot!")
        #~ self.Bind(wx.EVT_BUTTON, self.OnButtonPlot, self.button_plot)
        #~ self.sizer.Add(self.button_plot, 0, wx.LEFT | wx.TOP | wx.GROW)

    #~ def OnButtonPlot(self, event):
        #~ self.process()

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

    #~ def OnPaint(self, event):
        #~ self.canvas.draw()
        #~ self.Refresh()

    #~ def OnChangeDistribution(self, event):
        #~ self.change_distribution(event.GetId() - 1000)

    #~ def change_distribution(self, dist_number):
        #~ self.distribution = distributions[dist_number][1]
        #~ self.process()

    def OnChangeSignal(self, event):
        self.change_signal(event.GetString())

    def change_signal(self, signal_name):
        self.signal_name = signal_name
        self.process()

    def OnChangeDistribution(self, event):
        self.change_distribution(event.GetString())

    def change_distribution(self, distribution_name):
        self.distribution_name = distribution_name
        self.process()

    def process(self):
        key = (self.distribution_name, self.signal_name) #Used for caching
        if key in DIST_CACHE:
            s = DIST_CACHE[key]
        else:
            distribution = None
            for (text, _distribution) in distributions:
                if text == self.distribution_name:
                    distribution = _distribution
            if distribution is None:
                raise AttributeError

            signal = None
            for (text, _signal) in signals:
                if text == self.signal_name:
                    signal = _signal
            if signal is None:
                raise AttributeError

            s = distribution(signal)
            DIST_CACHE[key] = s

        self.axes.clear()
        self.axes.imshow(s)
        #print dir(self.axes)
        #print dir(self)
        self.canvas.draw()
        self.Refresh()

    #~ def OnPaint(self, event):
        #~ self.canvas.draw()
        #~ self.Refresh()

    def OnExit(self, event):
        self.Close()


class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

app = MyApp(redirect=False)
app.MainLoop()

