#2048游戏代码
#!/usr/bin/python
import random
GameList = [ [0 for x in range(5)] for y in range(5)]
def SuiJi():
    heng = random.randint(1,5)
    shu = random.randint(1,5)
    return [heng,shu]
SuiList = []
SuiList = SuiJi()
def Test(G,S):
    if G[S[0][0]][S[0][1]] = 0:
        return 1
    else
        SuiList = SuiJi()
        Test()
if Test(GameList,SuiList) == 1:#随机生成2的功能
    GameList[SuiList[0][0]][SuiList[0][1]] = 2
else     
#对方向进行判断的话，w是把第一行以下的数字竖直上移，其余方向与之类似。
