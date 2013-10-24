from mpl_figure_editor import MPLFigureEditor

# do pip install wx
import wx
 
import matplotlib
# We want matplotlib to use a wxPython backend
matplotlib.use('WxAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

try:
    from enthought.traits.api import Any, Instance

    from enthought.traits.api import HasTraits
    from enthought.traits.ui.api import View, Item
except:
    from traits.api import Any, Instance
    from traits.api import HasTraits
    from traitsui.api import View, Item

from numpy import sin, cos, linspace, pi

class Test(HasTraits):

        figure = Instance(Figure, ())

	view = View(Item('figure', editor=MPLFigureEditor(),
                                show_label=False),
                        width=400,
                        height=300,
                        resizable=True)

        def __init__(self):
            super(Test, self).__init__()
            axes = self.figure.add_subplot(111)
            t = linspace(0, 2*pi, 200)
            axes.plot(sin(t)*(1+0.5*cos(11*t)), cos(t)*(1+0.5*cos(11*t)))

Test().configure_traits()
