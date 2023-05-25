from startfunction import start
import time
import multiprocessing
if __name__ == '__main__':
    start_time = time.time()
    url = ["https://www.saramin.co.kr/" , "https://www.work.go.kr"]
    dir = "C:\CSV\data.csv"
    keyword = input("입력하세요 : ")

    pool = multiprocessing.Pool(processes=4)                             #8개 프로세스를 호출하였습니다.. 추가 할 수 있는데 컴퓨터 성능에 따라 달라집니다
    pool.starmap(start, [(address, dir, keyword) for address in url])   #get_items 함수 작업 요소를 전달합니다 , 전체 페이지 수 리스트와 현재 주소입니다.
    pool.close()                                                         # 테스트에 사용한 키워드는 '백엔드' 89개 회사 정보를 크롤링합니다. 기존 코드 30초에서 20초로 10 초 단축시켰습니다.
    pool.join()

    print("--- %s seconds ---" % (time.time() - start_time)) # 속도 측정용 코드입니다 ..   
    
