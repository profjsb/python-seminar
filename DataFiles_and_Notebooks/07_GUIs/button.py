try:
	from enthought.traits import *
	from enthought.pyface.api import GUI
	from enthought.traits.api import HasTraits, Int, Button
	from enthought.traits.ui.api import View, Item, ButtonEditor
except:
	from traits import *
	#from pyface.api import GUI
	from traits.api import HasTraits, Int, Button
	from traitsui.api import View, Item, ButtonEditor	

class Counter(HasTraits):
    value =  Int()
    add_one = Button()
    def _add_one_fired(self):
        self.value +=1
    view = View('value', Item('add_one', show_label=False ))

#Counter().edit_traits()
#GUI().start_event_loop()
Counter().configure_traits()

