from automation import auto_motive
from pagecounter import page_count 
from crawling import get_items
def start(url , route , keyword):
    browser , veriable = auto_motive(url , keyword)
    total_page = page_count(browser)
    get_items(total_page, veriable)
