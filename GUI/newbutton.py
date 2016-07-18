#!/usr/bin/python
import sys
from tkinter import *
def quit():
    print('hello, I must quit now .... ')
    sys.exit()

widget = Button(None, text = 'hello event world', command = quit)
widget.pack()
widget.mainloop()
