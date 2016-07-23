#!/usr/bin/env python3
import os
line = ''
PathFile = '/usr/bin/python'
print('this is first on Module OS')
print(os.path.basename(PathFile))
print(os.path.dirname(PathFile))
print('second')
print(PathFile.split('/')[-1])

for x in PathFile.split('/')[1:-1]:
    line = line + '/' + x

print(line)
