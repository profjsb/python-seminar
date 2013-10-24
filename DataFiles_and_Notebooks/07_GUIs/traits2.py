try:
    from enthought.traits.api import HasTraits, Str, \
            Int, Float, Enum,DelegatesTo,This,Instance
    from enthought.traits.ui.api import View, Item, Group
except:
    from traits.api import HasTraits, Str, \
            Int, Float, Enum,DelegatesTo,This,Instance
    from traitsui.api import View, Item, Group 
      
import sys

class Bear(HasTraits):
    first_name = Str
    weight = Float
    favorite_food = Enum("Honey","Turkey","PaloAltian",default="Honey")

class Parent(Bear):
    last_name = Str
    def _last_name_changed(self, old, new):
            print "Parent's last name changed to %s (was = '%s')." % (new,old)
            sys.stdout.flush()
            
class Cub(Bear):
    last_name  = DelegatesTo('father')
    father = Instance(Parent)
    mother = Instance(Parent)
    
yogi  = Parent(first_name="Yogi",weight=34.0,last_name="Morgan")
sally = Parent(first_name="Sally",weight=30.0,last_name="Klein")
oski = Cub(first_name="Oski",weight=39.0,father=yogi,mother=sally)

oski.configure_traits()
