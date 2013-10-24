try:
  from enthought.traits.api import HasTraits, Str, Float, Instance; import math
  from enthought.traits.ui.api import View, Item, ButtonEditor
except:
  from traits.api import HasTraits, Str, Float, Instance; import math
  from traitsui.api import View, Item, ButtonEditor

from matplotlib.figure import Figure

from mpl_figure_editor import MPLFigureEditor
import numpy as np

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
     t = np.linspace(0, 2*np.pi, 200)
     axes.plot(np.sin(t)*(1+0.5*np.cos(11*t)), np.cos(t)*(1+0.5*np.cos(11*t)))

t = Test()
t.configure_traits()