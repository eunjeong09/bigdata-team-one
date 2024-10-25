# 자치구별 사용중인 대피소 수량을 가로막대로 시각화

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# 폰트
font_path = './src/Fonts/Arial Unicode.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# CSV 파일 읽기
csv_file_path = './src/data/shelterInfo.csv'
df = pd.read_csv(csv_file_path, encoding='euc-kr')

# 그래프 크기 설정
plt.figure(figsize=(10, 6))

# 수평 막대그래프 그리기 (barh() 사용)
plt.barh(df['자치구'], df['사용중인 대피소'], color='lightblue')

# 제목과 축 라벨 추가
plt.title('자치구별 사용 중인 대피소 수량', fontsize=16)
plt.xlabel('사용중인 대피소', fontsize=12)
plt.ylabel('자치구', fontsize=12)

# 수량 값을 막대 위에 표시 (옵션)
for index, value in enumerate(df['사용중인 대피소']):
    plt.text(value, index, str(value), va='center')

# 그래프 출력
plt.tight_layout()  # 레이아웃 자동 조정
plt.show()