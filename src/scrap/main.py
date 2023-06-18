#메인함수입니다. 전체 함수를 실행하는 하나의 함수인 start 함수를 멀티프로세싱으로 실행합니다.
#시스템 구성은 두개 url 에 대해 멀티프로세스를 적용해 동시에 작업을 실행하고 각 url의 페이수에 해당하는 각각의 페이지의 크롤링은 멀티스레드 방식을 사용했습니다.

from startfunction import start
import time
import multiprocessing


def run_crawling(keyword, processCount, SavingDir): #검색어, 멀티프로세서 수, 저장경로
    start_time = time.time()
    url = ["https://www.saramin.co.kr/", "https://www.work.go.kr"]
    route = ["C:\CSV\saramin_data.csv", "C:\CSV\worknet_data.csv"]

    pool = multiprocessing.Pool(processCount=8)
    pool.starmap(start, [(address, route, keyword) for address in url])
    pool.close()
    pool.join()

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    run_crawling()