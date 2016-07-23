#!/usr/bin/env python3
#文件所在路径名，和基名获取方法
#另附自己的方法
import os
line = ''
PathFile = '/usr/bin/python'
print('this is first on Module OS')
#获取路径基名，即当前文件名
print(os.path.basename(PathFile))
#获取路径名，所在目录名
print(os.path.dirname(PathFile))
print('second')
print(PathFile.split('/')[-1])
for x in PathFile.split('/')[1:-1]:
    line = line + '/' + x
print(line)
