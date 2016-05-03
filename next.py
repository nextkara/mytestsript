#!/usr/bin/python
#python strip
'''
L = [1,2,3,4]
I = iter(L)
for i in L :
  print next(I)
'''
from tkinter import *
from tkinter.messagebox import showinfo
def reply():
    showinfo(title ='Error', message = 'click this')
def replytoo():
    showinfo(title ='right', message = 'click this')
    
window = Tk(className = 'One')
button = Button(window, text = 'something wrong',command = reply)
button = Button(window, text = 'something right',command = replytoo)
button.pack()
window.mainloop()