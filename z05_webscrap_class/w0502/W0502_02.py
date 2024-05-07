import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
# DB연결부분
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()
url ="https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(2)
# melon
# 순번 시퀀스번호 melon_seq
# 가수 singer

soup = BeautifulSoup(browser.page_source,"lxml")

# with open("melon.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
trs = soup.find_all("tr",{"class":"lst50"})
print(len(trs)) #50개


for idx, melon in enumerate(trs):
    print(f"[ {idx+1} 번째 ]")
    # 순위 rank
    rank = trs[21].find("span",{"class":"rank"})
    print("순위 : ",rank.text.strip())
    s_rank = trs[21].find("span",{"class":"rank_wrap"})
    v_rank = trs[21].find("span",{"class":"rank_wrap"})['title']
    print(v_rank)
    if v_rank =="순위 동일":
        v_rank = 0
    elif v_rank.find('단계 하락') != -1:
        v_rank = s_rank.find("span",{"class":"down"}).text
        v_rank = int(v_rank)*-1
    else:
        v_rank = s_rank.find("span",{"class":"up"}).text
        v_rank = int(v_rank)        
    print("순위변동 : {:+d}".format(v_rank))  # +부호 넣기
    img = trs[21].find("img")['src']
    print("이미지 : ",img)

    # 제목 title
    title= melon.find("div",{"class":"ellipsis rank01"})
    print(title.text)

    # 가수

    r_singer = melon.find("div",{"class":"ellipsis rank02"})
    singer=r_singer.find("a")
    print(singer.text)

    # 좋아요 likeNum
    likeNum = melon.find("span",{"class":"cnt"})
    print(likeNum.text[4:].replace(",",""))
    print("-"*60)