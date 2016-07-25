#!/bin/bash
read -e "This program is using for install virtualbox" BOXV

if [ $BOXV == "y" ];then
    yum install virtualbox -y
    yum install virtualbox-dkms -y
    yum install virtualbox-source -y
    yum install virtualbox-qt -y
else
    echo "Wrong ! program is quiting ...."
fi
