#!/usr/bin/python3
#python strip
#异常测试脚本，功能待完善~
class SeeErorr(Exception):
    raise IndentationError('Good')
a = SeeErorr()        
def rasieErorr(Eo):
    raise IndexError(Eo)
try:
    rasieErorr('my error')
except ValueError:
    print('inside error')
