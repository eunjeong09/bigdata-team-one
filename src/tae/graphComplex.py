# 자치구별 사용중인 대피소 수량을 가로막대로 시각화

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# 폰트
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# CSV 파일 읽기
csv_file_path = './src/tae/data/shelterInfo.csv'
df = pd.read_csv(csv_file_path, encoding='euc-kr')

# 자치구와 관련된 열 필터링
data = df[['자치구', '사용중인 대피소', '수용가능인원']]

# 피벗 테이블 생성
heatmap_data = data.pivot("자치구", "사용중인 대피소", "수용가능인원")

# 시각화
plt.figure(figsize=(12, 6))

# 히트맵
plt.subplot(1, 2, 1)
sns.heatmap(heatmap_data, annot=True, fmt='g', cmap='coolwarm', cbar_kws={'label': '수용가능인원'})
plt.title('자치구별 사용중인 대피소와 수용가능 인원 히트맵')
plt.xlabel('사용중인 대피소 수')
plt.ylabel('자치구')

# 선 그래프
plt.subplot(1, 2, 2)
plt.plot(data['자치구'], data['수용가능인원'], marker='o', label='수용가능인원', color='orange')
plt.ylabel('수용가능 인원')
plt.title('자치구별 수용가능 인원 변화')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()  # 레이아웃 조정
plt.show()