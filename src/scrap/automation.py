# 자동화 구현
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import certifi
import os

def auto_motive(url, word):
   

    def controller():
        if url == "https://www.saramin.co.kr/":
            return saramin()
        else:
            return worknet()

    def saramin():
        keyword = word  

        browser = webdriver.Chrome()
        browser.get(url)           
        browser.implicitly_wait(30)                   
        search = browser.find_element(By.ID, 'btn_search')  
        search.click()
        search = browser.find_element(By.CSS_SELECTOR, 'input.key')  
        search.click()          
        search.send_keys(keyword)                                                             
        search.send_keys(Keys.ENTER)                      
        wait = WebDriverWait(browser, 10)               
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/ul[1]/li[2]/a'))) 
        button = browser.find_element(By.XPATH, '//*[@id="content"]/ul[1]/li[2]/a')  
        button.click()

        variable = browser.current_url

        return browser, variable

    

    def worknet():
        keyword = word
        browser = webdriver.Chrome()
        browser.get(url)
        browser.implicitly_wait(30)
        search = browser.find_element(By.ID, 'topQuery')
        search.click()
        search.send_keys(keyword)
        search.click()
        search.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')))
        button = browser.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')
        button.click()

        variable = browser.current_url

        print(variable)

        return browser, variable

    return controller()

    

 