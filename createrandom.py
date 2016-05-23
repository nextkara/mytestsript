#!/usr/bin/python
import random
count = input("how many>> ")
maxnum = input("Max is >> ")
minnum = input("Min is >> ")
p = open("num.txt",'w')
for x in range(0,int(count)):
    p.write(str(random.randint(int(minnum),int(maxnum))))
    p.write('\n')
p.close()
