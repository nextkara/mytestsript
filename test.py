#!/usr/bin/python
class Bad(Exception):
    pass
def RasBad():
    raise Bad()
try:
    try:
        raise Bad()
    except Bad:
        print('inside error..')
        '里面的异常被捕获了，在外面看来是里面的代码块运行完毕了，没有输出错误'
except Bad:
    print('Bad now')
else:
    print('No bad thing happened')    