from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #웹의 특정 요소가 추가 될때 까지 기다리게 하는 코드 추가
from selenium.common.exceptions import NoSuchElementException #예외처리를 위함
from bs4 import BeautifulSoup

import requests
import pandas as pd
import csv

def get_items(page_index, url):

    new_url = url.replace("pageIndex=1", f"pageIndex={page_index}")  # page_index 위치에 해당하는 페이지의 주소 new_url
    response = requests.get(new_url)   # 각 페이지 마다 파싱(BeautifulSoup)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select("div.content")

    print(new_url)
    

    with open(r"C:\CSV\data.csv", 'a', encoding='UTF-8', newline='') as f:     #csv 파일생성
        csvWriter = csv.writer(f)

        for item in items:
            try:
                name = item.select_one('div.company-name a').get_text(strip=True)  # 딸려오는 개행문자 제거 - 에러수정   23/05/17
            except AttributeError:
                name = 'N/A'

            try:
                form = item.select_one('div.job_condition > span::nth-child(4)').get_text(strip=True)
            except AttributeError:
                form = 'N/A'    

            try:
                carrer = item.select_one('div.job_condition > span::nth-child(2)').get_text(strip=True)
               
            except AttributeError:
                carrer = 'N/A'

            try:
                salary = item.select_one().get_text(strip=True)
               
            except AttributeError:
                salary = 'N/A'

            try:
                locate = item.select_one().get_text(strip=True)
                
            except AttributeError:
                locate = 'N/A'

            csvWriter.writerow([name, carrer, form, salary, locate])
