
#!/bin/bash
ping -c 3 www.baidu.com
if [ $? -eq 0 ];then
  echo "successful"
else
  echo "nosuccessful"
fi
 
