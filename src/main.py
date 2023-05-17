from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import requests
import time
import csv

baseUrl = 'https://www.work.go.kr'                   #워크넷의 url 저장
browser = webdriver.Chrome()                         #webdriver를 Chrome 으로 설정함

browser.get(baseUrl)                                 #워크넷의 url를 get함수로 request 하여 browser에 저장한다.
browser.implicitly_wait(10)                          #10초 기다리는 함수? - 주석처리필요 - 로딩완료시점까지만 wait 할수있는지 -jm

search = browser.find_element(By.ID, 'topQuery')     #element 중 'topQuery'를 검색한다.
search.click()                                       #검색한 element를 클릭한다

keyword = input("입력하세요")               #검색할단어를 콘솔에서 input 받는다. <- pyauto_gui 사용해서 외부에서 별도의 창을 띄워보았음.
search.send_keys(keyword)                             #keyword를 검색창에 전송한다
search.send_keys(Keys.ENTER)                          #Enter 키를 전송한다

wait = WebDriverWait(browser, 10)                    #10초간 기다린다. - 해당부분 로딩완료되는 시점까지만 wait 할수 있는지 궁금함 -jm

button = browser.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')  
button.click()


#구인 정보


variable = browser.current_url                          #입력된 키워드의 페이지 현재 주소를 variable 에 입력받음
names = []


for page_index in range(1, 11):                                           # 정해진 페이지의 전체 값을 추출함 ( 1)
    new_url = variable.replace("pageIndex=1", f"pageIndex={page_index}")  #page_index 위치에 해당하는 페이지의 주소 new_url
    response = requests.get(new_url)                                      #각 페이지 마다 파싱(BeautifulSoup)
    html = response.text
    soup = BeautifulSoup(html , 'html.parser')
    
    items = soup.select("li.cont-right")  

    for item in items:  
        name = item.select('div.txt > span')[0].text                       # 요소에서 텍스트 정보를 추출함.            
        names.append(name)
    # infos = item.find_elements(By.CSS_SELECTOR, 'cp-info > p')


print(names)

time.sleep(100)