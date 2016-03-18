#!/bin/bash
#copy python strip that can run
if [ $1 == 'rm' ];then
 shift
 rm $1.py
 echo "Now is remove this file ...$1.py"
else
 echo "Now starting copying file..."
 cp copy.py $1.py
 echo "copy finished ...the file name is $1.py"
fi
