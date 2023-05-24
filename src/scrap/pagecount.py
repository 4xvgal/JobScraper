 
def page_count(browser):
    total_items = browser.find_element(By.CSS_SELECTOR, 'span.font-size-14.font-cgray em.count').text
    total_items = int(total_items.replace(",",""))                       #1000 자리 넘어가면 문자열에 , 가 들어가면서 int 형 변환에러가 발생하므로 , 제거해 주는 코드 추가  -LGJ    23/05/17
    page_count = total_items // 10
    total_page = []

    if total_items % 10 > 0:
        page_count += 1
    
    for i in range(page_count):
        total_page.append(i)

    return total_page
