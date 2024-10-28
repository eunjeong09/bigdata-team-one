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
from flask import Flask, render_template
def newsSearch(keyword):
    url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&ssc=tab.news.all&query={keyword}&oquery=&tqi=ixNfxdpzL8VssDsUz28ssssssON-294837"
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html,'html.parser')
    news_tit= soup.select(".news_tit")
    news_con = soup.select(".api_txt_lines")
    # news_info = soup.find_all('span', {'class':'info'})
    news_img = soup.select(".thumb")
    news_date = soup.find_all('span', {'class':'info'})
    # print(soup)
    # print('- '*50)
    # print(news_tit)
    # print(news_con)
    print('- '*50)
    cnt_img = 1 # img의 thumb가 여러가지 있어서 1,3, ... 홀수가 기사 사진 - 0,2,4, ... 출처의 마크
    cnt_plus = 0
    resultList = []
    for k in range(8):
        title = news_tit[k].text
        con = news_con[k].text
        img = news_img[cnt_img].attrs['data-lazysrc']
        url = news_tit[k].attrs['href']
        if '전' in news_date[k+cnt_plus].text :
            date = news_date[k+cnt_plus].text
        else:
            cnt_plus = cnt_plus + 1
            date = news_date[k+cnt_plus].text
        print('cnt :', k+1)
        print('제목 :', title)
        # print('내용 :', con)
        print('url :', url)
        print('img :', img)
        print('date :', date)
        print('- '*50)
        resultList.append([title]+[url]+[img]+[date])
        cnt_img = cnt_img+2
    newsSearchDf = pd.DataFrame(resultList)
    return newsSearchDf
app = Flask(__name__)
@app.route("/")
def home():
    # my_variable = "Hello, World!"
    my_variable = newsSearch('민방위')
    return render_template('index.html', my_variable=my_variable)
    # return render_template('news.html', my_variable=my_variable)
if __name__ == '__main__':
    app.run(debug=True)