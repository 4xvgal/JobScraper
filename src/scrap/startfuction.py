import automation
import pagecount
def start(keyword , route , url):
    browser , veriable = automation(keyword)
    pagecount(browser)
