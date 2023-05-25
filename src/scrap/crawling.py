
from bs4 import BeautifulSoup
import requests
import csv



def get_worknet(page_index , route , veriable):

    new_url = veriable.replace("pageIndex=1", f"pageIndex={page_index}")  # page_index 위치에 해당하는 페이지의 주소 new_url
    response = requests.get(new_url)   # 각 페이지 마다 파싱(BeautifulSoup)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select("li.cont-right")

    
    with open(route, 'a', encoding='CP949', newline='') as f:     #csv 파일생성
        csvWriter = csv.writer(f)

        for item in items:
            try:
                name = item.select_one('div.txt > span').get_text(strip=True)  # 딸려오는 개행문자 제거 - 에러수정   23/05/17
            except AttributeError:
                name = 'N/A'

            try:
                form = item.select_one('.cp-info > p > span:nth-child(1)').get_text(strip=True)
            except AttributeError:
                form = 'N/A'    

            try:
               carrer = item.select_one('.cp-info > p > span:nth-child(2)').get_text(strip=True)
               
            except AttributeError:
                carrer = 'N/A'

            try:
                salary = item.select_one('.cp-info > p > span:nth-child(4)').get_text(strip=True)
               
            except AttributeError:
                salary = 'N/A'

            try:
                locate = item.select_one('.cp-info > p:nth-child(2) > span:nth-child(1)').get_text(strip=True)
                
            except AttributeError:
                locate = 'N/A'

            csvWriter.writerow([name, carrer, form, salary, locate])

def get_saramin(page_index , route , veriable):

    new_url = veriable.replace("recruitPage=1", f"recruitPage={page_index}")  # page_index 위치에 해당하는 페이지의 주소 new_url
    response = requests.get(new_url)   # 각 페이지 마다 파싱(BeautifulSoup)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select("div.content")

    print(new_url)
    

    with open(route, 'a', encoding='UTF-8', newline='') as f:     #csv 파일생성
        csvWriter = csv.writer(f)

        for item in items:
            try:
                name = item.select_one('div.company-name a').get_text(strip=True)  # 딸려오는 개행문자 제거 - 에러수정   23/05/17
            except AttributeError:
                name = 'N/A'

            try:
                form = item.select_one('div.job_condition > span::nth-child(4)').get_text(strip=True)
            except AttributeError:
                form = 'N/A'    

            try:
                carrer = item.select_one('div.job_condition > span::nth-child(2)').get_text(strip=True)
               
            except AttributeError:
                carrer = 'N/A'

            try:
                salary = item.select_one().get_text(strip=True)
               
            except AttributeError:
                salary = 'N/A'

            try:
                locate = item.select_one().get_text(strip=True)
                
            except AttributeError:
                locate = 'N/A'

            csvWriter.writerow([name, carrer, form, salary, locate]) 
