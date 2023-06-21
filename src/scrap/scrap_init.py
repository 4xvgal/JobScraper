#메인함수입니다. 전체 함수를 실행하는 하나의 함수인 start 함수를 멀티프로세싱으로 실행합니다.
#시스템 구성은 두개 url 에 대해 멀티프로세스를 적용해 동시에 작업을 실행하고 각 url의 페이수에 해당하는 각각의 페이지의 크롤링은 멀티스레드 방식을 사용했습니다.
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from startfunction import start
from absorption_csv import absorption
import time
import multiprocessing
from clear_csv import Initialization



def run_crawling(keyword, processCount): #검색어, 멀티프로세서 수
    start_time = time.time()
    
    url = ["https://www.saramin.co.kr/", "https://www.work.go.kr"]
    route = ["C:\CSV\saramin_data.csv", "C:\CSV\worknet_data.csv"]
    
    final_route = ["C:\CSV\saramin_final.csv", "C:\CSV\worknet_final.csv"]
    merged = "C:\CSV\merged.csv"

    if os.path.exists(merged): # 크롤링 실행 전에 파일 존재 유무를 검사해서 중복된 파일을 제거한다.
        Initialization(route, final_route, merged)

    pool = multiprocessing.Pool(processCount)
    pool.starmap(start, [(address, route, keyword) for address in url])
    pool.close()
    pool.join()

    absorption(final_route , merged) #두 개의 표본화된 csv 파일에 대한 병합을 실시한다.

    

   #print("--- %s seconds ---" % (time.time() - start_time))


#run_crawling("파이썬", 1)