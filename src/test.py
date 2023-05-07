from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

browser = webdriver.Chrome()

browser.get('https://www.work.go.kr')
browser.implicitly_wait(10)

search = browser.find_element(By.ID, 'topQuery')
search.click()

keyword = input("입력하세요")
search.send_keys(keyword)
search.send_keys(Keys.ENTER)

wait = WebDriverWait(browser, 10)

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