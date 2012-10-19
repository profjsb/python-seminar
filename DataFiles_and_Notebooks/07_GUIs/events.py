# basic events GUI stuff
#   shows commands and Variables/textvaribles usage
# quote of the day
# J. S. Bloom (2012) Python Seminar Class AY250

from Tkinter import *
import urllib2
import string 

#make a root window
root = Tk() ; root.title("event example")

# make a string variable
qt = StringVar()

# here are two callback function we'll reference later
def report_quote(*args):
    # qt will hold quote of the day
    print "Quote changed to:"
    print qt.get()
    
def show_quote(*args):
    # disable the quote button to avoid multiple clicks
    a.configure(state=DISABLED)
    a.update_idletasks()    
    
    # grab a new quote from the web
    qt.set(" ".join([string.replace(x,"&quot;","'",100) for x in urllib2.urlopen("http://www.iheartquotes.com/api/v1/random").readlines()[:-2]]))
    
    # set the button state back to normal (enabled) and update all the Event Loop Tasks
    a.configure(state=NORMAL)
    root.update()
    
# here we set up some widgets...note how we set 
# the textvariable parameter of the Label e to the StringVar qt
# whenever qt changes, so will the textvariable of this Label
e  = Label(root,height=15,width=65,justify=LEFT,\
          textvariable=qt,relief=SUNKEN)

# destroy() is a method of all widgets in Tk
q  = Button(root, text="Quit",command=root.destroy)
a  = Button(root, text="Get Quote",command=show_quote)

# set the initial variable and set a watch on qt's change
# 'w' is for generating an event on writing
# 'r' is for generating an event on reading of that variable
qt.set("Click 'Get Quote'") ; print 'qt is a StringVar named', qt._name
qt.trace("w",report_quote)

# pack in all the buttons
e.pack(side=TOP,fill=X,expand=1)
q.pack(side=LEFT,expand=1)
a.pack(side=LEFT,expand=1)

# run the main loop
root.mainloop()
