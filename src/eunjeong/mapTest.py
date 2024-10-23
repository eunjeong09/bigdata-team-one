import folium
import os

# 위도
latitude = 37.394946
# 경도
longitude = 127.111104
m = folium.Map(location=[latitude, longitude], zoom_start=17, width=750, height=500)
m
folium.Marker(
    [latitude, longitude],
    popup="판교역",
    tooltip="판교역 입구",
    icon=folium.Icon("red", icon="star"),
).add_to(m)
m

# 현재 파일 위치를 기준으로 상대 경로 설정
current_file_path = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_file_path, "map.html")

# 지도 저장
m.save(relative_path)
