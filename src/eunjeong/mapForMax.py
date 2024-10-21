# 석민님의 Project01_20241017.py 파일을 참고해서 작성

# 요구사항
# 현재 위치를 표시하지만 folium의 icon을 이용한다
# csv파일의 도로명 주소를 지도에 표시하고, 군집화로 출력한다.

# 차별 주제 : 
# 최대 수용인원이 많은 순으로 차트를 표현할까?
# 1. 차트 : 10000명 이상의 수용인원을 count로 바 차트
# 2. 지도에서 count를 기준으로 다른 색을 지도에 표시(circle)

import folium
import os
import webbrowser
import pandas as pd

from folium.plugins import MarkerCluster

path = './src/eunjeong/shelter_location.csv'
df = pd.read_csv(path, encoding='utf-8')


# print(df.info())
# df.info()로 출력할 수 있는 내용 > column Non-Null Count Dtype

# 나의 위치 현재 우리집 위도 경도
homeLa = 37.5353617
homeLo = 126.9523534
m = folium.Map(location=[homeLa, homeLo], zoom_start=11)

cnt_seoul = 0

folium.Marker(
    location = (homeLa, homeLo),
    tooltip = '우리집',
    popup = folium.Popup('우리집 : 서울 용산구 효창원로 13길 7', min_width = 50, max_width=200),
    icon = folium.Icon(icon='home', color = 'blue'),
).add_to(m)


# 최대 수용인원이 5000명 이상인 사용중인 대표소는 초록색 원으로, 10000명 미만인 사용중인 대표소는 주황색으로
for k in range(len(df)):
    if df['운영상태'][k] == '사용중' and isinstance(df['도로명전체주소'][k], str) and df['도로명전체주소'][k][0:2] == '서울':
        if int(df['최대수용인원'][k]) > 10000:
            folium.Circle(
                location= (df['위도(EPSG4326)'][k], df['경도(EPSG4326)'][k]),
                tooltip=df['시설명'][k],
                radius=50,
                color='green'
            ).add_to(m)
        else:
            folium.Circle(
                location= (df['위도(EPSG4326)'][k], df['경도(EPSG4326)'][k]),
                tooltip=df['시설명'][k],
                radius=50,
                color='orange'
            ).add_to(m)
    
        


m_path = './src/eunjeong/map_for_max.html'
m.save(m_path)
webbrowser.open(os.path.realpath(m_path))
