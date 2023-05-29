from automation import saramin
from automation import worknet
from pagecounter import page_count 
from multithread import thread

#여러개 함수에 값을 전달해 통합 실행하는 start 함수

def start(url , route , keyword):

    #1.웹페이지 실행
    if(url ==   'https://www.saramin.co.kr/'):
         browser , veriable = saramin(url , keyword)

    else:
         browser , veriable = worknet(url , keyword)

    #2.전체페이지 계산
    total_page = page_count(browser, 'span.cnt_result', url)

    #3.멀티스레드(크롤링 과 , csv 작성)
    thread(total_page , url, veriable, route)
    

