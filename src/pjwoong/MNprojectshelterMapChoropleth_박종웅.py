import folium 
import os
import webbrowser
import requests
import json
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 사용자 위치 확인
from folium import plugins



# 1. 서울시 인구밀도
df = pd.read_csv('./data/서울시인구밀도.csv')
# print(df)
# print()
# print(df.info()) # 서울시 인구밀도
# print()

# 2. 대피소 위치
dp = pd.read_csv('./data/shelter_location.csv')
# print(dp)
# print()
# print(dp.info()) # 대피소 좌표
# print() 대피소위치


# 현재 지도 좌표
m = folium.Map(location=[37.563646,126.989580], zoom_start=15, tiles="cartodb positron")

# 현재 사용자 위치
plugins.LocateControl().add_to(m)

req = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
data = req.content
seoul_geo = json.loads(data)
folium.GeoJson(seoul_geo, name='구역표시').add_to(m)



#folium.Choropleth




# folium.Choropleth(
#     geo_data=seoul_geo,
#     name="policeChoropleth",
#     data=df,
#     columns=["동별(2)", "인구 (명)"],
#     key_on="feature.properties.name",fill_color="YlGn",
#     fill_opacity=0.5,line_opacity=0.1,
#     legend_name="Unemployment Rate (%)",
# ).add_to(m)



latlong = dp[['위도(EPSG4326)','경도(EPSG4326)','시설명','소재지전체주소']]
pc_cluster = MarkerCluster().add_to(m)

for lat,long,name,popup in zip(latlong['위도(EPSG4326)'],latlong['경도(EPSG4326)'],latlong['시설명'],latlong['소재지전체주소'] ):
    
    if '서울특별시' in popup :
        if '경기도' not in popup :   # 경기도에 있는 서울특별시청소년 교육원을 제외하기 위함 부정확 하니 다른 조건으로 수정 요망
            print(lat,long,name,popup)       

            folium.Marker(
                [lat,long],
                popup=popup,
                tooltip=name,
                icon=folium.Icon(color='red', prefix='fa', icon="info-sign")
            ).add_to(pc_cluster)






path = './data/policeMap.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('02map.html testing...')
print()