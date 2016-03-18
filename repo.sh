#!/bin/bash
while :;do
 w | grep 'nextkara' &> /dev/null
 if [ $? -eq 0 ];then 
   echo "nextkara is login ... "
 else
   break
 fi
sleep 2
done
