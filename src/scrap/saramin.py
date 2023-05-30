from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

import multiprocessing 
import requests
import pandas as pd
import time
import csv
import re

def select_info(item, section=None):
    try:
        return item.select_one(section).get_text(strip=True)
    except AttributeError:
        return 'N/A'
    
def scroll_down(browser):
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def extract_number(string): 
    return int(''.join(re.findall(r'\d+', string.replace(',', ''))))

def page_count(browser, section):
    total_items = browser.find_element(By.CSS_SELECTOR, section).text
    total_items = extract_number(total_items)
    page_count = total_items // 10
    total_page = []

    if total_items % 10 > 0:
        page_count += 1
    
    for i in range(page_count):
        total_page.append(i)
    return total_page

def get_items(page_index, url):
    chrome_options = Options()
    chrome_options.headless = True
    browser = webdriver.Chrome(options=chrome_options)

    new_url = url.replace("pageIndex=1", f"pageIndex={page_index}")
    browser.get(new_url)
    time.sleep(5)
    scroll_down(browser)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select("div.item_recruit")

    with open(r"C:\CSV\data.csv", 'a', encoding='UTF-8', newline='') as f: 
        csvWriter = csv.writer(f)

        for item in items:
            name = select_info(item,'div.area_corp > strong > a')
            form = select_info(item,'div.job_condition > span::nth-child(4)')
            carrer = select_info(item,'div.job_condition > span::nth-child(2)')
            salary = select_info(item,)
            locate = select_info(item,'div.job_condition > span::nth-child(1)')
            title = select_info(item, 'h2.job_tit')
            link = 'https://www.saramin.co.kr' + item.select_one('a').get('href')

            csvWriter.writerow([title,name, carrer, form, salary, locate, link])

    browser.close()

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.headless = True
    start_time = time.time()
    browser = webdriver.Chrome()
    browser.get('https://www.saramin.co.kr/') 
    browser.implicitly_wait(10)
    search = browser.find_element(By.ID, 'btn_search')
    search.click()
    search = browser.find_element(By.CSS_SELECTOR, 'input.key')
    search.click()
    keyword = input("입력하세요 : ")
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/ul[1]/li[2]/a')))
    button = browser.find_element(By.XPATH, '//*[@id="content"]/ul[1]/li[2]/a')
    button.click()
    time.sleep(2)
    total_page = page_count(browser, "#list_sort > div > div:nth-child(3) > span:nth-child(1)")
    variable = browser.current_url
    browser.close()

    with multiprocessing.Pool(processes=4) as pool:  #너무 많이 돌리면 서버 부하가 심함
        pool.starmap(get_items, [(page, variable) for page in total_page])

    print("--- %s seconds ---" %(time.time() - start_time))
