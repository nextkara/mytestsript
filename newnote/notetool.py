#!/usr/bin/python
class Display:
    def showNote(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s ----\n %s' % (key,showNote(self,key)))
        return '----\n '.join(attrs)
    def __str__(self):
        return '%s ----\n %s \n -------- \n ' % (self.__class__.__name__, self.showNote())
        
    def showMenu(self):
        print('Please select your choices ')
        print('1,add new note ')
        print('2,update new note')
        print('3,exit')
    def selectMenu(self,choices):
        self.choices = choices
        
class InputChoice:
    choices = input()
    def getChoices(self, choices):
        if choices == 1:
            self.addNote()
        elif choices == 2:
            self.updateNote()
        elif choices == 3: 
            exit()
    def addNote(self):
        print('your title:')
        title = input()
        print('your note:')
        newnote = input()
    def update(self):
        print('your title:')
        titleNo = input()
        if type(titleNo) is str:
            self.key = titleNo
        else:
            print('nothing to do')
            self.update()
        
             
         