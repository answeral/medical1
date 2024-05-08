import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
# 화면이 나타는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 마우스 이동
import pyautogui

# 1. 야놀자 홈페이지 이동
# 2. 검색창에 호텔 입력,
# 3. 날짜선택
# 4. 6월 5일,6일 클릭
# 5. 확인버튼 클릭
# 6. 검색창 클릭 > enter키 입력
# 7. 검색 진행
# 8. 스크롤 이동 반복
# ============================================================================================
# 9. 정보창이 띄어지면, 이미지,제목,평점,평가수,금액 저장하시오.
# yanolja 테이블
# yno,img,title,grade,grade_num,price

url = "https://www.yanolja.com/?utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-327025203539&gad_source=1&gclid=EAIaIQobChMI3NnUp73uhQMVD1wPAh2u4w_nEAAYASAAEgJNHPD_BwE"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
elem = browser.find_element(By.CLASS_NAME,'HomeSearchBar_searchBoxPlaceholder__3_zPf')
elem.click()
time.sleep(2)

elem = browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2')
elem.click()
time.sleep(2)

elem.send_keys("호텔")
elem.send_keys(Keys.ENTER)
time.sleep(3)

elem =browser.find_element(By.CLASS_NAME,'DateRange_text__3YHNV')
elem.click()
time.sleep(3)

elem = browser.find_elements(By.XPATH,'//td[text()="5"]')[1]
elem.click()
time.sleep(2)
elem = browser.find_elements(By.XPATH,'//td[text()="6"]')[1]
elem.click()
time.sleep(2)

elem = browser.find_element(By.CLASS_NAME,'DateRangePicker_rangePickerConfirmButton__2c41H')
elem.click()
time.sleep(2)
# elem = browser.find_element(By.CLASS_NAME,)
# elem.click()Icon_icon__2BP_o DateRange_icon__1oMYk DateRange_renewal22H2__n-WCV

prev_height = browser.execute_script("return document.body.scrollHeight")
print("현재 높이:",prev_height)
cnt = 0
while True:
    if cnt == 5: break
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
        
    prev_height = curr_height
    print("현재 높이 : ",curr_height)
    cnt +=1