 
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def extract_number(string):  #문자열에서 숫자만 추출
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

    

    
