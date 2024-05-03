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
url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.get(url)
time.sleep(2)


soup = BeautifulSoup(browser.page_source,"lxml")
# with open ("coupang1.html","w",encoding="utf8") as f:
     # f.write(soup.prettify())

# all_elem = soup.find_all("div",{"class":"descriptions-inner A"})
# print(len(all_elem))
titles = soup.find_all("div",{"class":"name"})
print(titles[0].text)

prices = soup.find_all("strong",{"class":"price-value"})
print(prices[0].text)

rates = soup.find_all("em",{"class":"rating"})
print(rates[0].text)

reviews = soup.find_all("span",{"class":"rating-total-count"})
print(reviews[3].text[1:-1])

for i in range(len(titles)):
     titles = soup.find_all("div",{"class":"name"})
     print(titles[i].text)

     prices = soup.find_all("strong",{"class":"price-value"})
     print(prices[i].text)

     rates = soup.find_all("em",{"class":"rating"})
     print(rates[i].text)

     reviews = soup.find_all("span",{"class":"rating-total-count"})
     print(reviews[i].text[1:-1])