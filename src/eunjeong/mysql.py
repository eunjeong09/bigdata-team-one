# mysql데이터베이스 
import pymysql
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
       
config={
  'host' : '127.0.0.1' ,  
  'user' : 'root',
  'password' : '1234',
  'database' : 'sys' ,
  'port' : 3306
}

CN = pymysql.connect(**config)
cursor = CN.cursor()

def preventSelectAll():
    msg = "select * from prevent"
    cursor.execute(msg)
    rows = cursor.fetchall()

    print()
    for r in rows:
        print(r[0], r[1])

def preventInsert():
    # 크롤링한 데이터 출력 및 데이터베이스에 삽입
    for title, content in zip(titles, contents):
        
        # SQL 파라미터 바인딩을 통해 안전하게 데이터 삽입
        msg = "INSERT INTO prevent (title, content) VALUES (%s, %s)"
        cursor.execute(msg, (title.text, content.text))
    
    # 루프 후 한 번에 커밋
    CN.commit()

# WebDriver 실행
driver = webdriver.Chrome() 

# 국민재난안전포털의 비상대비 행동요령 페이지로 이동
url = 'https://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/contents/prevent/SDIJKM5107.html?menuSeq=785'
driver.get(url)

# 페이지 로딩 대기 (필요에 따라 적절한 시간으로 설정)
time.sleep(5)

# 크롤링할 요소 찾기 (제목과 내용)
titles = driver.find_elements(By.CLASS_NAME, 'level4_title')  
contents = driver.find_elements(By.CLASS_NAME, 'contextIndent_oneDepList')

# 크롤링 결과 DB저장
# preventSelectAll()
preventInsert()
