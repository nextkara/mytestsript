#!/usr/bin/python
#异常处理测试脚本
def kaboom(x, y):
    print(x + y)
try:
    kaboom([1, 2, 3], "Spam")
except TypeError:
    print('hello world')#对异常进行自定义处理
finally:
    '只要程序没被中断，这段一定会运行，可以用来关闭文件等后续扫尾的操作'
    print('Always run!')
print('resuming here')
'处理好的异常不会中断程序的正常执行'
    