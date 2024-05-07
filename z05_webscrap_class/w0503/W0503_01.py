import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECHILD
import pyautogui

# DB연결부분
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.get(url)
time.sleep(2)
# 역대 관객순
# 이미지, 제목, 누적관객수, 개봉날짜
# 이미지 저장까지
#  23 - 20 년까지
# 콘솔창에 출력하고, db에 저장

# daum_movie 테이블
# dno 시퀀스

# title varchar2(100) c-item-content>  c-item-content
# img varchar2(300)
# audience number(10)

soup = BeautifulSoup(browser.page_source,"lxml")
# with open ("daum.movie.html","w",encoding="utf8") as f:
#      f.write(soup.prettify())

strongs = soup.find_all("strong",{"class":"tit-g clamp-g"})
print(len(strongs))

titles = strongs[0].find("a").text()
print(titles)
