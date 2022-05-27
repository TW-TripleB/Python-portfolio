from pymongo import MongoClient
import datetime
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


def get_wrong(website, time_func):
    if time_func == "1":
        gt = before_day
        lte = utc_now.strftime('%Y-%m-%dT%H:%M:%SZ')
    if time_func == "2":
        gt = input(str("輸入gt : 格式:2022-04-10T07:00:00Z : "))
        lte = input(str("輸入lte : 格式:2022-04-10T07:00:00Z : "))
        if gt >= lte :
            print("gt must < lte")
            get_wrong(website, time_func)
            return 
    wrongIssue = col.aggregate([{"$match":{"website":f'{website}','receiveTime':{"$gt":datetime.datetime.strptime(gt,'%Y-%m-%dT%H:%M:%SZ'),"$lte":datetime.datetime.strptime(lte, '%Y-%m-%dT%H:%M:%SZ')}}},{"$group":{'_id':"$wrongs.issue",'count':{"$sum":1}}},{"$sort":{'count':-1}}])
    print(f"-----------------{website}-----------------")
    for row in wrongIssue:
        print(row)
        issue = row["_id"][0]
        wrongData = col.find({'website':f'{website}','wrongs.issue':f'{issue}','receiveTime':{"$gt":datetime.datetime.strptime(gt,'%Y-%m-%dT%H:%M:%SZ'),"$lte":datetime.datetime.strptime(lte, '%Y-%m-%dT%H:%M:%SZ')}}).sort([('receiveTime',-1)])
        try:
            for num in range(1):
                if wrongData[num] and wrongData[num]:
                    print("Url:",wrongData[num]['taskUrl'])
                    print("pageType:", wrongData[num]["pageType"])
                    # print("SKU:",wrongData[num]['sku'])
                    print("data:",wrongData[num]["data"])
        except:
            continue
        print()

if __name__ == "__main__":
    websiteMap = {'1':'www.amazon.com','2':'www.bestbuy.com', '3':'www.bhphotovideo.com','4':'www.microcenter.com','5':'www.officedepot.com', '6':'www.staples.com', '7':'www.walmart.com'}
    if time_func == "1":     
        websites = ['www.amazon.com', 'www.bestbuy.com', 'www.bhphotovideo.com', 'www.microcenter.com', 'www.officedepot.com', 'www.staples.com', 'www.walmart.com']
    elif time_func == "2" :
        website = input(str(" 1.www.amazon.com, 2.www.bestbuy.com, 3.www.bhphotovideo.com, 4.www.microcenter.com, 5.www.officedepot.com, 6.www.staples.com, 7.www.walmart.com : "))
        websites = [websiteMap[website]]
    for i in websites:
        get_wrong(i, time_func)
    
    
