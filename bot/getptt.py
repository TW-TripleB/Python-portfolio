'''
PTT八卦板爬網示範程式-4(將今日文章存成JSON檔的另一種形式)
'''
def getArticles():        #傳入的網址存放在[urL]
    global timeS,numS,totaL     #在函式(區域)內，要更改全域變數的值，必須先宣告其為[global]
    myCookies={"over18":"1"}
    rQ=requests.get(myUrl,cookies=myCookies).text   #模擬送出cookies的驗證值
    souP=BeautifulSoup(rQ,"html5lib")  
    for mySoup in souP.find_all("div","r-ent"):
        if mySoup.find("div","date").text != todaY:   #判斷文章日期是否不是今日
            timeS = timeS - 1   #不是的話就把[timeS]減一
            if timeS==0:        #[timeS]為零時，傳回[None]，程式就此結束
                return None
        else: 
            try:    #宣告一個[字典]資料型態變數(itemDict)，用來暫存每一篇八卦文章的資料
                totaL=totaL+1        
                itemDict={str(totaL):
                    {"標題":mySoup.find("div","title").text.strip()
                    ,"日期":mySoup.find("div","date").text.strip()
                    ,"超連結":"https://ptt.cc"+mySoup.find("div","title").a["href"].strip()
                    ,"作者":mySoup.find("div","author").text.strip()
                    ,"推文":mySoup.find("div","nrec").text.strip()}
                    }
                pttDict.update(itemDict)   #將字典型態的八卦文章存入[字典]內
            except:
                continue
    nextUrl="https://www.ptt.cc"+souP.find("div","btn-group btn-group-paging").find_all("a")[1]["href"]        
    return nextUrl   #傳回[上頁]文章的網址

import requests
from bs4 import BeautifulSoup
import datetime
import json

myUrl="https://www.ptt.cc/bbs/Gossiping/index.html"

todaY1=datetime.date.today()
todaY2=str(todaY1).split("-")   #todaY2是一個串列(list)
if int(todaY2[1]) < 10:         
    todaY=" "+str(int(todaY2[1]))+"/"+todaY2[2]    #月份若為單位數，前面會有一個空格
else:   
    todaY=todaY2[1]+"/"+todaY2[2]

timeS=10    #非在函式內宣告，所以是[全域]變數，此變數是用來剔除管理員公告之用
totaL=0     #計算今日新聞的總數
pttDict={}     #宣告一個[字典]資料型態變數(pttDict)，用來存放所有八卦文章的資料


while myUrl:   #使用條件式迴圈來處理下一頁資料的問題，只要[myUrl]不為空值就繼續抓下一頁的資料
    myUrl=getArticles()   #[_getArticles()]是我們的自訂函式，用來處理網頁資料抓取

fileName=str(datetime.date.today())+".json"
with open(fileName,"w",encoding="utf-8") as filE:
    json.dump(pttDict,filE,ensure_ascii=False,indent=4)

    
with open(fileName,"r",encoding="utf-8") as filE:
    dictFile=json.load(filE)

for keY,valuE in dictFile.items():
    print(keY)
    print(valuE)
    print("--------------------------------------------")
print("今天是: ",todaY1)
print("全部新聞共有: ",totaL," 篇")

