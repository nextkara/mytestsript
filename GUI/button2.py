#!/usr/bin/python3
import sys
from tkinter import *

widget = Button(None, text = 'Hello Gui', command = (lambda: print('hello lambda world') or sys.exit() ))
widget.pack()
widget.mainloop()
