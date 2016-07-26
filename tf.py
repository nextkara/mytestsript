#!/usr/bin/env python3
#文件是否存在检测脚本
import os
if not os.path.exists('z.py'):
    with open('z.py','wt') as f:
        f.write('hello again!\n')
else:
    print('file exist!')
