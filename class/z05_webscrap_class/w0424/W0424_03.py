import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://www.daum.net"

# 크롬브라우저 열기
browser = webdriver.Chrome()
# 다음페이지 이동
browser.get(url)

# 로그인 버튼 클릭
elem = browser.find_element(By.XPATH,'//*[@id=""')
elem.click()
time.sleep(random.randint(2,5))

input_js = 'document.getElementById("id").value="{id}";\
            document.getElementById("pw").value="{pw}";\
             '.format(id='aaa',pw='1111')
time.sleep(random.randint(2,5))

elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea]/ul/li[6]/a')




# 완료
time.sleep(100)