#!/usr/bin/python
#python strip
#root     ssh:notty    222.243.153.132  Tue May 24 14:09 - 14:09  (00:00)
l = [] 
for line in open('lastb.txt','r'):
    #l.append([line.split('ssh:notty    ')[0].rstrip(),line.split('ssh:notty    ')[1][0:16]])
    lines = line.split('ssh:notty    ')
    #print(lines)
    #print(lines[0],lines[1])
    user = lines[0].rstrip()
    ipaddr = lines[1].rstrip()
    l.append([user,ipaddr])
print(l)