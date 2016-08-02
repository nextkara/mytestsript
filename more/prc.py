#!/usr/bin/python3
#coding=utf-8
'''
#爬虫脚本待分析
import urllib
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


html = getHtml("http://www.nextkara.net")

print(getImg(html))
'''
#日志分析脚本
import re, sys

#通过正则表达式进行判断日志内容
installPack = re.compile(r'.*Installed:.*')
removePack = re.compile(r'.*Erased:.*')
logdict_In = []
logdict_In2 = []
logdict_Un = []
logdict_Un2 = []
count1 = 0
count2 = 0

y1 = 0
y2 = 0
if sys.argv[0] == []
    log = 'dnf.rpm.log'
else:
    log = sys.argv[0]
#在匹配模式之前加上r,避免匹配模式内的字符被转义,减少错误
with open(log) as f1:
    for x in f1:
        try:
            Find1 = installPack.findall(x)[0].split(" ")
            logdict_In.append(Find1[0] + " " + Find1[1] + " " + Find1[2] + " ")
            logdict_In2.append(Find1[-1])
            '''
            if Nfind1 in logdict_In.keys():
                Nfind1a = Nfind1 + "-" + str(y1)
                logdict_In[Nfind1a] = Find1[-1]
                y1 = y1 + 1
            else:
                y1 = 0
            '''
        except IndexError:
            pass
        try:
            Find2 = removePack.findall(x)[0].split(" ")
            logdict_Un.append(Find2[0] + " " + Find2[1] + " " + Find2[2] + " ")
            logdict_Un2.append(Find2[-1])
            '''
            if Nfind2 in logdict_Un.keys():
                Nfind2a = Nfind2 + "-" + str(y2)
                logdict_Un[Nfind2a] = Find2[-1]
                y2 = y2 + 1
            else:
                y2 = 0
            '''
        except IndexError:
            pass
'''
#测试段
print(logdict_In)
print(logdict_Un)
'''
with open("install.log", "w+") as f2:
    '''
    for key in logdict_In:
        f2.write(key + logdict_In[key] + "\n")
        count1 = count1 + 1
    '''
    for l1 in logdict_In:
        f2.write(l1 + logdict_In2[y1] + ' \n')
        y1 = y1 + 1
    f2.write("A total of " + str(y1) + " packages installed\n")
with open("remove.log", "w+") as f3:
    '''
    for key in logdict_Un:
        f3.write(key + logdict_Un[key] + "\n")
        count2 = count2 + 1
    '''
    for l2 in logdict_Un:
        f3.write(l2 + logdict_Un2[y2] + ' \n')
        y2 = y2 + 1
    f3.write("A total of " + str(y2) + " packages removed\n")
