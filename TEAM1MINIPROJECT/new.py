import time
import json
import pandas as pd
import numpy as np
import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def newsSearch(keyword):
    url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&ssc=tab.news.all&query={keyword}&oquery=&tqi=ixNfxdpzL8VssDsUz28ssssssON-294837"
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html,'html.parser')
    news_tit= soup.select(".news_tit")
    news_con = soup.select(".api_txt_lines")
    # news_info = soup.find_all('span', {'class':'info'})
    news_img = soup.select(".thumb")
    # print(soup)
    # print('- '*50)
    # print(news_tit)
    # print(news_con)
    print('- '*50)
    cnt = 0
    cnt_img = 1 # img의 thumb가 여러가지 있어서 1,3, ... 홀수가 기사 사진 - 0,2,4, ... 출처의 마크
    for k in range(5):
        title = news_tit[k].text
        con = news_con[k].text
        img = news_img[cnt_img].attrs['data-lazysrc']
        url = news_tit[k].attrs['href']
        print('cnt :', k+1)
        print('제목 :', title)
        # print('내용 :', con)
        print('img :', img)
        print('url :', url)
        print('- '*50)
        cnt = cnt+1
        cnt_img = cnt_img+2
newsSearch('민방위')