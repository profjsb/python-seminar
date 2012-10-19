# basic GUI Hello in Tkinter
from Tkinter import *

#make a root window
root = Tk() ; root.title("grid example")
root.minsize(120,50)
root.maxsize(700,500)


# stick a label in it and pack it in.
a = Label(root, text="A",borderwidth=4,bg="PeachPuff")
b = Label(root, text="B",borderwidth=4,bg="LightBlue",relief=RIDGE)
c = Label(root, text="C",borderwidth=4,bg="PeachPuff",relief=GROOVE)
d = Label(root, text="D",borderwidth=4,bg="LightBlue")
e = Label(root, text="E",borderwidth=4,bg="PeachPuff",relief=GROOVE)
f = Label(root, text="F",borderwidth=4,bg="LightBlue")
g = Label(root, text="G",borderwidth=4,bg="Yellow")
h = Label(root, text="H",borderwidth=4,bg="PeachPuff",relief=SUNKEN)
i = Label(root, text="I",borderwidth=4,bg="LightBlue")
j = Label(root, text="J",borderwidth=4,bg="PeachPuff",padx=30,relief=GROOVE)
k = Label(root, text="K",borderwidth=4,bg="LightBlue",relief=GROOVE)

a.grid(row=0,column=0)
b.grid(row=0,column=1,sticky=(N,S,E,W))
c.grid(row=0,column=2,sticky=(N,S))
e.grid(row=1,column=0,sticky=(E,W))
f.grid(row=1,column=1,sticky=(E))
g.grid(row=1,column=2,sticky=(W))
h.grid(row=2,column=0,sticky=(N,S,W,E))
d.grid(row=0,column=3,sticky=(N,S,W,E),columnspan=2,rowspan=2)
i.grid(row=2,column=1,sticky=(N,S,W,E),columnspan=2)
j.grid(row=2,column=3,sticky=(N,S,W,E))
k.grid(row=2,column=4,sticky=(N,S,W,E),ipadx=30,ipady=30)

    
## get the gridsize and make each row and column expandable 
for r in range(root.grid_size()[0]):
    root.rowconfigure(r, weight=1)
for c in range(root.grid_size()[1]):
    root.columnconfigure(c, weight=1)

# run the main loop
root.mainloop()