# 대피소 지도위에 표시
import folium
import os
import webbrowser
import requests
import json
import pandas as pd
import numpy as np

df_sh = pd.read_csv('./src/junghwa/shelter_location.csv',index_col=False)
print(df_sh)
print()
print(df_sh.info())
print()
long = df_sh['경도(EPSG4326)'].mean()
lat = df_sh['위도(EPSG4326)'].mean()
m = folium.Map(location=(lat,long), zoom_start=11, tiles="cartodb positron")
for k in range(len(df_sh)):
    # Check if latitude and longitude values are valid (not NaN)
    if pd.notna(df_sh.loc[k, '위도(EPSG4326)']) and pd.notna(df_sh.loc[k, '경도(EPSG4326)']):
        location = (float(df_sh.loc[k,'위도(EPSG4326)']), float(df_sh.loc[k,'경도(EPSG4326)']))
        name = str(df_sh.loc[k,'시설명'])
        popup = folium.Popup(name + '\n' + str(df_sh.loc[k,'시설면적(㎡)']) , min_width=50, max_width=200)
        folium.Marker(
            location,
            popup=popup,
            tooltip=name,
            icon=folium.Icon(icon='building',color='lightblue',prefix='fa')
        ).add_to(m)
    else:
        # Handle rows with missing location data (e.g., print a warning or skip them)
        print(f"Warning: Skipping row {k} due to missing location data.")
folium.LayerControl().add_to(m)
# makedirs() 를 이용한 폴더오류 해결
os.makedirs('./src/junghwa', exist_ok=True)  
path = './src/junghwa/shelter.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('shelter.html testing...')
print()
print('done')
