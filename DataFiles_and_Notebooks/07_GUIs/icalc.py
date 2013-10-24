# useful Traits-based GUI instant calc
# J. S. Bloom (2012) Python Seminar Class AY250

try:
	from enthought.traits.api import HasTraits, Str, Float ; import math
except:
	from traits.api import HasTraits, Str, Float ; import math
	
seval = lambda expr: eval(expr, dict(__builtins__=None), vars(math))

class Calc(HasTraits):
    expression = Str
    rez        = Str("Type an expression")
    def _expression_changed(self, old, new):
            try:
                self.rez = str(seval(new))
            except:
                pass

c = Calc() ; c.configure_traits()
