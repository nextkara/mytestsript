#!/usr/bin/env python3

listconfig = []
print("the configuration show to you now")
for x in open('ifcfg-enp0s3','r'):
    print(x)
    print('change or not? ;p')
    choice = input()
    if choice == 'yes':
        print(x.split('=')[1])
        print('please input your choice')
        change=input()
        listconfig.append(x.split('=')[0] + '=' + change + '\n')
    elif choice =='no':
        listconfig.append(x)
with open('net.cfg','w+') as f:
    for x in listconfig:
        f.write(x)
