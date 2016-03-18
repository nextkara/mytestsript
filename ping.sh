#!/bin/bash
#
NUMP=1
while :;do
  ping -c 1 59.71.12.$NUMP &> /dev/null
  if [ $? -eq 0 ];then
    echo "ping 59.71.12.$NUMP success.."
  else
    echo "ping 59.71.12.$NUMP unsuccess.."
  fi
  let NUMP=$NUMP+1
  if [ $NUMP -eq 192 ];then
    break
  fi
done
