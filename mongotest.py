from pymongo import MongoClient
import pandas as pd
# client = MongoClient(SERVER, username = UID, password = PWD, authSource = AUTHSOURCE)[DATABASE]
client=MongoClient('172.16.76.192',27017,
                    username = "crawlerdbo",
                    password = "crawler@20140918",
                    authSource = "crawler"
                   )
if client:
    print("connected")
db=client["crawler"]
if db:
    print("acessed")
col=db["urls"]

# data={
#     "name":"noob",
#     "alexa":"10000",
#     "url":"https://www.amazon.com"
# }

# exe=col.insert_one(data)
# collist=db.collection_names()
# if "sites" in collist:
#     print("column exist")
# else:
#     print("fail")
df = pd.read_excel("SAU_SAUReport-20220406_0901.xlsx",
                sheet_name="sheet2"

                )
data=[]
url=[]

for i in col.find({"tid" : 806401}, {'u':1}):
    if i['u'] not in data:
        data.append(i['u'])
for k in df["url"]:
    url.append(str(k))
for j in data:
    if j not in url:
        print(j)
