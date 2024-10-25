import os
import webbrowser
import requests
import csv
import pandas as pd
import numpy as np

df_sh = pd.read_csv('converted_addresses.csv',index_col=False)
# print(df_sh.loc[:,'지번주소'])
import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

def get_lat_lon(convert_j):
    geolocator = Nominatim(user_agent="my_agent")
    try:
        location = geolocator.geocode(convert_j)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except (GeocoderTimedOut, GeocoderServiceError):
        print("Error: 지오코딩 서비스에 문제가 발생했습니다. 다시 시도해주세요.")
        return None, None
def process_addresses_and_save_to_csv(json_data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:  # 'utf-8'로 인코딩 지정
        writer = csv.writer(csvfile)
        writer.writerow(["주소", "위도", "경도"])  # 헤더 추가
        for item in df_sh['지번주소']:
            # Access the address using the 'EMER_FACIL_LOC' key within each item
            convert_j = item['지번주소']
            lat, lon = get_lat_lon(convert_j)
            writer.writerow([convert_j, lat, lon])