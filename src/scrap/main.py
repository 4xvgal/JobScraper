#메인함수입니다. 전체 함수를 실행하는 하나의 함수인 start 함수를 멀티프로세싱으로 실행합니다.
#시스템 구성은 두개 url 에 대해 멀티프로세스를 적용해 동시에 작업을 실행하고 각 url의 페이수에 해당하는 각각의 페이지의 크롤링은 멀티스레드 방식을 사용했습니다.

from startfunction import start
import time
import multiprocessing

if __name__ == '__main__':
    
    #start 에 전달 할 요소들
    start_time = time.time()
    url = ["https://www.saramin.co.kr/" , "https://www.work.go.kr"]
    route = ["C:\CSV\saramin_data.csv" , "C:\CSV\worknet_data.csv"]
    keyword = input("입력하세요 : ")

    pool = multiprocessing.Pool(processes=8)                            #16개 프로세스를 호출하였습니다.. 추가 할 수 있는데 컴퓨터 성능에 따라 달라집니다
    pool.starmap(start, [(address, route, keyword) for address in url])  #주소 , 경로 , 키워드를 준다.
    pool.close()                                                         # 테스트에 사용한 키워드는 '백엔드' 89개 회사 정보를 크롤링합니다. 기존 코드 30초에서 20초로 10 초 단축시켰습니다.
    pool.join()

    print("--- %s seconds ---" % (time.time() - start_time)) # 속도 측정용 코드입니다 ..   
    
