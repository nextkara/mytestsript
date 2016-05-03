#!/usr/bin/python3
import os
line = os.popen('lsb_release -a | grep -e "^Description.*"|cat -vET').read()
line = line.replace('^I','').split(':')[1].split(' ')[0]
print(line)
