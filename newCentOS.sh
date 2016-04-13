#!/bin/bash
mkdir /cdrom
rm -rf /etc/yum.repos.d/*
echo "[cdrom]
name=CDROM
baseurl=file:///cdrom
gpgcheck=0
enable=1" > /etc/yum.repos.d/cdrom.repo
echo "set ai
set nu">>/root/.vimrc
mount /dev/cdrom /cdrom
yum makecache
yum install -y vim
yum install -y tree
yum install -y gcc
yum install -y finger

