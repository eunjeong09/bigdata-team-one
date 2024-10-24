import urllib.request
import os.path
import json
import time
import requests
import pandas as pd
url = "http://openapi.seoul.go.kr:8088/71714f72486e6f3037386a676f4a67/json/VTsClnswspfGnrl/1/100/"

req = requests.get(url)
req.raise_for_status()
# print(req)
json_df =req.json()
time.sleep(1)
data = json_df['VTsClnswspfGnrl']['row']
issues = pd.DataFrame(data,columns=["CGG_NM","FACIL_SE","EMER_FACIL_LOC","RWT_QUA","GEN_KND","SRV_DIV"])
# df = pd.DataFrame(json_df['VTsClnswspfGnrl']['row'],index=range(1,len(json_df['VTsClnswspfGnrl']['row'])+1))
print(issues)
'''
PS C:\Mtest\workrestAPI> & C:/Users/user/anaconda3/envs/ck/python.exe c:/Mtest/workrestAPI/testjason.py
Empty DataFrame
Columns: [CGG_NM, FACIL_SE, EMER_FACIL_LOC, RWT_QUA, GEN_KND, SRV_DIV]
Index: []

'''




# items = json.load(open('./data/서울시 민방위 비상급수시설현황.json','r',encoding='utf-8'))
# path = open('.서울시 민방위 비상급수시설현황.json','r', encoding='utf-8').read()
# mydata = json.loads(path)
# print(mydata)
# print(' ♟️ '*20)
# for item in items:
#     print(item['name'] + ' : ' + item['owner']['login'])

# print()