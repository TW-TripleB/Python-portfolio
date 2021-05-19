from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,LocationSendMessage,StickerSendMessage,TemplateSendMessage,PostbackTemplateAction,MessageTemplateAction,ConfirmTemplate
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('EU3EHNEz94DGmWAhXI488KZYlbqA3Nw+qtbFJGAVaXIMiIhhWwSlNdV6Bec67YHtrW9EY0ZQ0L20xvGw9BT3s94msFgxg21Lg3L85rB/w+kqYe7Im53En7zqOoJky4Bf+IGAYfQGaxZKxKskIsyiAQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('dde6f90f7884388f53c0528770cbcb70')
'''
def _getArticle():
    global myUrl,totaL,numS,timeS
    rQ=requests.get(myUrl,cookies=myCookies).text   #模擬送出cookies的驗證值
    souP=BeautifulSoup(rQ,"html5lib")    
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
'''

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


def searchKey(msg):
    word = {'聯成':'成人補習班','停水':'台中供五停二','美女':'周子瑜'}
    return word.get(msg,'不知道你說什麼？')

status=0
# line_bot_api.push_message("Uc4720f0b27099d3bfbbaaae5f2b5d086",TextSendMessage(text="Say yes to me"))
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    global status
    
    msg = event.message.text
    
    if '自行車' in msg:
        station,sbi,bemp = getTPbike()
        info = ''
        for i in range(10):
            info += station[i]+'-'+str(sbi[i])+'-'+str(bemp[i]) + '\n'
        msg = info
        
    elif '空氣品質' in msg:
        status = 1
        msg = '請輸入地區：'
    elif '圖' in msg:
        status = 99
    elif "sticker" in msg:
        status=97
        
    elif 'map' in msg:
        status = 98
    elif "ptt" in msg:
        status=95
        num,date,title,link,author=ptt()
        info=""
        for i in range(10):
            info+=num[i]+"\n"+date[i]+"\n"+title[i]+"\n"+link[i]+"\n"+author[i]+"\n"
        msg=info
    elif "威力彩" in msg:
        status=69
        number,number2=lottery()
        jackpot="第一區號碼:"
        for i in number:
            jackpot+=str(i)+","
        for j in number2:
            jackpot+="\n"+"第二區號碼:"+str(j)
        msg=jackpot
        
    elif "chat box" in msg:
        status=96
    else:    
        # if status == 1:
        #     # msg = getAir(msg)
        # else:                
        #     msg = searchKey(msg)
        status = 0    
    
    if status == 99:
        message = ImageSendMessage(original_content_url='https://images.chinatimes.com/newsphoto/2021-01-30/656/20210130003822.jpg',preview_image_url='https://images.chinatimes.com/newsphoto/2021-01-30/656/20210130003822.jpg')
    elif status == 98:
        message = LocationSendMessage(title='聯成逢甲',address='台中市逢甲路',latitude=24.177879,longitude=120.642695)
    elif status==97:
        message=StickerSendMessage(package_id="1",sticker_id="1")
    elif status == 96:
        message=TemplateSendMessage(alt_text="視窗確認訊息",template=ConfirmTemplate(text="是否購買?",actions=[PostbackTemplateAction(label='Yes',text="Yes",data="item=2"),MessageTemplateAction(label="No",text="No")]))
    else:
        message = TextSendMessage(text=msg)
    line_bot_api.reply_message(
        event.reply_token,
        message)
pttdict={}
myUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
timeS=10    #此變數是用來剔除管理員公告之用
numS=0      #計算[爆]新聞的總數
totaL=0     #計算今日新聞的總數
from lotterypower import lottery
import random
import os
from searchbike import getTPbike
# from air import getAir
from PTTbomb import ptt
import requests
from bs4 import BeautifulSoup
import datetime   #載入[datetime]模組，協助處理日期問題
'''
myCookies={"over18":"1"}
    
todaY1=datetime.date.today()
todaY2=str(todaY1).split("-")   #todaY2是一個串列(list)
if int(todaY2[1]) < 10:         
    todaY=" "+str(int(todaY2[1]))+"/"+todaY2[2]    #月份若為單位數，前面會有一個空格
else:   
    todaY=todaY2[1]+"/"+todaY2[2]
'''
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
