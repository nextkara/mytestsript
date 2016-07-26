#!/bin/bash
#homework for magedu
#3、显示/etc/passwd文件中以bash结尾的行
[nextkara@centos ~]$ cat /etc/passwd | grep '.*bash$'
root:x:0:0:root:/root:/bin/bash
nextkara:x:503:503::/home/nextkara:/bin/bash

#4、显示/etc/passwd文件中的两位数或三位数
[nextkara@centos ~]$  grep '[[:digit:]]\{2,3\}\:' /etc/passwd
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologi n
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
gopher:x:13:30:gopher:/var/gopher:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
saslauth:x:499:76:"Saslauthd user":/var/empty/saslauth:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
memcached:x:498:499:Memcached daemon:/var/run/memcached:/sbin/nologin
ldap:x:55:55:LDAP User:/var/lib/ldap:/sbin/nologin
mysql:x:500:500::/home/mysql:/sbin/nologin
nginx:x:501:501::/home/nginx:/sbin/nologin
www:x:502:502::/home/www:/sbin/nologin
nextkara:x:503:503::/home/nextkara:/bin/bash
munin:x:497:498:Munin user:/var/lib/munin:/sbin/nologin
apache:x:48:48:Apache:/var/www:/sbin/nologin

#5、显示`netstat -tan`命令结果中以‘LISTEN’后跟0个、1个或者多个空白字符结尾的行
[nextkara@centos ~]$ netstat -tan | grep '.*LISTEN[[:space:]]\?'
tcp        0      0 0.0.0.0:11211               0.0.0.0:*                   LISTEN      
tcp        0      0 0.0.0.0:80                  0.0.0.0:*                   LISTEN      
tcp        0      0 0.0.0.0:21                  0.0.0.0:*                   LISTEN      
tcp        0      0 0.0.0.0:22                  0.0.0.0:*                   LISTEN      
tcp        0      0 127.0.0.1:25                0.0.0.0:*                   LISTEN      
tcp        0      0 0.0.0.0:3306                0.0.0.0:*                   LISTEN      

#6、添加用户bash、testbash、basher以及nologin用户（nologin用户的shell为/sbin/nologin）；而后找出/etc/passwd文件中用户名与其shell名相同的行
[root@centos nextkara]# useradd bash testbash basher 
[root@centos nextkara]# useradd -s /bin/nologin nologin

#7、显示当前系统上root、centos或者user1用户的默认shell和UID （请事先创建这些用户，若不存在）
[root@centos nextkara]# id root centos user1
uid=0(root) gid=0(root) groups=0(root)
nextkara:x:503:503::/home/nextkara:/bin/bash
for x in open('/etc/passwd'):
    if x.split(:)[1] == 'root':
        print(x.split(:)[-1])
    elif x.split(:)[1] == 'centos':
        print(x.split(:)[-1])
    elif x.split(:)[1] == 'usr1':
        print(x.split(:)[-1])

