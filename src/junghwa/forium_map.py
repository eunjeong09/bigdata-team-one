# 대피소 지도위에 표시
import folium
from folium.plugins import MarkerCluster
import os
import webbrowser
import requests
import json
import pandas as pd
import numpy as np

df_sh = pd.read_csv('shelter_location.csv',index_col=False)
region_df = df_sh[df_sh['도로명전체주소'].str.contains("영등포구", na=False)]
print()

if region_df['도로명전체주소'].notna().any():
    long = region_df['경도(EPSG4326)'].mean()
    lat = region_df['위도(EPSG4326)'].mean()
    m = folium.Map(location=(lat,long), zoom_start=11, tiles='cartodbpositron')
    for index in region_df.index:
    # Check if latitude and longitude values are valid (not NaN)
        if pd.notna(region_df.loc[index, '위도(EPSG4326)']) and pd.notna(region_df.loc[index, '경도(EPSG4326)']):
            location = (float(region_df.loc[index,'위도(EPSG4326)']), float(region_df.loc[index,'경도(EPSG4326)']))
            name = str(region_df.loc[index,'시설명'])
            popup = folium.Popup(name + '\n' + str(region_df.loc[index,'시설면적(㎡)']) , min_width=50, max_width=200)
            
            # folium.CircleMarker(
            #     location,
            #     popup=popup,
            #     radius= 400,
            #     color='red',
            #     fill_color='#EC4074').add_to(m)   
            folium.Marker(
                location,
                popup=popup,
                tooltip=name,
                icon=folium.Icon(icon='building',color = 'lightgreen' ,prefix='fa') 
            ).add_to(m)

    else:
        print(f"Warning: Skipping row {index} due to missing location data.")

os.makedirs('.junghwa', exist_ok=True)  
path = '.shelter_new.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('shelter_new.html testing...')
print()
print('done')