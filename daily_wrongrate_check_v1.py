from pymongo import MongoClient
import datetime
import re
# client = MongoClient(SERVER, username = UID, password = PWD, authSource = AUTHSOURCE)[DATABASE]
client=MongoClient('172.16.76.193',27017,
                    username = "apacuser",
                    password = "apacuser@prod",
                    authSource = "CDP_DataReceiver"
                   )
if client:
    print("connected")

db=client["CDP_DataReceiver"]

if db:
    print("acessed")
col=db["wrongDataV2"]
utc_now = datetime.datetime.utcnow()
before_day = (utc_now - datetime.timedelta(days = 1)).strftime('%Y-%m-%d') + 'T07:00:00Z'
time_func = input(str("select fuction: 1. same time as daily report, 2. set time range : "))
countryCode = input(str("select country: 1. USA, 2. CAN : "))

def get_wrong(website, time_func):
    if time_func == "1":
        gt = before_day
        lte = utc_now.strftime('%Y-%m-%dT%H:%M:%SZ')
    if time_func == "2":
        gt = input(str("輸入gt : 格式:2022-04-10T07:00:00Z : "))
        lte = input(str("輸入lte : 格式:2022-04-10T07:00:00Z : "))
        regex = re.compile('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z')
        match = regex.fullmatch(gt)
        match2 = regex.fullmatch(lte)
        if gt >= lte :
            print("gt must < lte")
            get_wrong(website, time_func)
            return 
        elif match:
            pass
        elif match2:
            pass
        else:
            print("format type error----")
            get_wrong(website, time_func)
            return

    wrongdata = col.aggregate([{"$match":{"website":f'{website}','receiveTime':{"$gt":datetime.datetime.strptime(gt,'%Y-%m-%dT%H:%M:%SZ'),"$lte":datetime.datetime.strptime(lte, '%Y-%m-%dT%H:%M:%SZ')}}},{"$group":{'_id':"$wrongs.issue",'count':{"$sum":1}}},{"$sort":{'count':-1}}])
    print(f"-----------------{website}-----------------")
    for row in wrongdata:
        print(row)


if __name__ == "__main__":
    websiteMap_USA = {'1':'www.amazon.com','2':'www.bestbuy.com', '3':'www.bhphotovideo.com','4':'www.microcenter.com','5':'www.officedepot.com', '6':'www.staples.com', '7':'www.walmart.com'}
    websiteMap_CAN = {"1":"www.amazon.ca","2":"www.bestbuy.ca","3":"www.canadacomputers.com","4":"www.memoryexpress.com"}
    if time_func == "1": 
        if countryCode == "1" :    
            websites = ['www.amazon.com', 'www.bestbuy.com', 'www.bhphotovideo.com', 'www.microcenter.com', 'www.officedepot.com', 'www.staples.com', 'www.walmart.com']
        elif countryCode == "2" : 
            websites = ["www.amazon.ca","www.bestbuy.ca","www.canadacomputers.com","www.memoryexpress.com"]
    elif time_func == "2" :
        if countryCode == "1" :
            website = input(str("select website: 1.www.amazon.com, 2.www.bestbuy.com, 3.www.bhphotovideo.com, 4.www.microcenter.com, 5.www.officedepot.com, 6.www.staples.com, 7.www.walmart.com : "))
            websites = [websiteMap_USA[website]]
        elif countryCode == "2" : 
            website = input(str("select website: 1.www.amazon.ca, 2.www.bestbuy.ca, 3.www.canadacomputers.com, 4.www.memoryexpress.com : "))
            websites = [websiteMap_CAN[website]]
    for i in websites:
        get_wrong(i, time_func)