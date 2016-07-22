#!/bin/bash
BIRTH=1204
TODAY=`date +%d`
THISMOUTH=`date +%m`
BAI=100
BIRTHMOUTH=$(($BIRTH % $THISMOUTH))
BIRTHDAY=$(($BIRTH / $BAI))

MCHA=$(($BIRTHMOUTH - $THISMOUTH))
DAYCHA=$(($BIRTHDAY - $TODAY))
if [ $DAYCHA -le 3 ] && [ $MCHA -eq 0 ];then
    echo -e "\bBirthday is coming soon..Birthday is $BIRTH"
else
    echo 'Today ,no birthday'
fi
