#!/usr/bin/python3
#复制文件及移动文件
'''
Warning
Even the higher-level file copying functions (shutil.copy(), shutil.copy2()) cannot copy all file metadata.
On POSIX platforms, this means that file owner and group are lost as well as ACLs.
On Mac OS, the resource fork and other metadata are not used. 
This means that resources will be lost and file type and creator codes will not be correct.
On Windows, file owners, ACLs and alternate data streams are not copied.
大致意思就是不能完全复制所有的元数据，因为平台限制
'''
import shutil
#不保留元数据
shutil.copy("/etc/fstab", "fstab")
#路线作为字符串写入，要加引号
#保留元数据
shutil.copy2("/etc/fstab", "fstab2")
#递归复制
shutil.copytree( "/var/log/", "/home/nextkara/t/python/more/a")
#移动文件和目录
shutil.move("fstab", "fstab3")
#保留符号链接
shutil.copytree("/val/log/","home/nextkara/t")
#只拷贝符号链接本身
shutil.copy2("link", "link2", follow_symlinks=False)
