from auto_Selenium import auto_motive
from pagecounter import page_count 
from crawl_BS import get_items
def start(url , route , keyword):
    browser , veriable = auto_motive(url , keyword)
    total_page = page_count(browser, 'span.cnt_result')
    get_items(total_page, veriable, url)
