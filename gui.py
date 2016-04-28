import sys, os
from tkinter import *
from tkinter.messagebox import showinfo
def reply():
    showinfo(title = 'popup', message = 'button pressed')
window = Tk(className = 'Jump one')
te = os.getcwd()
button = Button(window, text = te, command = reply)
button.pack()
window.mainloop()

