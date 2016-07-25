#!/usr/bin/python3
#python strip
class SeeErorr(Exception):
    raise IndentationError('Good')
a = SeeErorr()        
def rasieErorr(Eo):
    raise IndexError(Eo)
try:
    rasieErorr('my error')
except ValueError:
    print('inside error')
