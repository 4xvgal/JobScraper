from concurrent.futures import ThreadPoolExecutor
from crawling import get_worknet
from crawling import get_saramin

def thread(total_page, variable, route):
    pool = ThreadPoolExecutor(3)

    if "https://www.saramin.co.kr/" in variable:
        future = pool.submit(get_saramin, [(page, route, variable) for page in total_page])
        
    else:
        future = pool.submit(get_worknet, [(page, route, variable) for page in total_page])

    pool.shutdown(wait=True)