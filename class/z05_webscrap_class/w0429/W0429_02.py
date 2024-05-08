import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 마우스 이동
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://flight.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(1)

# 출발지 선택//전체문서 b
time.sleep(1)
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(1)
elem.click()
# 국내부분 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()

# 김포국제공항 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
time.sleep(1)
elem.click()
time.sleep(2)

# 도착지 선택//전체문서 b
time.sleep(1)
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(1)
elem.click()
# 국내부분 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()

# 김포국제공항 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주")]')
time.sleep(2) 
elem.click()

# 가는 날 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 가는 날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
print("14일 개수 : ",len(elem))
time.sleep(2)
elem[1].click()

# 가는 날 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="오는 날"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 오는 날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
print("15일 개수 : ",len(elem))
time.sleep(2)
elem[1].click()

# 인원수 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[contains(text(),"성인")]')
time.sleep(1)
elem.click()
time.sleep(1)

# 1명 추가
elem = browser.find_element(By.XPATH,'//button[@class="searchBox_outer__9n6IB"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 인원선택창 닫기
browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]').click()
browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]').click()
#항공권 검색
# 화면 대기 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 최대30초까지 대기
elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))
print(elem)
print(elem[0].text)
## 화면 스크롤 내리기
# 현재 스크롤 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 : ",prev_height)
# 스크롤 이동
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 재조정된 스크롤 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 같으면 중단하고 빠져나옴.
    prev_height = curr_height
    print("현재 높이 : ",curr_height)
# 웹스크래핑을 해서 정보를 가져오기
# 항공권 정보를 가져오기
input("Enter키 입력시 프로그램이 종료됩니다. >>")
# 화면 닫기
browser.quit()
# time.sleep(100)

# # 실제구문 1개 : find_element
# browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')

# # 실제 구문 - 여러 개 가져오기 : find_elements
# browser.find_elements(By.XPATH,'//b[text()="15"]')

# # 문자열과 일치할 때 선택하는 방법
# elem = browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')
# # 문자열이 포함되어 있을 때 선택하는 방법
# elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
# # id를 가지고 검색
# elem = browser.find_element(By.XPATH,'//i[@id="_next"]')
# # class를 가지고 선택
# elem = browser.find_element(By.XPATH,'//i[@class="_next"]')
