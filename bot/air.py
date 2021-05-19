import json
import requests

def getAir(site):
    url="https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&format=json"
    air=json.loads(requests.get(url).text)
    content={}
    allair=air["records"]
    for row in allair:
        name=row["SiteName"]
        status=row["Status"]
        content[name]=status
    return content.get(site,"couldn't find")
