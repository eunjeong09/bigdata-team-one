import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time
import requests
import pandas as pd
# Import numpy
import numpy as np  

url = "http://openapi.seoul.go.kr:8088/71714f72486e6f3037386a676f4a67/json/VTsClnswspfGnrl/1/100/"
#1000개 이상을 불러올 경우 'Empty DataFrame'
req = requests.get(url)
req.raise_for_status()
# print(req) 실행 시 200
json_df =req.json()
time.sleep(1)
def get_lat_lon(EMER_FACIL_LOC):
    geolocator = Nominatim(user_agent="my_agent")
    try:
        location = geolocator.geocode(EMER_FACIL_LOC)
        if location: 
            latitude = location.latitude
            longitude = location.longitude
            return latitude, longitude
        else:
            return np.nan, np.nan
    except (GeocoderTimedOut, GeocoderServiceError):
        print("Error: 지오코딩 서비스에 문제가 발생했습니다. 다시 시도해주세요.")
        return None, None
data = json_df['VTsClnswspfGnrl']['row']
issues = pd.DataFrame(data,columns=["CGG_NM","FACIL_SE","EMER_FACIL_LOC","RWT_QUA","GEN_KND","SRV_DIV"])
# df = pd.DataFrame(json_df['VTsClnswspfGnrl']['row'],index=range(1,len(json_df['VTsClnswspfGnrl']['row'])+1))
issues['EMER_FACIL_LOC'].map(get_lat_lon)
issues[['latitude', 'longitude']] = issues['EMER_FACIL_LOC'].apply(lambda x: pd.Series(get_lat_lon(x)))
issues.dropna(subset=['latitude', 'longitude'], inplace=True)
