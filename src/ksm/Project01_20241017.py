import folium  
import os
import webbrowser
import requests
import json
import pandas as pd
import numpy as np
import time

from folium.plugins import MarkerCluster    

path = './data/shelter_location.csv'
df = pd.read_csv(path, encoding='utf-8')

# print(df)
# print(df.info())
# print('- '*50)
# print(df.describe())

# 나의 위치(현재 학원: 서울 마포구 양화로 122)
myLa = 37.55403252137646
myLo = 126.92056491925895
m = folium.Map(location=[myLa ,myLo] , zoom_start=11)

# req = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
# data = req.content
# seoul_geo = json.loads(data)
# folium.GeoJson(seoul_geo, name='구역표시').add_to(m)

cnt_seoul= 0
print('- '*50)

folium.Marker(
            location = (myLa, myLo),
            tooltip="현재위치",
            popup=folium.Popup("현재 주소 : 서울 마포구 양화로 122", min_width=50, max_width=200),
            icon=folium.Icon(icon="cloud", color="blue"),
            ).add_to(m)

pc_cluster = MarkerCluster().add_to(m)

for k in range(len(df)):
    if df.iloc[k,4] =="사용중":
        if isinstance(df['도로명전체주소'][k], str) and df['도로명전체주소'][k][0:2] == "서울":  
            cnt_seoul= cnt_seoul+1
            folium.Marker(
            location = (df.iloc[k,22], df.iloc[k,23]),
            tooltip=df.iloc[k,5],
            popup=folium.Popup('최대인원 :' +str(df.iloc[k,12])+' // 주소 :' +str(df.iloc[k,7]), min_width=50, max_width=200),
            icon=folium.Icon(color="red"),
            ).add_to(pc_cluster)
            
m_path = './data/shelter_map.html'
m.save(m_path)
webbrowser.open(os.path.realpath(m_path))
print(m_path,' testing...')
print()

print('서울 대피소 숫자:',cnt_seoul)
'''
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   번호            18161 non-null  int64
 1   관리번호          18161 non-null  object
 2   지정일자          18161 non-null  object
 3   해제일자          1092 non-null   object
 4   운영상태          18161 non-null  object
 5   시설명           18161 non-null  object
 6   시설구분          18161 non-null  object
 7   도로명전체주소       18147 non-null  object
 8   소재지전체주소       18161 non-null  object
 9   도로명우편번호       18139 non-null  float64
 10  시설위치(지상/지하)   18161 non-null  object
 11  시설면적(㎡)       18161 non-null  float64
 12  최대수용인원        18161 non-null  int64
 13  최종수정시점        18161 non-null  object
 14  데이터갱신구분       18161 non-null  object
 15  데이터갱신일자       18161 non-null  object
 16  위도(도)         18161 non-null  int64
 17  위도(분)         18161 non-null  int64
 18  위도(초)         18161 non-null  float64
 19  경도(도)         18161 non-null  int64
 20  경도(분)         18161 non-null  int64
 21  경도(초)         18161 non-null  float64
 22  위도(EPSG4326)  18155 non-null  float64
 23  경도(EPSG4326)  18155 non-null  float64
 24  좌표정보(X)       18155 non-null  float64
 25  좌표정보(Y)       18155 non-null  float64
'''


