'''
PTT八卦板爬網示範程式-5(計算當日新聞總數與[爆]新聞數量)(非函式版)
'''

from bs4 import BeautifulSoup
import datetime
from selenium import webdriver 
import json  #載入[datetime]模組，協助處理日期問題

myUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
headLess=webdriver.ChromeOptions()
headLess.add_argument("headLess")
wwW=webdriver.Chrome(options=headLess)


wwW.implicitly_wait(10)
wwW.get(myUrl)
wwW.maximize_window()
buttoN=wwW.find_element_by_class_name("btn-big")
buttoN.click()
#myCookies={"over18":"1"}
dictfilE={}
todaY1=datetime.date.today()
todaY2=str(todaY1).split("-")   #todaY2是一個串列(list)
if int(todaY2[1]) < 10:         
    todaY=" "+str(int(todaY2[1]))+"/"+todaY2[2]    #月份若為單位數，前面會有一個空格
else:   
    todaY=todaY2[1]+"/"+todaY2[2]

timeS=10    #此變數是用來剔除管理員公告之用
numS=0      #計算[爆]新聞的總數
totaL=0     #計算今日新聞的總數

while True:   
    souP=BeautifulSoup(wwW.page_source,"html5lib")   #模擬送出cookies的驗證值    
    for mySoup in souP.find_all("div","r-ent"):
        if mySoup.find("div","date").text != todaY:   #判斷文章日期是否不是今日
            timeS = timeS - 1   #不是的話就把[timeS]減一
        else: 
            totaL=totaL+1
            try:
                if mySoup.find("div","nrec").text=="爆":   #研判推文是否為[爆]等級
                    numS=numS+1   #計算[爆]等級的新聞共有幾篇
                    print("日期: ",mySoup.find("div","date").text)
                    print(mySoup.find("div","title").text.strip())
                    print("ptt.cc"+mySoup.find("div","title").a["href"])
                    print("作者: ",mySoup.find("div","author").text)
                    #print("推文: ",mySoup.find("div","nrec").text) 
                    print("=================================================")
                    itemDict={str(totaL):
                              {"標題":mySoup.find("div","title").text.strip()
                              ,"日期":mySoup.find("div","date").text.strip()
                              ,"超連結":"https://ptt.cc"+mySoup.find("div","title").a["href"].strip()
                              ,"作者":mySoup.find("div","author").text.strip()
                              ,"推文":mySoup.find("div","nrec").text.strip()}
                              }
                    dictfilE.update(itemDict)
            except:
                continue
    if timeS<=0:        #[timeS]小於零時，離開結束迴圈
        break
    bottoN=wwW.find_element_by_partial_link_text("上頁").click()
fileName=str(datetime.date.today())+".json"
with open(fileName,"w",encoding="utf-8") as filE:
    json.dump(dictfilE,filE,ensure_ascii=False,indent=4)        
    
print("今天是: ",todaY1)
print("全部新聞共有: ",totaL," 篇")
print("爆新聞總共有:",numS,"篇")    

wwW.quit()