#멀티 스레드부 입니다.
from concurrent.futures import ThreadPoolExecutor
from crawling import get_info

def thread(total_page, url, variable, route):

    with ThreadPoolExecutor(8) as executor: #동시에 실행될 수 있는 최대 스레드 
        futures = [executor.submit(get_info, page, url, route, variable) for page in total_page]  #각 페이지에 대한 작업을 한개의 프로세스에서 여러개의 스레드로 동시에 작업합니다. 추가로 전달되는 요소는 주소, 경로, 크롤링이 처음 시작되는 페이지인 veriable 변수 입니다.
        # 결과를 필요로 할 때까지 대기
        results = [future.result() for future in futures]