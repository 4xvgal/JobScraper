#데이터를 크롤링하는 함수입니다.
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
import requests
import csv
import os
import time
import portalocker



#사람인과 , 워크넷 크롤링을 각각 컨트롤하는 getinfo()
#주의 : 현재 csv 파일은 워크넷과 사람인 각각 따로 생성하게 두었습니다.

def select_info(item, section=None):
    if section == None:
        return 'N/A'
    else:
        selected_element = item.select_one(section)

        if selected_element is None:
            return 'N/A'
        else:
            return selected_element.get_text(strip=True).replace('\n','')                                                                  #select_info 함수 만드신거 여기 적용했습니다.
    
# 데이터를 CSV 파일로 저장하기 위한 함수
def save_to_csv(data, absolute_path):
    with portalocker.Lock(absolute_path, 'a') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)

def get_info(page_index, url, route, veriable):
    # 사람인 크롤링
    def get_saramin():
        ua = UserAgent(verify_ssl=False)                                                               #사람인은 자동화된 시스템을 제한하는건지 계속 에러 페이지로 리디렉션 해서 가상 유저 헤더로 넣어서 해결하였습니다.
        headers = {'User-Agent': ua.random}
        new_url = veriable.replace("recruitPage=1", f"recruitPage={page_index}")
        response = requests.get(new_url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.select("div.item_recruit")
        absolute_path = os.path.abspath(route[0])

        # 처음 크롤링을 시작할 때 기존의 파일 삭제
        if page_index == 1 and os.path.exists(absolute_path):
            os.remove(absolute_path)
            if os.path.exists('C://CSV/merged.csv'):
                os.remove('C://CSV/merged.csv')
                

        with open(absolute_path, 'a', encoding='CP949', newline='', errors='ignore') as f:
            csvWriter = csv.writer(f)

            for item in items:                                                                          #가상 선택자 에러 계속 띄워서 다른걸로 바꾸엇습니다
                name = select_info(item,'div.area_corp > strong > a')                                        # select_info 함수 써서 더 간결하게 변햇습니다.
                form = select_info(item, 'div.job_condition > span:nth-child(4)')
                carrer = select_info(item, 'div.job_condition > span:nth-child(2)')
                education = select_info(item, 'div.job_condition > span:nth-child(3)')
                salary = select_info(item, None)
                locate = select_info(item, 'div.job_condition > span:nth-child(1)')
                locate = locate.replace("근무지", "")   

                csvWriter.writerow([name, carrer, education,form, salary, locate])

        filename = absolute_path
        header = ['회사명', '경력','학력', '고용형태', '급여', '근무지']

        data = []
        with open(filename, 'r', encoding='CP949', newline='', errors='ignore') as file:
            reader = csv.reader(file)
            data = list(reader)

        data.insert(0, header)
 
        new_filename = r'C:\CSV\saramin_final.csv'                                              #사람인은 saramin_final.csv 를 최종적으로 헤더까지 추가된 파일로 지정했습니다 

        with open(new_filename, 'w', encoding='CP949', newline='', errors='ignore') as file:
            writer = csv.writer(file)
            writer.writerows(data)


    #워크넷 크롤링부
    def get_worknet(): 
        
        new_url = veriable.replace("pageIndex=1", f"pageIndex={page_index}")      # page_index 위치에 해당하는 페이지의 주소 new_url
        response = requests.get(new_url)                                          # 각 페이지 마다 파싱(BeautifulSoup)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.select("li.cont-right")
        absolute_path = os.path.abspath(route[1])                                 # 절대경로 설정을 위한 os 모듈 사용 (워크넷의 경로는 route 리스트 형태로 인덱스 1번에 있습니다.)

        # 처음 크롤링을 시작할 때 기존의 파일 삭제
        if page_index == 1 and os.path.exists(absolute_path):
            os.remove(absolute_path)
        with open(absolute_path, 'a', encoding='CP949', newline='', errors='ignore') as f:
            csvWriter = csv.writer(f)

            for item in items:
                name = select_info(item, 'div.txt > span')
                form = select_info(item, '.cp-info > p > span:nth-child(1)')
                career = select_info(item, '.cp-info > p > span:nth-child(2)')
                salary = select_info(item, '.cp-info > p > span:nth-child(4)')
                locate = select_info(item, '.cp-info > p:nth-child(2) > span:nth-child(1)')
                locate = locate.replace("근무지", "")
                education = select_info(item, '.cp-info > p > span:nth-child(3)')

                save_to_csv([name, career, education, form, salary, locate], absolute_path)


        filename = absolute_path  # 기존의 CSV 파일 경로
        header = [ '회사명', '경력','학력', '고용형태', '급여', '근무지']

        # 기존 데이터 읽기
        data = []
        with portalocker.Lock(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        # 헤더 추가
        data.insert(0, header)

        # 수정된 데이터를 새로운 파일에 쓰기
        new_filename = r'C:\CSV\worknet_final.csv'                      #워크넷은 workent_final.csv 를 최종적으로 헤더까지 추가된 파일로 지정했습니다 

        with portalocker.Lock(new_filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data)

         
                
    # 조건문입니다. 사람인과 , 워크넷의 각각 주소에 따라 위의 함수가 작동합니다 
    if(url == 'https://www.saramin.co.kr/'):
        get_saramin()
    else:
        get_worknet()
