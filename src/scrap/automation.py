# 자동화 구현
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains




#사람인 웹브라우저를 실행하는 코드 
def saramin(url, word):

    keyword = word  
    browser = webdriver.Chrome()                                  #webdriver를 Chrome 으로 설정함
    browser.get(url)                                              #사람인의 url 저장
    browser.implicitly_wait(10)                                   #최대 10초까지 기다리게 하는 함수 특정요소를 찾기 위해 10초 동안 대기. 시간 안에 찾아질시 즉시 중단. -HG
    search = browser.find_element(By.ID, 'btn_search')            #검색 버튼을 찾아 상호작용. 사람인의 경우 검색 전 상호작용이 필요함
    search.click()
    search = browser.find_element(By.CSS_SELECTOR, 'input.key')   #상호 작용 후 검색창 클릭
    search.click()                                                #검색한 element를 클릭한다
    search.send_keys(keyword)                                          #keyword를 검색창에 전송한다
    search_button = browser.find_element(By.ID, 'btn_search_recruit')  #Enter키가 전송이 안되는 치명적 오류가 있어서 그냥 버튼누르는걸로 바꿨습니다..
    actions = ActionChains(browser)
    actions.move_to_element(search_button).click().perform()
    wait = WebDriverWait(browser, 10)                              #10초간 기다린다. - 해당부분 로딩완료되는 시점까지만 wait 할수 있는지 궁금함 -jm
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/ul[1]/li[2]/a')))  
    button = browser.find_element(By.XPATH, '//*[@id="content"]/ul[1]/li[2]/a')  
    button.click()

    variable = browser.current_url

    return browser, variable

    
#워크넷 웹브라우저를 실행하는 코드(이하 주석은 사람인과 동일)
def worknet(url, word):                                            
    keyword = word
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(30)
    search = browser.find_element(By.ID, 'topQuery')
    search.click()
    search.send_keys(keyword)
    search.click()
    search.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')))
    button = browser.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a')
    button.click()
    
    variable = browser.current_url

    return browser, variable


    

 