'''
selenium--運動相簿--運動筆記[https://running.biji.co/]
'''
import os
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

wdriveR=webdriver.Chrome()
wdriveR.maximize_window()

urL = "https://running.biji.co/index.php?q=album&act=photo_list&album_id=43488&cid=8074&type=album&subtitle=%E6%AF%8D%E5%AD%90%E9%B1%B7%E9%AD%9A%E9%A6%96%E5%B1%86%E5%9C%8B%E9%9A%9BY%E6%8B%96%E9%A6%AC%E6%8B%89%E6%9D%BE%20%E5%8F%B0%E5%8C%97%E5%A0%B4-%E7%B4%847%E5%85%AC%E9%87%8C2"
#urL=input("請輸入相簿網址: ")

wdriveR.get(urL)  #開啟瀏覽器
#隱性等待 10 秒
wdriveR.implicitly_wait(10)

for vI in range(50):
    # 向下捲動，會花費一些時間
    wdriveR.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)

souP=BeautifulSoup(wdriveR.page_source,"html5lib")  
titlE = souP.find("h1","album-title flex-1").text.strip()   # 標題
allImgs = souP.find_all("img","photo_img photo-img")
# 以標題建立目錄儲存圖片
imagesDir=titlE + "/"
if not os.path.exists(imagesDir):
    
    os.mkdir(imagesDir)
    # 處理所有 <img> 標籤
    nN=0
    for imG in allImgs:
        # 讀取 src 屬性內容(圖檔完整路徑)
        fullPath=imG.get("src")
        if fullPath != None:
            fileName = fullPath.split('/')[-1]  # 取得圖檔名
            print(fullPath)
            # 儲存圖片
            try:
                imagE = urlopen(fullPath)
                with open(os.path.join(imagesDir,fileName),"wb") as filE:
                    filE.write(imagE.read())  
                nN=nN+1
            except:
                print("{} 無法讀取!".format(fileName))
                
    print("共下載",nN,"張圖片")                
else:
    print("這個相簿已經有了耶!!")    

wdriveR.quit() #關閉瀏覽器並退出驅動程式
    
