# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # By 모듈 임포트
# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬드라이버 실행
driver = webdriver.Chrome() 

#크롬 드라이버에 url 주소 넣고 실행

# 네이버 뉴스 페이지 열기
driver.get('https://news.naver.com/')

# 검색창 찾기
search_icon = driver.find_element(By.CLASS_NAME, 'Ntool_button')
search_icon.click()

# 검색창 찾기 (클래스명 이용)
wait = WebDriverWait(driver, 20)  # 시간을 20초로 늘려볼 수 있습니다.
search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="뉴스 검색"]')))

# 검색어 입력
search_box.send_keys('민방위대피소')

# 검색 버튼 클릭
search_box.send_keys(Keys.RETURN)  # 검색어 입력 후 엔터키로 검색

# 검색 결과 페이지 로드 기다리기
time.sleep(2)  # 페이지가 로드될 때까지 기다림

#test
test_element = wait.until(EC.presence_of_all_elements_located(By.CLASS_NAME, 'news_contents'))
print(test_element)

# 'news_contents' 클래스를 가진 요소가 나타날 때까지 기다림
# news_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'news_wrap')))

# # 최대 3개의 뉴스 요소만 출력
# for news in news_elements:  # 리스트 슬라이싱을 사용하여 최대 3개만 가져옴
#     title_element = news.find_element(By.CLASS_NAME, 'news_tit')
#     # description_element = news.find_element(By.CLASS_NAME, 'news_dsc')
    
#     # 뉴스 제목과 설명 가져오기
#     title = title_element.text
#     # description = description_element.text if description_element else "No description available"
    
#     print(f"Title: {title}")
#     # print(f"Description: {description}")
#     print("-" * 80)

# 브라우저 종료
driver.quit()