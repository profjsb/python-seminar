# basic GUI Hello in Tkinter
from Tkinter import *

#make a root window
root = Tk() ; root.title("pack example")

# stick a label in it and pack it in.
q = Button(root, text="Quit",borderwidth=4,bg="PeachPuff")
a = Checkbutton(root, text="A",borderwidth=4)
b = Checkbutton(root, text="B",borderwidth=4)
c = Checkbutton(root, text="C",borderwidth=4)
e = Label(root, text="What grade should I give you in this class?",borderwidth=4,bg="PeachPuff",relief=GROOVE)

e.pack(side=TOP,fill=X)
q.pack(side=BOTTOM,expand=1,fill=X)
a.pack(side=LEFT,expand=1)
b.pack(side=LEFT,expand=1)
c.pack(side=LEFT,expand=1)

# run the main loop
root.mainloop()