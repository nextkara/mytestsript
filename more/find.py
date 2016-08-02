#!/usr/bin/env python3
import os
import re
#当前目录寻找文件
ListDir = ""
for x in os.listdir():
    ListDir = ListDir + " " + x
L = re.findall("file.log", ListDir, flags=re.IGNORECASE)
print(L)
