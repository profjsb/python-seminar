from enthought.traits.api import HasTraits, Str, Float, Instance; import math
from enthought.traits.ui.api import View, Item, ButtonEditor

from mpl_figure_editor import MPLFigureEditor

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

t = Test()
t.configure_traits()