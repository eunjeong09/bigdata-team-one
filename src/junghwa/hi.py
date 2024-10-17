# 대피소 지도위에 표시
import folium
from folium.plugins import MarkerCluster
import os
import webbrowser
import requests
import json
import pandas as pd
import numpy as np

df_sh = pd.read_csv('./src/junghwa/shelter_location.csv',index_col=False)
region_df = df_sh[df_sh['도로명전체주소'].str.contains("영등포구", na=False)]
print()

def color_select(row):  # Changed function input to 'row'
    # Access the '최대수용인원' column value from the current row
    allow = row['최대수용인원'] 
    # Handle potential errors if 'allow' is not a string or doesn't contain '-'
    try:
        po_d = int(allow.split('-')[0]) 
    except (AttributeError, IndexError):  
        po_d = 0  # or any default value you prefer
    if po_d > 200:
        return 'darkviolet'
    else:
        return 'dodgerblue'

if region_df['도로명전체주소'].notna().any():
    long = region_df['경도(EPSG4326)'].mean()
    lat = region_df['위도(EPSG4326)'].mean()
    m = folium.Map(location=(lat,long), zoom_start=11, tiles='cartodbpositron')
    pc_cluster = MarkerCluster().add_to(m)
    for index in region_df.index:
        # Check if latitude and longitude values are valid (not NaN)
        if pd.notna(region_df.loc[index, '위도(EPSG4326)']) and pd.notna(region_df.loc[index, '경도(EPSG4326)']):
            location = (float(region_df.loc[index,'위도(EPSG4326)']), float(region_df.loc[index,'경도(EPSG4326)']))
            name = str(region_df.loc[index,'시설명'])
            popup = folium.Popup(name + '\n' + str(region_df.loc[index,'시설면적(㎡)']) , min_width=50, max_width=200)
            # Pass the entire row to color_select()
            folium.Marker(
                location,
                popup=popup,
                tooltip=name,
                icon=folium.Icon(icon='building',color = color_select(region_df.loc[index]),prefix='fa') 
            ).add_to(pc_cluster)
        else:
            print(f"Warning: Skipping row {index} due to missing location data.")
# makedirs() 를 이용한 폴더오류 해결
os.makedirs('./src/junghwa', exist_ok=True)  
path = './src/junghwa/shelter_yd.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('shelter_yd.html testing...')
print()
print('done')