# 자치구별 사용중인 대피소 수량을 가로막대로 시각화

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 폰트
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# CSV 파일 읽기
csv_file_path = './src/tae/data/shelterInfo.csv'
df = pd.read_csv(csv_file_path, encoding='euc-kr')

# 강북과 강남 자치구 리스트
gangbuk_districts = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', 
                     '중랑구', '성북구', '강북구', '도봉구', '노원구', 
                     '은평구', '서대문구', '마포구']  # 강북 14개 구

gangnam_districts = ['강남구', '서초구', '송파구', '강동구', '양천구', '구로구', 
                     '금천구', '영등포구', '동작구', '관악구', '강서구']  # 강남 11개 구

# 강북과 강남 대피소 개수 합산
gangbuk_count = df[df['자치구'].isin(gangbuk_districts)]['사용중인 대피소'].sum()
gangnam_count = df[df['자치구'].isin(gangnam_districts)]['사용중인 대피소'].sum()
total_count = gangbuk_count + gangnam_count  # 총합 계산

# 파이차트 데이터 준비
labels = [f'강북 (14개구): {gangbuk_count}개', f'강남 (11개구): {gangnam_count}개']
sizes = [gangbuk_count, gangnam_count]
colors = ['skyblue', 'lightcoral']

# 파이차트 그리기
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.title(f'강북 vs 강남 대피소 개수 (총합: {total_count}개)')
plt.show()