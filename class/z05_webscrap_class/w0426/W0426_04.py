import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
headers =  {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://watcha.com/browse/webtoon"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)
prev_height = browser.execute_script('retrun document.body.scrollHeight' )
print("최초 높이 : ",prev_height)
# 스크롤 내리기
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
        break
    prev_height = curr_height
    print("현재 높이 : ",curr_height)
    
soup = BeautifulSoup(browser.page_source,"lxml")
sections = soup.find_all("section",{"class":"custom-11ytuur e1134x5i3"}) 
uls = sections[14].find_all("ul",{"class":"evjjsye0 custom-plh92q-Row e8ldpmn0"})
print(uls)
lis = uls.find_all("li",{"class":"w_exposed_cell e1bnpttb3 custom-vnoe9g-RowItem etpnybg1"})
alts = lis[0].find("img")
print(lis[0].find("img"))
print("제목 : ",alts["alt"])
input("Enter키 입력시 프로그램이 종료됩니다. >>")
# 화면 닫기
browser.quit()