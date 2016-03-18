#!/usr/bin/python
#python strip
myfile = open('py.txt','rw')
myfile.write('come on baby!\n')
T = ['hello','my','girl']
myfile.write(T)
F = myfile.readline()
print(F)
myfile.close()
