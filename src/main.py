from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(r'C:\program files\python310\chromedriver.exe')

browser.get('https://www.work.go.kr/seekWantedMain.do')
browser.implicitly_wait(5)

first_sel = browser.find_element(By.ID ,'topQuery')
first_sel.send_keys("벡엔드")
first_sel.send_keys(Keys.ENTER)
time.sleep(100)
#third_sel = browser.find_element(By.CLASS_NAME ,'btn')
#third_sel.click()
second_sel = browser.find_element(By.CLASS_NAME,'line-dot')
second_sel.click()
print(second_sel.text)