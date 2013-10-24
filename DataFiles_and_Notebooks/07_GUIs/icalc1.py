# useful Traits-based GUI instant calc
# J. S. Bloom (2012) Python Seminar Class AY250

try:
  from enthought.traits.api import HasTraits, Str, Float ; import math
  from enthought.traits.ui.api import View, Group, Item
except:
  from traits.api import HasTraits, Str, Float ; import math
  from traitsui.api import View, Group, Item 
  
seval = lambda expr: eval(expr, dict(__builtins__=None), vars(math))

class Calc(HasTraits):
    expression = Str
    rez        = Str("Type an expression below")
    def _expression_changed(self, old, new):
            try:
                self.rez = str(seval(new))
            except:
                self.rez = ""
                
view1 = View(Item('rez',width=-250,resizable=True,padding=2,
                  label="Result",enabled_when="False",full_size=True),
             Item('expression', width=-250,resizable=True),
                  title='Instant Calc',resizable=True,
                  buttons=['OK'],scrollable=False)
                
c = Calc() ; c.configure_traits(view=view1)
