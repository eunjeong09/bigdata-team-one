from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# ChromeDriver 경로 설정
driver_path = '/usr/local/bin/chromedriver'  # 확인한 정확한 경로로 입력

# Chrome 옵션 설정 (필요 시 추가 옵션 설정 가능)
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 창을 띄우지 않음 (옵션)

# ChromeDriver 서비스 설정
service = Service(executable_path=driver_path)

# WebDriver 실행
driver = webdriver.Chrome(service=service, options=chrome_options)

# 국민재난안전포털의 비상대비 행동요령 페이지로 이동
url = 'https://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/contents/prevent/SDIJKM5107.html?menuSeq=785'
driver.get(url)

# 페이지 로딩 대기 (필요에 따라 적절한 시간으로 설정)
time.sleep(5)

# 크롤링할 요소 찾기 (제목과 내용)
titles = driver.find_elements(By.CLASS_NAME, 'level4_title')  
contents = driver.find_elements(By.CLASS_NAME, 'contextIndent_oneDepList')

# 크롤링한 데이터 출력
for title, content in zip(titles, contents):
    print(f"{title.text}")
    print(f"{content.text}")
    print('-' * 50)

# WebDriver 종료
driver.quit()
