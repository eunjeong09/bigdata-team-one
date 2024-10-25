# 석민님의 Project01_20241017.py 파일을 참고해서 작성

# 요구사항
# 현재 위치를 표시하지만 folium의 icon을 이용한다
# csv파일의 도로명 주소를 지도에 표시하고, 군집화로 출력한다.

# 차별 주제 : 
# 최대 수용인원이 많은 순으로 차트를 표현할까?
# 1. 차트 : 10000명 이상의 수용인원을 count로 바 차트
# 2. 지도에서 count를 기준으로 다른 색을 지도에 표시(circle) -> mapForMax
# 3. 지도에서 행정 구역에 따라 다르게 색칠(count) -> mapForLocation

import json
import folium
import os
import webbrowser
import pandas as pd

from folium.plugins import MarkerCluster
import requests

path = './src/eunjeong/shelter_location.csv'
df = pd.read_csv(path, encoding='utf-8')

# 나의 위치 현재 우리집 위도 경도
homeLa = 37.5353617
homeLo = 126.9523534
m = folium.Map(location=[homeLa, homeLo], zoom_start=11)

cnt_seoul = 0

# folium.Marker(
#     location = (homeLa, homeLo),
#     tooltip = '우리집',
#     popup = folium.Popup('우리집 : 서울 용산구 효창원로 13길 7', min_width = 50, max_width=200),
#     icon = folium.Icon(icon='home', color = 'blue'),
# ).add_to(m)

r = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')   
c = r.content
seoul_geo = json.loads(c)
 
seoul_districts = [
    {"name": "강남구", "count": 0},
    {"name": "강동구", "count": 0},
    {"name": "강북구", "count": 0},
    {"name": "강서구", "count": 0},
    {"name": "관악구", "count": 0},
    {"name": "광진구", "count": 0},
    {"name": "구로구", "count": 0},
    {"name": "금천구", "count": 0},
    {"name": "노원구", "count": 0},
    {"name": "도봉구", "count": 0},
    {"name": "동대문구", "count": 0},
    {"name": "동작구", "count": 0},
    {"name": "마포구", "count": 0},
    {"name": "서대문구", "count": 0},
    {"name": "서초구", "count": 0},
    {"name": "성동구", "count": 0},
    {"name": "성북구", "count": 0},
    {"name": "송파구", "count": 0},
    {"name": "양천구", "count": 0},
    {"name": "영등포구", "count": 0},
    {"name": "용산구", "count": 0},
    {"name": "은평구", "count": 0},
    {"name": "종로구", "count": 0},
    {"name": "중구", "count": 0},
    {"name": "중랑구", "count": 0}
]

def increase_count(gu_name):
    # seoul_districts 리스트에서 해당 구를 찾아서 count를 1 증가시킴
    for district in seoul_districts:
        if district["name"] == gu_name:
            district["count"] += 1
            return


for k in range(len(df)):
    if df['운영상태'][k] == '사용중' and isinstance(df['도로명전체주소'][k], str) and df['도로명전체주소'][k][0:2] == '서울':
        increase_count(df['도로명전체주소'][k].split()[1])


def get_color(count):
    if count <= 28:
        return '#cce5ff'  # 연한 파란색
    elif count <= 57:
        return '#99ccff'  # 밝은 파란색
    elif count <= 85:
        return '#66b2ff'  # 중간 파란색
    elif count <= 113:
        return '#3399ff'  # 진한 파란색
    elif count <= 141:
        return '#0073e6'  # 짙은 파란색
    else:
        return '#004080'  # 매우 짙은 파란색

def get_count(gu_name):
    for district in seoul_districts:
        if district["name"] == gu_name:
            return district["count"]


# GeoJSON 파일에서 구 이름별로 색칠하기
for feature in seoul_geo['features']:
    gu_name = feature['properties']['name']  # GeoJSON 파일에서 구 이름을 가져옴
    gu_count = get_count(gu_name)
    gu_color = get_color(gu_count)  # 해당 구의 색상을 결정
    
    # Folium GeoJson 레이어에 구별로 색상을 지정하여 추가
    folium.GeoJson(
        feature, 
        style_function=lambda x, color=gu_color: {
            'fillColor': color, 'color': 'black', 'weight': 1.5, 'fillOpacity': 0.7
        },
        tooltip=gu_name  # 마우스오버시 구 이름이 뜨도록 설정
    ).add_to(m)

m_path = './src/eunjeong/map_for_location.html'
m.save(m_path)
webbrowser.open(os.path.realpath(m_path))
