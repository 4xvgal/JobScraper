import requests
from bs4 import BeautifulSoup

#미완성

def getMaxpages(url):      #Url 의 최대 페이지 수를 return 하는 함수             
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html , 'html.parser')

def getPageIndex(url):      #url의 page index를 찾아 return 하는 함수
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html , 'html.parser')
    page_numbers = soup.find_all('a', class_='')

#testing definition


url = 'https://www.work.go.kr/wnSearch/unifSrch.do?regDateStdt=&regDateEndt=&colName=tb_workinfo&srchDateSelected=all&sortField=RANK&sortOrderBy=DESC&searchDateInfo=&temp=&pageIndex=1&tabName=tb_workinfo&dtlSearch=&query=%EC%9E%90%EB%B0%94&radio_period=on&srchStdt=&srchEndt=&reQuery=&agreeQuery=&prikeyQuery=&exceptQuery='


print(getMaxpages(url))
