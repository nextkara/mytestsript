#!/usr/bin/python
import shelve
from notetool import Display
class Note(Display):
    def __init__(self, title, youNote):
        self.title = title
        self.youNote = youNote
    def removeNote(self, numBer):
        pass
    def updateNote(self, numBer):
        pass
    def addNote(self):
        pass
class secertNote(Note):
    def protectNote(self):
        print('this is a secret note!')
if __name__ == '__main__':
    