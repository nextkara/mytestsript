#!/usr/bin/env python3
#文件是否存在检测脚本
import os
fileList = [ 'v.sh', 'wechat.py', 'zypper.log', 'ssld.py']
i = 0
Flag=0
'''
if not os.path.exists('z.py'):
    with open('z.py','wt') as f:
        f.write('hello again!\n')
else:
    print('file exist!')
'''
for x in fileList:
    print('check for ' + x +'....',)
    if os.path.exists(x):
        print('yes')
        i += 1
    else:
        print('no')
        Flag = i
if i == 4:
    print('Makefile created already')
else:
    print('this file is already loss..' + fileList[Flag])