from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

df = pd.read_csv('output.csv', encoding='cp949')  

options = webdriver.ChromeOptions()
options.add_argument('--headless')  
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

results = []  

for address in df['시설주소']:
    try:
        driver.get('https://www.juso.go.kr/support/AddressMainSearch.do')
        search_box = driver.find_element(By.ID, 'keyword')
        search_box.send_keys(address + Keys.ENTER)
        time.sleep(0.5) # 모든 요소가 다 로딩되는걸 기다리면 시간이 증가 
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        road_name_element = soup.select_one('#list1 > div.subejct_2 > span.roadNameText')
        if road_name_element:
          converted_address = road_name_element.text.strip()
          results.append([address, converted_address])
        else:
            results.append([address, ''])  

    except Exception as e:
        print(f"Error processing address '{address}': {e}")
        results.append([address, 'Error'])  

results_df = pd.DataFrame(results, columns=['시설주소', '지번주소'])
results_df.to_csv('converted_addresses.csv', encoding='utf-8', index=False)
converted_addresses_df = pd.read_csv('converted_addresses.csv', encoding='utf-8')

print('done')
driver.quit()
