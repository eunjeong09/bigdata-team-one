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

# 자치구별 대피소 데이터를 이용한 강북, 강남, 기타 그룹화
# 강북, 강남, 기타로 나눌 자치구 리스트 정의
gangbuk_districts = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', 
                     '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구']
gangnam_districts = ['서초구', '송파구', '강남구']
# 기타는 위에 포함되지 않은 나머지 자치구로 자동으로 계산되게 설정

# 강북, 강남, 기타로 나누어 대피소 개수 합산
gangbuk_count = df[df['자치구'].isin(gangbuk_districts)]['사용중인 대피소'].sum()
gangnam_count = df[df['자치구'].isin(gangnam_districts)]['사용중인 대피소'].sum()
other_count = df[~df['자치구'].isin(gangbuk_districts + gangnam_districts)]['사용중인 대피소'].sum()

# 파이차트 데이터 준비
labels = ['강북', '강남', '기타']
sizes = [gangbuk_count, gangnam_count, other_count]
colors = ['skyblue', 'lightcoral', 'lightgrey']

# 파이차트 그리기
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.title('강북, 강남, 기타 지역 대피소 개수')
plt.show()