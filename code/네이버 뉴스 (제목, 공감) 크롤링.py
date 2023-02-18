# -*- coding: utf-8 -*-
"""네이버 뉴스 (제목, 공감) 크롤링.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qYdYHBCORaTbP_HEC4aUqGpFPrkC55NC
"""

pwd

import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver import ActionChains as AC  # 웹 브라우저 동작
from tqdm import tqdm
from tqdm.notebook import tqdm
import re
from time import sleep
import time
from urllib.parse import quote

def get_news(query, page_num=10):
    
    url_list1 = []
    
    url_query = quote(query)
    
    driver = webdriver.Chrome(r"C:/Users/Park JuYoung/Desktop/chromedriver.exe")
    driver.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + url_query)
    time.sleep(2)
    
    for _ in range(0, page_num):
        driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div/a[2]').click()
        time.sleep(2)
        things = driver.find_elements_by_link_text('네이버뉴스')
        for thing in things:
            url = thing.get_attribute('href')
            url_list1.append(url)
            

    return url_list1

keyword = input('검색 키워드를 입력하세요 : ')
url_list13 = get_news(keyword, 399)
print('Done')

print(len(url_list13))
url_list13

# url_list 저장
df = pd.DataFrame({"url":url_list13})
df.to_csv('naver_news_urls13.csv')

# 저장해둔 url 불러오기
df = pd.read_csv('naver_news_urls13.csv')
print(len(df['url']))
df['url']

number = len(df['url'])
number

dict = {}

# 페이지당 기사 수집
for i in tqdm(range(0, number)):   # len(df['url'])
    try:
        # 뉴스 크롬창 띄우기
        driver = webdriver.Chrome(r"C:/Users/Park JuYoung/Desktop/chromedriver.exe")
        driver.get(df['url'][i])
        time.sleep(1)

        # 기사 데이터 수집
        title = driver.find_element_by_css_selector('.tts_head').text
        like = driver.find_element_by_css_selector(".end_btn .u_likeit_list.good .u_likeit_list_count._count").text
        warm = driver.find_element_by_css_selector(".end_btn .u_likeit_list.warm .u_likeit_list_count._count").text
        sad = driver.find_element_by_css_selector(".end_btn .u_likeit_list.sad .u_likeit_list_count._count").text
        angry = driver.find_element_by_css_selector(".end_btn .u_likeit_list.angry .u_likeit_list_count._count").text
        want = driver.find_element_by_css_selector(".end_btn .u_likeit_list.want .u_likeit_list_count._count").text


        # review 수집하기
        review_list = []
        overlays1 = ".u_cbox_text_wrap"
        reviews = driver.find_elements_by_css_selector(overlays1)
        for review in tqdm(reviews):    
            review = review.text
            review_list.append(review)

        target_info = {}
        target_info['기사명'] = title
        target_info['좋아요'] = like
        target_info['훈훈해요'] = warm
        target_info['슬퍼요'] = sad
        target_info['화나요'] = angry
        target_info['후속기사 원해요'] = want

        dict[i] = target_info
        

        driver.close()
        time.sleep(1)
        
    except:
        driver.close()
        continue

print(len(dict))
dict

# 판다스화
import pandas as pd
result_df = pd.DataFrame.from_dict(dict, 'index')
result_df

result_df.to_csv("청원.csv")

result = pd.read_csv('C:/Users/Park JuYoung/Desktop/KUBIG/NLP/청원.csv')

result

result = pd.read_csv('C:/Users/Park JuYoung/Desktop/KUBIG/NLP/징역.csv', encoding = 'euc-kr')

result

