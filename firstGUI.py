from tkinter import *
'''
class Greet:
    def __init__(self):
        self.a = 0
    def greeting():
        print('hello GUI')
        if self.a == 1:
            print('On')
            self.a = 0
        elif self.a == 0:
            print('Off')
            self.a = 1
win = Frame()
win.pack()
Label(win, text = 'hello Contianer').pack(side = TOP)
Button(win, text = 'hello', command = greeting).pack(side = LEFT)
Button(win, text = 'Quit', command = win.quit).pack(side = RIGHT)
'''
'''
widget = Label(None, text = 'hello GUI world')
widget.pack(expand = YES, fill = BOTH)
widget.mainloop()
win.mainloop()
'''
class Hello:
    def __init__(self, parent=None):
        self.top = Frame(parent)
        self.top.pack()
        self.data = 0
        self.make_widgets()
    def make_widgets(self):
        Button(self.top, text = 'Bye', command = self.top.quit).pack(side=LEFT,fill=Y)
        Button(self.top, text = 'Hi ', command = self.massage).pack(side=RIGHT,fill=Y)
        Button(self.top, text = 'Clear', command = self.clear).pack(side=)
    def massage(self):
        self.data += 1
        print('hello number',self.data,)
        if self.data % 2 == 0:
            print('off')
        elif self.data % 2 == 1:
            print('on')
if __name__ == '__main__':
    Hello().top.mainloop()