from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 사람인 웹브라우저를 실행하는 코드
def saramin(url, word):

    # 아래 옵션이 추가된 이유는 사람인이 headless로 실행되는 크롤러를 인식하고 실행을 막는 거 같아서 추가했더니 잘돌아갑니다 .. 참조: https://beomi.github.io/gb-crawling/posts/2017-09-28-HowToMakeWebCrawler-Headless-Chrome.html
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

    # 여기서 부터는 이전과 동일
    keyword = word
    browser = webdriver.Chrome('chromedriver', chrome_options=options)
    browser.get(url)
    browser.implicitly_wait(10)
    search = browser.find_element(By.ID, 'btn_search')
    search.click()
    search = browser.find_element(By.CSS_SELECTOR, 'input.key')
    search.click()
    search.send_keys(keyword)
    browser.implicitly_wait(10)
    search_button = browser.find_element(By.ID, 'btn_search_recruit')
    actions = ActionChains(browser)
    actions.move_to_element(search_button).click().perform()
    wait = WebDriverWait(browser, 10)
    button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/ul[1]/li[2]/a')))
    button.click()

    variable = browser.current_url

    return browser, variable

# 워크넷 웹브라우저를 실행하는 코드
def worknet(url, word):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    
    # 여기서 부터는 이전과 동일
    keyword = word
    browser = webdriver.Chrome('chromedriver', chrome_options=options)
    browser.get(url)
    browser.implicitly_wait(10)
    search = browser.find_element(By.ID, 'topQuery')
    search.click()
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')))
    button.click()

    variable = browser.current_url

    return browser, variable


    

