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

def select_info(item, section):
    try:
        return item.select_one(section).get_text(strip=True)  # 딸려오는 개행문자 제거 - 에러수정   23/05/17
    except AttributeError:
        return 'N/A'


def page_count(broswer, section):
    total_items = browser.find_element(By.CSS_SELECTOR, section).text
    total_items = int(total_items.replace(",",""))                     #1000 자리 넘어가면 문자열에 , 가 들어가면서 int 형 변환에러가 발생하므로 , 제거해 주는 코드 추가  -LGJ    23/05/17
    page_count = total_items // 10
    total_page = []

    if total_items % 10 > 0:
        page_count += 1
    
    for i in range(page_count):
        total_page.append(i)
    return total_page




#현재 페이지의 구인정보 추출  멀티 프로세싱 적용을 위해 함수로 구현하였습니다.
def get_items(page_index, url):


    new_url = url.replace("pageIndex=1", f"pageIndex={page_index}")  # page_index 위치에 해당하는 페이지의 주소 new_url
    response = requests.get(new_url)   # 각 페이지 마다 파싱(BeautifulSoup)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select("li.cont-right")

    print(new_url)
    

    with open(r"C:\CSV\data.csv", 'a', encoding='UTF-8', newline='') as f:     #csv 파일생성
        csvWriter = csv.writer(f)

        for item in items:
            name = select_info(item,'div.txt > span')
            form = select_info(item,'.cp-info > p > span:nth-child(1)')
            carrer = select_info(item,'.cp-info > p > span:nth-child(2)')
            salary = select_info(item,'.cp-info > p > span:nth-child(4)')
            locate = select_info(item,'.cp-info > p:nth-child(2) > span:nth-child(1)')
            title = select_info(item, 'div.link > a')
            link = 'https://www.work.go.kr' + item.select_one('a').get('href')


            csvWriter.writerow([title,name, carrer, form, salary, locate, link])


if __name__ == '__main__':
    
   
    # 자동화 구현
    chrome_options = Options()
    # headless 설정
    chrome_options.headless = True
    start_time = time.time()
    browser = webdriver.Chrome()                      #webdriver를 Chrome 으로 설정함
    browser.get('https://www.work.go.kr')             #워크넷의 url 저장
    browser.implicitly_wait(10)                       #최대 10초까지 기다리게 하는 함수 특정요소를 찾기 위해 10초 동안 대기. 시간 안에 찾아질시 즉시 중단. -HG
    search = browser.find_element(By.ID, 'topQuery')  #element 중 'topQuery'를 검색한다.
    search.click()                                    #검색한 element를 클릭한다
    keyword = input("입력하세요 : ")                   #검색할단어를 콘솔에서 input 받는다
    search.send_keys(keyword)                         #keyword를 검색창에 전송한다
    search.send_keys(Keys.ENTER)                      #Enter 키를 전송한다
    wait = WebDriverWait(browser, 10)                 #10초간 기다린다. - 해당부분 로딩완료되는 시점까지만 wait 할수 있는지 궁금함 -jm
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')))  #-> 이 코드의 추가로 특정 요소가 찾아 진다면 즉시 중단 - HG
    button = browser.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')  
    button.click()
    variable = browser.current_url #입력된 키워드의 페이지 현재 주소를 variable 에 입력받음

    #최대페이지 계산 함수
    total_page = page_count(browser,'span.font-size-14.font-cgray em.count') 


    print("test")
    # 멀티 프로세스 적용
    pool = multiprocessing.Pool(processes=8)                             #8개 프로세스를 호출하였습니다.. 추가 할 수 있는데 컴퓨터 성능에 따라 달라집니다
    pool.starmap(get_items, [(page, variable) for page in total_page])   #get_items 함수 작업 요소를 전달합니다 , 전체 페이지 수 리스트와 현재 주소입니다.
    pool.close()                                                         # 테스트에 사용한 키워드는 '백엔드' 89개 회사 정보를 크롤링합니다. 기존 코드 30초에서 20초로 10 초 단축시켰습니다.
    pool.join()
                                

    filename = r'C:\CSV\data.csv'   # 기존의 CSV 파일 경로
    header = ['제목','회사명', '경력','고용형태', '급여', '근무지','링크']  # 추가할 헤더 정보

    # 기존 데이터 읽기
    data = []
    with open(filename, 'r', encoding='utf-8',newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    # 헤더 추가
    data.insert(0, header)

    # 수정된 데이터를 새로운 파일에 쓰기
    new_filename = r'C:\CSV\data1.csv'                       # 새로 생성될 파일 경로
    with open(new_filename, 'w', encoding='utf-8',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
                                                            
    print("--- %s seconds ---" % (time.time() - start_time)) # 속도 측정용 코드입니다 .. 