#공공데이터 json 포멧에서 주소값을 받아 위도 경도 열 추가 후 CSV파일로 저장

import json
import csv

import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
def get_lat_lon(EMER_FACIL_LOC):
    geolocator = Nominatim(user_agent="my_agent")
    try:
        location = geolocator.geocode(EMER_FACIL_LOC)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except (GeocoderTimedOut, GeocoderServiceError):
        print("Error: 지오코딩 서비스에 문제가 발생했습니다. 다시 시도해주세요.")
        return None, None
def read_addresses_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:  # 'utf-8'로 인코딩 지정
        data = json.load(f)
    return data
def process_addresses_and_save_to_csv(json_data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:  # 'utf-8'로 인코딩 지정
        writer = csv.writer(csvfile)
        writer.writerow(["주소", "위도", "경도"])  # 헤더 추가
        for item in json_data['DATA']:
            # Access the address using the 'EMER_FACIL_LOC' key within each item
            EMER_FACIL_LOC = item['emer_facil_loc']
            lat, lon = get_lat_lon(EMER_FACIL_LOC)
            writer.writerow([EMER_FACIL_LOC, lat, lon])

# JSON 파일 경로 및 출력 CSV 파일 경로 지정
json_file_path = "./서울시 자치구별 민방위 비상급수시설 현황 자료.json"  # JSON 파일 경로
output_csv_path = "output.csv"  # 출력 CSV 파일 경로

# JSON 파일에서 주소 읽기
addresses_data = read_addresses_from_json(json_file_path)

# 주소 처리 및 CSV 파일 저장
process_addresses_and_save_to_csv(addresses_data, output_csv_path)

print(f"{output_csv_path} 파일이 생성되었습니다.")