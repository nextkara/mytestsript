#!/bin/bash
#this is new line
#other line
echo "What's change in new file"
echo "Please live a message for update:"
git status -s
echo "Please wait 3 seconds..."
sleep 3
git add .
git commit -m "$1"
git push 

