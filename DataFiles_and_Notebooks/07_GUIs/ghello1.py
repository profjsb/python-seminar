# basic GUI Hello in Tkinter
from Tkinter import *

#make a root window
root = Tk() ; root.title("Hello?")

# stick a label in it and pack it in.
Label(root, text="Is it me you're looking for?").pack()

def good(): print "good."
def bad(): print "bad!"
    
# make some buttons
b1 = Button(root,text="Yes",command=good)
b2 = Button(root,text="No",command=bad)
b1.pack(side=LEFT,expand=1,fill=X) ; b2.pack(side=LEFT,fill=X,expand=1)


# run the main loop
root.mainloop()