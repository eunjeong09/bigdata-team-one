# 수원지(필터사용 음용수/생활용수) 2019등록 히트맵, 민방위대피소 동시에 표시
import folium
from folium.plugins import HeatMap 
import os
import webbrowser
import pandas as pd
import numpy as np
from folium.plugins import TagFilterButton

df = pd.read_csv('csvformap.csv', index_col=False)
year_df = df[df['등록년도'].astype(str).str.contains("2019", na=False)]
print()

shelter_df = pd.read_csv('shelter_data.csv')  
ydp_shelters = shelter_df[shelter_df['도로명전체주소'].str.contains("영등포구", na=False)]

if year_df['지번주소'].notna().any():
    long = year_df['longitude'].mean()
    lat = year_df['latitude'].mean()
    m = folium.Map(location=(lat, long), zoom_start=14, tiles='cartodbpositron')
    heatmap_data = year_df[['latitude', 'longitude', '양수량(톤/일)']].dropna().values.tolist()
    HeatMap(heatmap_data).add_to(m)
   
    for i, row in year_df.iterrows(): 
        latlng = (row['latitude'], row['longitude'])  
        category = row['용도구분']  

        if category in ['생활용수', '음용수'] and not pd.isnull(latlng[0]) and not pd.isnull(latlng[1]):
            if category == '생활용수':
                color = 'blue'  # Blue for 생활용수
            else:
                color = 'red'  # Red for 음용수

            folium.Marker(
                tuple(latlng),
                tags=[category],  
                icon=folium.Icon(color=color)  
            ).add_to(m)

    TagFilterButton(
        ['생활용수', '음용수'],  
        icon='fa-filter',
        clear_text='모두 보기'  
    ).add_to(m)

    for i, row in ydp_shelters.iterrows():
        folium.Marker(
            location=[row['위도(EPSG4326)'], row['경도(EPSG4326)']],
            popup=row['최대수용인원'],  
            icon=folium.Icon(color='green', icon='home') 
        ).add_to(m)

os.makedirs('.data', exist_ok=True)
path = '.final_map.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print()
print('done')