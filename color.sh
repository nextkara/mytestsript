#!/bin/bash
#show color and add special color to your scripts
while :;do
cat << EOF
a|A send red to your code >>>>>
b|B send green to your code >>>>>>
q|Q for quit this program >>>>>>
EOF
read -p "your choice and your file:" CHOICE
read -p "your file:" SENDFILE
read -p "times you want to add:" TIMESA
case $CHOICE in

a|A)echo 'echo -e "\e[1;31m this is red text \e[0m"' >> $SENDFILE;;
b|B)echo 'echo -e "\e[31;42m this is Greem \e[0m"' >>$SENDFILE;;
q|Q)quit;;
*);;
esac
let TIMESA=$TIMESA-1
[ $TIMESA -eq 0 ] && break

done
