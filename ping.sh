#!/bin/bash
#
NUMP=1
while :;do
  ping -c 1 172.18.19.$NUMP &> /dev/null
  if [ $? -eq 0 ];then
    echo -e "ping 172.18.19.$NUMP \e[1;32m success..\e[0m"
  else
    echo -e "ping 172.18.19.$NUMP \e[1;31m unsuccess..\e[0m"
  fi
  let NUMP=$NUMP+1
  if [ $NUMP -eq 254 ];then
    break
  fi
done
