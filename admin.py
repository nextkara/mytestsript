#!/usr/bin/python
#python strip
#nextkara:x:1000:100:nextkara:/home/nextkara:/bin/bash
#f = open('/home/nextkara/t/mytestsript/passwd.txt','r')
d = {}
for line in open('passwd.txt','r'):
    d[line.split(':')[0]] = int(line.split(':')[2])
#print(d)
#f.close()
#d2 = { key:value for key,value in d.items()}
for key in d.keys():
    print(key," ===> ",d[key])