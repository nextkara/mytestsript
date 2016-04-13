#!/bin/bash
zypper addrepo -f http://mirrors.aliyun.com/opensuse/update/leap/42.1/oss  openSUSE-42.1-Update-Oss
zypper addrepo -f http://mirrors.aliyun.com/opensuse/update/leap/42.1/non-oss/ openSUSE-42.1-Update-Non-Oss
zypper addrepo -f http://mirrors.aliyun.com/opensuse/distribution/leap/42.1/repo/oss/ openSUSE-42.1-Oss
zypper addrepo -f http://mirrors.aliyun.com/opensuse/distribution/leap/42.1/repo/non-oss/  openSUSE-42.1-Non-Oss
zypper addrepo -f http://mirrors.aliyun.com/packman/openSUSE_Leap_42.1/ aliyun-packman
zypper in -y gcc
zypper in -y vlc
zypper in -y virtualbox

