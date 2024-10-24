import time
import requests
import pandas as pd
# Import numpy
import numpy as np  
import json
import folium
from folium.plugins import MarkerCluster
import os
import webbrowser
df=pd.read_csv("./output.csv",index_col=False)
region_df = df[df['주소'].str.contains("영등포", na=False)]
print()

if region_df['주소'].notna().any():
    long = region_df['경도'].mean()
    lat = region_df['위도'].mean()
    m = folium.Map(location=(lat,long), zoom_start=11, tiles='cartodbpositron')
    pc_cluster = MarkerCluster().add_to(m)
    for index in region_df.index:
        # Check if latitude and longitude values are valid (not NaN)
        if pd.notna(region_df.loc[index, '위도']) and pd.notna(region_df.loc[index, '경도']):
            location = (float(region_df.loc[index,'위도']), float(region_df.loc[index,'경도']))
            name = str(region_df.loc[index,'주소'])
            popup = folium.Popup(name + '\n' + str(region_df.iloc[0]) , min_width=50, max_width=200)
            # Pass the entire row to color_select()
            folium.Marker(
                location,
                popup=popup,
                tooltip=name,
                icon=folium.Icon(icon='building',color = 'red', prefix='fa') 
            ).add_to(pc_cluster)
        else:
            print(f"Warning: Skipping row {index} due to missing location data.")
# makedirs() 를 이용한 폴더오류 해결
os.makedirs('./src/junghwa', exist_ok=True)  
path = './src/junghwa/water_yd.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('water_yd.html testing...')
print()
print('done')
print()

