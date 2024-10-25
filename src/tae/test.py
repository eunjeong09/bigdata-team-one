import pandas as pd
import matplotlib.pyplot as plt

# 파일 경로와 인코딩 설정
csv_file_path = '/Users/tae/Documents/GitHub/bigdata-team-one/src/tae/data/shelterInfo.csv'

# CSV 파일 읽기
df = pd.read_csv(csv_file_path, encoding='euc-kr')

# 열 이름의 공백 제거
df.columns = df.columns.str.strip()

# DataFrame 열 이름 확인
print(df.columns)

# 수평 막대 그래프 그리기
plt.barh(df['자치구'], df['사용중인 대피소'], color='lightblue')
plt.xlabel('사용중인 대피소 수')
plt.ylabel('자치구')
plt.title('자치구별 사용중인 대피소 수량')
plt.show()
