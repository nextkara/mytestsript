#!/bin/usr/env python3
'''
import pymysql
db = pymysql.connect("YourIP", "UserName", "Password", "database")
cursor = db.cursor()
cursor = execute("select * from database")
try:
    '提交'
    db.commit()
except:
    '失败回滚'
    db.rollback()
db.close()


con = pymysql.connect("192.168.238.128", "root", "root", "person")
cur = con.cursor()
cur.execute("INSERT INTO `information`(Name,Age, Sex, Income) VALUES ('MaD', 20, 'M', 2000)")
cur.execute("insert into `information`(`Name`,`Age`,`Sex`,`income`)values('GF','209','s','234')")
print(cur.execute("select * from information"))
con.commit()
cur.close()
con.close()    
''' 
import pymysql as mysql
import re,sys
installPack = re.compile(r'Installed:')
removePack = re.compile(r'Erased:')
logdict_time = []
logdict_packname = []
logdict_packname2 = []
logdict_time2 = []
countInstall = []
countRemove = []
y1 = 0
y2 = 0
IPserver = "192.168.238.128"
User = "root"
Passwd = "root"
Tofile = "yes"
def mysqlselect(choice):
    if choice == "c":
        db = mysql.connect(IPserver,User,Passwd)
    elif choice == "d":
        db.close()
    elif choice == "u":
        try:
            db.commit()
        except:
            db.rollback()
            print("must have something wrong with  it ,now it's going to rollback your action to last commit")
def reSelect():
    with open(log) as f1:
        for x in f1:
            try:
                Find1 = installPack.findall(x)[0].split(" ")
                logdict_time.append(Find1[0] + " " + Find1[1] + " " + Find1[2] + " ")
                logdict_packname.append(Find1[-1])
            except IndexError:
                pass
            try:
                Find2 = removePack.findall(x)[0].split(" ")
                logdict_time2.append(Find2[0] + " " + Find2[1] + " " + Find2[2] + " ")
                logdict_packname2.append(Find2[-1])
            except IndexError:
                pass
def sqlChange(select):
    if select == "no"
        
    