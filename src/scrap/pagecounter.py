from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #웹의 특정 요소가 추가 될때 까지 기다리게 하는 코드 추가
from selenium.common.exceptions import TimeoutException 
from bs4 import BeautifulSoup
import re

# 공통된 키워드에 대한 사람인과 워크넷의 전체 페이지 수를 측정해서 리턴합니다
# 단일 page_count 함수에 if else 문으로 작업을 나누었습니다. 이유는 귀찮아서..

def extract_number(string):  #사람인에서 사용되는 함수 , 전체 페이지 정보 추출을 위한 문자열 추출
    return int(''.join(re.findall(r'\d+', string.replace(',', ''))))

def page_count(browser , section, url):
    
    if(url == "https://www.saramin.co.kr/"):
       
        total_items = browser.find_element(By.CSS_SELECTOR, section).text
        total_items = extract_number(total_items)                       #1000 자리 넘어가면 문자열에 , 가 들어가면서 int 형 변환에러가 발생하므로 , 제거해 주는 코드 추가  -LGJ    23/05/17
        page_count = total_items // 10
        total_page = []    
      
        if total_items % 10 > 0:
            page_count += 1
    
        for i in range(page_count):
            total_page.append(i)


        return total_page
       
                    
    else:

        total_items = browser.find_element(By.CSS_SELECTOR, 'span.font-size-14.font-cgray em.count').text
        total_items = int(total_items.replace(",",""))                       #1000 자리 넘어가면 문자열에 , 가 들어가면서 int 형 변환에러가 발생하므로 , 제거해 주는 코드 추가  -LGJ    23/05/17
        page_count = total_items // 10
        total_page = []

        if total_items % 10 > 0:
           page_count += 1
    
        for i in range(page_count):
            total_page.append(i)
        
 
        return total_page

    

    
