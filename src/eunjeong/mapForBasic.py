# 석민님의 Project01_20241017.py 파일을 참고해서 작성

# 요구사항
# 현재 위치를 표시하지만 folium의 icon을 이용한다
# csv파일의 도로명 주소를 지도에 표시하고, 군집화로 출력한다.
# 차별 주제 : ?

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

pc_cluster = MarkerCluster().add_to(m)

for k in range(len(df)):
    if df.iloc[k,4] == '사용중':
        if isinstance(df['도로명전체주소'][k], str) and df['도로명전체주소'][k][0:2] == '서울':
            cnt_seoul = cnt_seoul +1
            folium.Marker(
                location= (df['위도(EPSG4326)'][k], df['경도(EPSG4326)'][k]),
                tooltip=df['시설명'],
            ).add_to(pc_cluster)

m_path = './src/eunjeong/map_for_basic.html'
m.save(m_path)
webbrowser.open(os.path.realpath(m_path))
