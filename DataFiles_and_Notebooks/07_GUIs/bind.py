# basic events binding GUI stuff
#   shows binding on a Canvas
# J. S. Bloom (2012) Python Seminar Class AY250

from Tkinter import *

def callback(event):
    print {"4": "Button", "7": "Enter", "2": "Key"}[event.type] + " event->",
    print (event.x,event.y,event.char,event.keysym,"button:",event.num)

root = Tk()
w=Canvas (root) ; w.pack() ; w.focus_set()
callback_name  = w.bind("<Button-1>",callback)
callback_name2  = w.bind("<Enter>",callback)
callback_name4  = w.bind("<Key>",callback)

root.mainloop()
