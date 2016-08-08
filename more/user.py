#!/usr/bin/python3
import sys
S1 = sys.argv[1]
S2 = sys.argv[2]
L = 0
try:
    L = int(S1)        
except ValueError:
    if S1 == "rm":
        with open("userdel.sh","w+") as f2:
            f.write("#!/bin/bash")
            for x in range(1, int(S2)):
                f.write("userdel -r usr" + str(S2))
if L != 0:
    with open("adduser.sh","w+") as f:
        f.write("#!/bin/bash")
        for x in range(1,int(S1)+1):
            f.write("useradd -u 120" + str(x) + " user" + str(x))
            f.write("cp -r /etc/skel/.[^.]* /testdir/user" + str(x))
            f.write("echo centos | passwd --stdin usr" + str(x))