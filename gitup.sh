#!/bin/bash
#this is new line
#other line
if [ $1 == null ];then
  CHANGE = "Something change we don't know"
else 
   CHANGE = $1
fi
echo "What's change in new file"
echo "Please live a message for update:"
git status -s
echo "Please wait 3 seconds..."
sleep 3
git add .
git commit -m "$CHANGE"
git push 

