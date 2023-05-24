# 자동화 구현
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #웹의 특정 요소가 추가 될때 까지 기다리게 하는 코드 추가
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

import multiprocessing 
import requests
import pandas as pd
import time
import csv


def auto_motive(url , word):
    chrome_options = Options()
    # headless 설정
    chrome_options.headless = True
    start_time = time.time()
    browser = webdriver.Chrome()                      #webdriver를 Chrome 으로 설정함
    browser.get(url)            #워크넷의 url 저장
    browser.implicitly_wait(10)                       #최대 10초까지 기다리게 하는 함수 특정요소를 찾기 위해 10초 동안 대기. 시간 안에 찾아질시 즉시 중단. -HG
    search = browser.find_element(By.ID, 'topQuery')  #element 중 'topQuery'를 검색한다.
    search.click()                                    #검색한 element를 클릭한다
    keyword = word
    search.send_keys(keyword)                         #keyword를 검색창에 전송한다
    search.send_keys(Keys.ENTER)                      #Enter 키를 전송한다
    wait = WebDriverWait(browser, 10)                 #10초간 기다린다. - 해당부분 로딩완료되는 시점까지만 wait 할수 있는지 궁금함 -jm
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')))  #-> 이 코드의 추가로 특정 요소가 찾아 진다면 즉시 중단 - HG
    button = browser.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')  
    button.click()
    variable = browser.current_url                                       #입력된 키워드의 페이지 현재 주소를 variable 에 입력받음

    return (browser , variable)