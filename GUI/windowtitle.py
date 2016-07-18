#!/usr/bin/python3
from tkinter import *
root = Tk()
widget = Label(root)
widget.config(text = 'hello GUI world')
widget.pack(side = TOP, expand = YES, fill = BOTH)
root.title('NextGUI')
root.mainloop()