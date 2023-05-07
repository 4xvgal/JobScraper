from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

browser.get('https://www.work.go.kr')
browser.implicitly_wait(10)

search = browser.find_element(By.ID, 'topQuery')
search.click()

search.send_keys('자바')
search.send_keys(Keys.ENTER)

wait = WebDriverWait(browser, 10)

button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()

#구인 정보
items = browser.find_element(By.CLASS_NAME, 'top')