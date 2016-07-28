#!/usr/bin/python3
#临时文件创建
from tempfile import TemporaryFile
import os
with TemporaryFile('w+') as f:
    f.write('hello python \n')
    print(os.listdir())
    f.write('Bye \n')
    #使用seek()方法后，之前缓冲区里的内容写入临时文件中
    f.seek(0)
    data = f.read()
    print(data)
print(os.listdir())
#临时文件的所在目录不在脚本运行目录
