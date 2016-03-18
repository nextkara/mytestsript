#!/bin/bash
read -e "This program is using for install virtualbox" BOXV
if [ $BOXV == "y" ];then

apt-get install virtualbox -y
apt-get install virtualbox-dkms -y
apt-get install virtualbox-source -y
apt-get install virtualbox-qt -y

else
echo "Wrong ! program is quiting ...."
fi
