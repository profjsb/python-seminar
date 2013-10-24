try:
	from enthought.traits.api import HasTraits, Str, \
            Int, Directory, RGBColor, Float, Array, Enum
	from enthought.traits.ui.api import View, Item, Group
except:
	from traits.api import HasTraits, Str, \
            Int, Directory, RGBColor, Float, Array, Enum
	from traitsui.api import View, Item, Group	

class Bear(HasTraits):
    name = Str
    color = RGBColor("gold")
    weight = Float
    location = Array()
    favorite_food = Enum("Honey","Turkey","PaloAltian",default="Honey")
    datadir = Directory("./")
    
yogi = Bear(name="Yogi",weight=34.0,location=(131.2,+31.1))
yogi.configure_traits()