#8、找出/etc/rc.d/init.d/functions文件中某单词（单词中间可以存在下划线）后面跟着一组小括号的行
[nextkara@centos ~]$ grep '[[:lower:]]*_[[:lower:]]*()' /etc/rc.d/init.d/functions 
fstab_decode_str() {
__readlink() {
__fgrep() {
__umount_loop() {
__umount_loopback_loop() {
__pids_var_run() {
__pids_pidof() {
echo_success() {
echo_failure() {
echo_passed() {
echo_warning() {
update_boot_stage() {
get_numeric_dev() {
is_ignored_file() {
is_true() {
is_false() {
apply_sysctl() {
key_is_random() {
find_crypto_mount_point() {
init_crypto() {

#9、使用echo输出一个路径，而后egrep找出其路径基名；进一步的使用egrep取出其目录名
[nextkara@VM_82_212_centos ~]$ echo /etc/rc.d/init.d/functions | egrep '/.*/' --color
/etc/rc.d/init.d/functions
[nextkara@VM_82_212_centos ~]$ echo /etc/rc.d/init.d/functions | egrep '[a-z]*$' --color 
/etc/rc.d/init.d/functions

#10、找出ifconfig命令执行结果中1-255之间的数字
[nextkara@centos ~]$ ifconfig | egrep '[1-2][0-5][0-5]\.|[0-9]\.|[0-9][0-9]\.' --color
          inet addr:10.105.82.212  Bcast:10.105.127.255  Mask:255.255.192.0
          RX bytes:1414135433 (1.3 GiB)  TX bytes:1698261352 (1.5 GiB)
          inet addr:127.0.0.1  Mask:255.0.0.0
          RX bytes:2968 (2.8 KiB)  TX bytes:2968 (2.8 KiB)
          
#、复制/etc/grub.cfg配置文件至/tmp目录，用查找替换命令删除/tmp/grub.cfg文件中的行首的空白字符；
 vim 末行模式下 :%s/^[[:space:]]*//
 [nextkara@centos ~]$ sed 's/^[[:space:]]*//' grub.conf
#、复制/etc/rc.d/init.d/functions文件至/tmp目录，用查找替换命令为/tmp/functions
#的每行开头为空白字符的行的行首加一个#; 原有空白字符保留；
[nextkara@centos ~]$ sed 's/^[[:space:]]/#&/' fun.txt 
备注：&：表示引用前面模式中匹配到的内容
#、替换/tmp/functions文件中的/etc/sysconfig/init为/var/log；
sed 's/\/etc\/sysconfig\/init/\/var\/log/'
  vim 末行模式下 : %s/\/etc\/sysconfig\/init/\/var\/log/
#、删除/tmp/functions文件中所以#开头，且#后面至少跟了一个空白字符的行的行首#;
sed 's/^#[[:space:]]{1,}/&/'
#0、查找/var目录属主为root，且属组为mail的所有文件；
[nextkara@VM_82_212_centos ~]$ find /var -user root -group mail 
##、查找/usr目录下不属于root、bin或hadoop的所有文件；
[root@localhost ~]# find /usr -not -user root -o -not -user bin  |head
/usr
/usr/bin
/usr/bin/nroff
/usr/bin/comm
/usr/bin/catchsegv
/usr/bin/pic
/usr/bin/cp
/usr/bin/gencat
/usr/bin/post-grohtml
/usr/bin/getent

##、查找/etc目录下最近一周内其内容修改过，且属主不为root或hadoop的所有文件；
[root@localhost ~]# find /etc -not -user root -o -not -user hadoop -atime -7
/etc
/etc/fstab
/etc/crypttab
/etc/mtab
/etc/resolv.conf
/etc/pki
/etc/pki/rpm-gpg
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-Debug-7
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-Testing-7

##、查找当前系统上没有属主或属组，且最近一周内曾被访问过的所有文件；
[root@localhost ~]# find / -nouser -o -nogroup -atime -7
find: ‘/proc/3422/task/3422/fd/6’: 没有那个文件或目录
find: ‘/proc/3422/task/3422/fdinfo/6’: 没有那个文件或目录
find: ‘/proc/3422/fd/6’: 没有那个文件或目录
find: ‘/proc/3422/fdinfo/6’: 没有那个文件或目录

##、查找/etc目录下大于20k且类型为普通文件的所有文件；
[root@localhost ~]# find /etc -size -20k -ls 
16777345   12 drwxr-xr-x  77 root     root         8192 7月 18 14:41 /etc
16777346    4 -rw-r--r--   1 root     root          501 4月  8 19:09 /etc/fstab
16777347    0 -rw-------   1 root     root            0 4月  8 19:09 /etc/crypttab
16777348    0 lrwxrwxrwx   1 root     root           17 4月  8 19:09 /etc/mtab -> /proc/self/mounts
18353673    4 -rw-r--r--   1 root     root           73 7月 18 14:23 /etc/resolv.conf
33595531    0 drwxr-xr-x   9 root     root           91 5月 12 17:59 /etc/pki
50331789    0 drwxr-xr-x   2 root     root          101 4月  8 19:09 /etc/pki/rpm-gpg
50331790    4 -rw-r--r--   1 root     root         1690 12月  9  2015 /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
50331791    4 -rw-r--r--   1 root     root         1004 12月  9  2015 /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-Debug-7
50331792    4 -rw-r--r--   1 root     root         1690 12月  9  2015 /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-Testing-7

##、查找/etc目录下所有用户都没有写权限的文件；

##、查找/etc目录下至少有一类用户没有执行权限的文件；

##、查找/etc/init.d目录下，所有用户都有执行权限，且其它用户拥有写权限的文件；

##、让普通用户能使用/tmp/cat去查看/etc/shadow文件；

#9、创建目录/test/data，让某组内普通用户对其有写权限，且创建的所有文件的属组为目录所属的组；此外，每个用户仅能删除自己的文件；


note:
    权限： 
        r: read 读
        w: write 写
        x： excute 执行
        
        文件：默认没有执行权限
        目录：
            r: 可获取其下文件列表，不能使用ls -l 命令；
            w: 可修改此目录下的文件列表，即创建或删除文件；
            x：可cd 至此目录中，且可使用 ls -l 来获取所有文件的详细属性
            
        mode ： rwxrwxrwx
        ownership: user, groups
每一类用户权限组合机制：
    ---------
    rwxrwxrwx
        664 775 600 755
        