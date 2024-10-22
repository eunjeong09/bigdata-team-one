import matplotlib.pyplot as plt    #맷플롯립의 pyplot 모듈
 
# 우리나라의 연간 1인당 국민소득을 각각 years, gdp에 저장 
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]
 
#선 그래프를 그린다. x축에는 years값, y축에는 gdp값을 표시한다.
plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')
 
#제목을 설정한다.
plt.title('GDP per capita') #1인당 국민소득
 
#y축에 레이블을 붙인다.
plt.ylabel('dollars')
plt.savefig('gdp_per_capita.png', dpi = 600)
plt.show()

 
#1인당 국민소득
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]
 
plt.bar(range(len(years)), gdp)      #막대그래프 호출: bar(x, y) 
 
plt.title("GDP per capita")          #차트 제목
plt.ylabel('dollars')                #y축 라벨 
 
plt.xticks(range(len(years)), years) #x축에 틱을 붙임. 
plt.show()