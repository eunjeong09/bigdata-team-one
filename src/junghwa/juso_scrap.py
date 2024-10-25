from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time
import csv

'''
https://www.juso.go.kr/openIndexPage.do
검색 위치 테그
<div class="box_search">
    <input type="text" name="searchKeyword" id="inputSearchAddr" class="input_country ui-autocomplete-input"
     title="검색어 입력-도로명, 건물명, 지번, 초성검색" maxlength="80" onkeypress="enterSearch(event);" 
     style="ime-mode:active;" placeholder="도로명, 건물명, 지번, 초성검색">
</div>

검색 후 결과 테그
<div class="subejct_2">
    <span class="roadNameText">
        서울특별시 양천구 신월동  591-1
            신안약수아파트
    </span>
</div>
'''
driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.ID, 'keyword').send_keys('국회대로 608(당산동)' + Keys.ENTER)
mydata = driver.page_source
soup = BeautifulSoup(mydata, 'html.parser')
print(soup)
time.sleep(15)

#[CODE 1]
def Juso_DtoZ(result):
    Juso_URL = "https://www.juso.go.kr/openIndexPage.do"
    wd = webdriver.Chrome() #교재 코드 수정
             
    for i in range(1, 10):  #마지막 매장번호(최근 신규 매장번호) 까지 반복
        wd.get(https://www.juso.go.kr/openIndexPage.do)
        time.sleep(1)  #웹페이지 연결할 동안 1초 대기
        try:
            wd.get(Juso_URL)
            wd.find_element(By.ID, 'keyword').send_keys('국회대로 608(당산동)' + Keys.ENTER)
            mydata = wd.page_source
            soup = BeautifulSoup(mydata, 'html.parser')
            print(soup)
            time.sleep(1.5)
            
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            print(store_name)  #매장 이름 출력하기
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string
            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue 
    return

#[CODE 0]
def main():
    result = []
    print('주소 crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    Juso_DtoZ(result)  #[CODE 1]
    
    CB_tbl = pd.DataFrame(result, columns=('주소'))
    os.makedirs('./junghwa', exist_ok=True)  
    CB_tbl.to_csv('./결측주소.csv', encoding='utf-8', mode='w', index=True)

if __name__ == '__main__':
     main()
