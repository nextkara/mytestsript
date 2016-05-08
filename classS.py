#!/usr/bin/python
class Test():
    def __setattr__(self, name ,value):
        self.__dict__[name] = value
        print('set name = ', name)
    def __getattr__(self, name):
        print('output', self.name)
