'''
PTT八卦板爬網示範程式-5(計算當日新聞總數與[爆]新聞數量)(非函式版)
'''
def _getArticle():
    global myUrl,totaL,numS,timeS
    rQ=requests.get(myUrl,cookies=myCookies).text   #模擬送出cookies的驗證值
    souP=BeautifulSoup(rQ,"lxml")    
    for mySoup in souP.find_all("div","r-ent"):
        if mySoup.find("div","date").text != todaY:   #判斷文章日期是否不是今日
            timeS = timeS - 1   #不是的話就把[timeS]減一
        else: 
            totaL=totaL+1
            try:
                if mySoup.find("div","nrec").text=="爆":   #研判推文是否為[爆]等級
                    numS=numS+1   #計算[爆]等級的新聞共有幾篇
                    itemdict={str(numS):
                    {"Date:":mySoup.find("div","date").text,
                    "Title:":mySoup.find("div","title").text.strip(),
                    "Link:":"ptt.cc"+mySoup.find("div","title").a["href"],
                    "Author:":mySoup.find("div","author").text}}
                pttdict.update(itemdict)
            except:
                continue
    if timeS<=0:        #[timeS]小於零時，離開結束迴圈
        return None
    return "https://www.ptt.cc"+souP.find("div","btn-group btn-group-paging").find_all("a")[1]["href"]    
def ptt():
    global myUrl
    while myUrl:
        myUrl=_getArticle()
    num=list()
    date=list()
    title=list()
    link=list()
    author=list()
    for row,value in pttdict.items():
        num.append(str(row))
        date.append(value["Date:"])
        title.append(value["Title:"])
        link.append(value["Link:"])
        author.append(value["Author:"])

    return num,date,title,link,author

pttdict={}

myUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
timeS=10    #此變數是用來剔除管理員公告之用
numS=0      #計算[爆]新聞的總數
totaL=0     #計算今日新聞的總數


import requests
from bs4 import BeautifulSoup
import datetime   #載入[datetime]模組，協助處理日期問題
myCookies={"over18":"1"}
    
todaY1=datetime.date.today()
todaY2=str(todaY1).split("-")   #todaY2是一個串列(list)
if int(todaY2[1]) < 10:         
    todaY=" "+str(int(todaY2[1]))+"/"+todaY2[2]    #月份若為單位數，前面會有一個空格
else:   
    todaY=todaY2[1]+"/"+todaY2[2]

ptt()

