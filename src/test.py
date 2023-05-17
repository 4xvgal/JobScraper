from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #웹의 특정 요소가 추가 될때 까지 기다리게 하는 코드 추가
from selenium.common.exceptions import NoSuchElementException #예외처리를 위함
from bs4 import BeautifulSoup

import requests
import pandas as pd
import time
import csv

browser = webdriver.Chrome()  #webdriver를 Chrome 으로 설정함

browser.get('https://www.work.go.kr')   #워크넷의 url 저장
browser.implicitly_wait(10)            #최대 10초까지 기다리게 하는 함수 특정요소를 찾기 위해 10초 동안 대기. 시간 안에 찾아질시 즉시 중단. -HG

search = browser.find_element(By.ID, 'topQuery')  #element 중 'topQuery'를 검색한다.
search.click()                                    #검색한 element를 클릭한다

keyword = input("입력하세요 : ")                 #검색할단어를 콘솔에서 input 받는다
search.send_keys(keyword)                     #keyword를 검색창에 전송한다
search.send_keys(Keys.ENTER)                  #Enter 키를 전송한다


wait = WebDriverWait(browser, 10)           #10초간 기다린다. - 해당부분 로딩완료되는 시점까지만 wait 할수 있는지 궁금함 -jm
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')))  #-> 이 코드의 추가로 특정 요소가 찾아 진다면 즉시 중단 - HG


button = browser.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')  
button.click()

#페이지 수     아직 추가하지 않음 
#검색된 구직 정보의 개수를 기반으로 페이지 수를 측정하여 카운트 - HG
total_items = browser.find_element(By.CSS_SELECTOR, 'span.font-size-14.font-cgray em.count').text
total_items = int(total_items)
page_count = total_items // 10
if total_items % 10 > 0:
    page_count += 1

variable = browser.current_url                          #입력된 키워드의 페이지 현재 주소를 variable 에 입력받음
names = []
#파일 생성
f = open(r"C:\Users\gwon9\Documents\Python project\data.csv", 'w',encoding='CP949', newline='') # 파일 저장 위치 이 위치에 엑셀 파일이 저장됨
csvWirter = csv.writer(f)    


# ...
for page_index in range(1, page_count+1):                                          
    new_url = variable.replace("pageIndex=1", f"pageIndex={page_index}")  
    browser.get(new_url)  # selenium을 사용하여 실제로 페이지를 이동
    time.sleep(3)  # 페이지 로딩을 위해 잠시 대기
    html = browser.page_source  # 현재 페이지의 HTML을 가져옴
    soup = BeautifulSoup(html , 'html.parser')

    # 이 페이지에서의 구인 정보를 가져옵니다.
    items = browser.find_elements(By.CSS_SELECTOR, 'li.cont-right')
    for item in items:
        try:
            name = item.find_element(By.CSS_SELECTOR, 'div.txt > span').text
        except NoSuchElementException:
            name = 'N/A'
        try:
            form = item.find_element(By.CSS_SELECTOR, '.cp-info > p > span:nth-child(1)').text
        except NoSuchElementException:
            form = 'N/A'
        try:
            carrer = item.find_element(By.CSS_SELECTOR, '.cp-info > p > span:nth-child(2)').text
        except NoSuchElementException:
            carrer = 'N/A'
        try:
            salary = item.find_element(By.CSS_SELECTOR, '.cp-info > p > span:nth-child(4)').text
        except NoSuchElementException:
            salary = 'N/A'
        try:
            locate = item.find_element(By.CSS_SELECTOR, '.cp-info > p:nth-child(2) > span:nth-child(1)').text
        except NoSuchElementException:
            locate = 'N/A'

        #데이터 쓰기
        csvWirter.writerow([name, carrer ,form, salary, locate])

#파일 닫기
f.close()
