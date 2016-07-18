#!/usr/bin/python3
#python strip
from operator import itemgetter
from itertools import groupby
d = {'logmessage':''}
L = []
TempData = []
for z in open('vmlog'):
    if z[:24] == ']':
        d['logmessage'] = d['logmessage'] + str(TempData)
        TempData = []
        L.append(d)
        i = 0
        d = {}
        d['day'] = z[1:24]
        d['logmessage'] = z[26:]
        L.append(d)
    else:
        TempData.append(z)
        i = 1

L.sort(key = itemgetter('day'))
for day,items in groupby(L, key = itemgetter('day')):
    print day
    for i in items:
        print ' ',i
print L
print d
#print TempData
