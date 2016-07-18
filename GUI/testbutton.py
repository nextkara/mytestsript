#!/usr/bin/python3
from tkinter import *
import sys
class gui:
    def __init__(self,parent = None):
        times = 0
    def checkAgain(times):
        times += 1
        print('you click ',times,'times')
    def buttonA():
        self.widget = Button(None, text = 'hello Gui', command = sys.exit())
        self.widget.pack()
        self.widget.mainloop()
T = gui
T.buttonA()

