# basic events (1) GUI stuff
#   shows commands and Variables/textvaribles usage
# J. S. Bloom (2012) Python Seminar Class AY250

from Tkinter import *
root = Tk()
myvar = StringVar()
myvar.set("this is the first time I've set")

Entry(root, width=7, textvariable=myvar).pack()
def changing(*args):
    print "new value for myvar:", myvar.get()

myvar.trace("w",changing) ; print 'Tkinter calls myvar:', myvar._name
myvar.set("bye.")

root.mainloop()
