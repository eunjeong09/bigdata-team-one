import matplotlib.pyplot as plt    #맷플롯립의 pyplot 모듈
import matplotlib.font_manager as fm
import pandas as pd

# 폰트
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

path = './src/eunjeong/shelter_location.csv'
df = pd.read_csv(path, encoding='utf-8')

seoul_districts = [
    {"name": "강남구", "count": 0},
    {"name": "강동구", "count": 0},
    {"name": "강북구", "count": 0},
    {"name": "강서구", "count": 0},
    {"name": "관악구", "count": 0},
    {"name": "광진구", "count": 0},
    {"name": "구로구", "count": 0},
    {"name": "금천구", "count": 0},
    {"name": "노원구", "count": 0},
    {"name": "도봉구", "count": 0},
    {"name": "동대문구", "count": 0},
    {"name": "동작구", "count": 0},
    {"name": "마포구", "count": 0},
    {"name": "서대문구", "count": 0},
    {"name": "서초구", "count": 0},
    {"name": "성동구", "count": 0},
    {"name": "성북구", "count": 0},
    {"name": "송파구", "count": 0},
    {"name": "양천구", "count": 0},
    {"name": "영등포구", "count": 0},
    {"name": "용산구", "count": 0},
    {"name": "은평구", "count": 0},
    {"name": "종로구", "count": 0},
    {"name": "중구", "count": 0},
    {"name": "중랑구", "count": 0}
]

def increase_count(gu_name):
    for district in seoul_districts:
        if district["name"] == gu_name:
            district["count"] += 1
            return


for k in range(len(df)):
    if df['운영상태'][k] == '사용중' and isinstance(df['도로명전체주소'][k], str) and df['도로명전체주소'][k][0:2] == '서울':
        increase_count(df['도로명전체주소'][k].split()[1])

# print(seoul_districts)

nameArr = []
countArr = []
for district in seoul_districts:
    nameArr.append(district["name"])
    countArr.append(district["count"])

plt.bar(range(len(nameArr)), countArr)      #막대그래프 호출: bar(x, y) 
 
plt.title("지역별 대피소 수")          #차트 제목
plt.ylabel('개수')                #y축 라벨 
 
plt.xticks(range(len(nameArr)), nameArr) #x축에 틱을 붙임. 
plt.show()