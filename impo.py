#!/usr/bin/python3
#python strip
'''
print ('header')
title = "the meaning of title"
a = 'a!'
b = 'b!'
c = 'c!'
'''
'这是创建用户和删除用户的脚本'
import getpass
import fileinput
print("this a root program, and you should enter you password")
user = getpass.getuser()
passwd = getpass.getpass()
def svc_login(user, passwd):
    '''
    支持缓冲区协议和 canexport C 连续缓冲区对象。这包括所有字节、 bytearray，和文件对象，
    以及 manycommon memoryview 对象。 字节类似物体可以被用于各种行动来处理二进制数据;
    这些 includecompression，保存到一个二进制文件，并通过套接字发送。
    有些操作需要可变的二进制数据。 文档通常是指这些作为"读写字节喜欢的对象"。
    Examplemutable 缓冲区对象包括 bytearray 和一个 bytearray，
    其中 amemoryview。其他操作需要的二进制数据被存储的 inimmutable 对象 
    （"只读字节-喜欢的对象"）;例子包括字节和字节对象的内存视图。
    '''
    #TODO 完善后续密码加密功能，将加密的密码与输入的密码进行加密操作后对比，进行验证
    passwdFile = open('/test/passwd','r')
    for LineP in passwdFile:
        if user == lineP.split(":")[0]:
            if passwd == lineP.split(":")[1]
            print("Login successful")
        else:
            pass
    else:
        print("Login unsuccessful")
if svc_login(user, passwd):
    print("权利越大，责任越大，我想你应该明白这点")
with fileinput.input() as f_input:
    with open("delusr.sh", "w+") as f:
        for line in f_input:
            Nline = line.split(":")[0]
            f.write('userdel ' + line)
            print("this user will be put in del list: " + line,end='')
