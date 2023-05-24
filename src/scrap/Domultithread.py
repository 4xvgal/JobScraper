#멀티스레드 적용시킬 예정
#사이트 Url 을 startfucntion 으로 넘기는 부분에서 멀티 프로세스 적용하고
#crawling 부에서 멀테스레드 적용 
from concurrent.futures import ThreadPoolExecutor
from crawling import get_items

def multi_thread(total_page , variable):
    pool = ThreadPoolExecutor(3)
    future = pool.submit(get_items, [(page, variable) for page in total_page])   #get_items 함수 작업 요소를 전달합니다 , 전체 페이지 수 리스트와 현재 주소입니다.
    future.close()                                                        
    future.join()
                  