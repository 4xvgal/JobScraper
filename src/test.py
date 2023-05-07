from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
baseUrl = 'https://www.work.go.kr'  #워크넷의 url 저장
browser = webdriver.Chrome()        #webdriver를 Chrome 으로 설정함

browser.get(baseUrl)   #워크넷의 url를 get함수로 request 하여 browser에 저장한다.
browser.implicitly_wait(10) #10초 기다리는 함수? - 주석처리필요 - 로딩완료시점까지만 wait 할수있는지 -jm

search = browser.find_element(By.ID, 'topQuery')   #element 중 'topQuery'를 검색한다.
search.click()                                      #검색한 element를 클릭한다

keyword = input("입력하세요")                           #검색할단어를 콘솔에서 input 받는다.
search.send_keys(keyword)                             #keyword를 검색창에 전송한다
search.send_keys(Keys.ENTER)                          #Enter 키를 전송한다

wait = WebDriverWait(browser, 10)                       #10초간 기다린다. - 해당부분 로딩완료되는 시점까지만 wait 할수 있는지 궁금함 -jm

button = browser.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')  
button.click()

#구인 정보
items = browser.find_elements(By.CSS_SELECTOR, 'li.cont-right')   

names = []
for item in items:
    name = item.find_element(By.CSS_SELECTOR, 'div.txt > span').text
    names.append(name)
    # infos = item.find_elements(By.CSS_SELECTOR, 'cp-info > p')

print(names)


time.sleep(100)