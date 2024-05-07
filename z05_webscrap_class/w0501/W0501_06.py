import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url= "https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page=1"
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

time.sleep(2)

soup = BeautifulSoup(browser.page_source,"lxml")
with open ("yeogi.html","w",encoding="utf8") as f:
     f.write(soup.prettify())

title = soup.find_all("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
print(title[0].text)

for t in title[0:21]:
     print("호텔 이름 : ",t.text.strip())

# 선생님 풀이
hotels = soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})
print(len(hotels))

title = hotels[0].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
print(title.text)




# #  DB 연결
# conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
# cursor = conn.cursor()
# sql = ''''''
# cursor.execute(sql)
# # DB 연결해제
# cursor.close()
# conn.close()
