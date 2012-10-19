# basic GUI Hello in Tkinter

from Tkinter import *

#make a root window
root = Tk()
root.title("Hello?")

# stick a label in it.
mylabel = Label(root, text="Is it me you're looking for?")

# pack it into the root window
mylabel.pack()

# run the main loop
root.mainloop()