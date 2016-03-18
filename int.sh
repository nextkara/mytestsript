#!/bin/bash
#
TwoInt() {
A='1a'
B='2'
C=$[$A+$B]
echo $C
}
TwoInt
echo $?
