#!/usr/bin/python
#python strip
'''
this is the introdaction for this
strips,please read carefully!
'''
while True:
 reply = input('Enter text: ')
 if reply == 'stop':break
 try:
  num = int(reply)
 except:
  print('bad!' * 2)
 else:
  print(int(reply) ** 2)
print('bye')
