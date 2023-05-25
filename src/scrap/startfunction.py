from automation import auto_motive
from pagecounter import page_count 
from multithread import thread


def start(url , route , keyword):
    browser , veriable = auto_motive(url , keyword)
    total_page = page_count(browser, 'span.cnt_result', url)
    thread(total_page , veriable, route)
    
