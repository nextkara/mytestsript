#!/usr/bin/python3
import os
from sys import argv
def SysInfo():
    #line = os.popen('lsb_release -a | grep -e "^Description.*"|cat -vET').read()
    #line = line.replace('^I','').split(':')[1].split(' ')[0]
    line = os.popen('cat /proc/version').read().replace('(' or ')' or '.' ,' ').split(' ')
    return line

def SysCheck(os):
    try:
        if os.index('SUSE') > 0:
            i = 1
            print('your system is openSUSE')
        elif os.index('centos') > 0:
            i = 2
            print('your system is CentOS')
        elif os.index('ubuntu') > 0:
            i = 3
            print('your system is Ubuntu')
    except ValueError:
        print('cannot read your system version')
        i = 99
    return i
def Sysinstall(i):
    if i == 1:
        pass
    elif i == 2:
        pass
    elif i == 3:
        pass
    elif i == 99:
        pass
def helpDoc(argv):
    if argv[1][0] == '-':
        if argv[1][1] == 'h':
            print('this is help')
        else:
            print('nothing to do')
    elif argv is ['']:
        pass
    #print(argv)
if __name__ == '__main__':
    helpDoc(argv)
    os = SysInfo()
    num = SysCheck(os)
    Sysinstall(num)
