# https://jumin.mois.go.kr/ageStatMonth.do
# 서울특별시, 인천직할시, 경기도 3개의 인구를 웹스크래핑해서
# 서울특별시 : 인구
# 인천직할시 : 인구
# 경기도 : 인구
# 합계 : 인구를 출력하시오.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# selenium은 자동화프로그램
browser = webdriver.Chrome()
url = 'https://jumin.mois.go.kr/ageStatMonth.do'
browser.get(url)
time.sleep(3)

soup = BeautifulSoup(browser.page_source,'lxml')
# with open ("jumin.html","w",encoding="utf8") as f:
#      f.write(soup.prettify())
# 테이블 검색
tb = soup.find("table",{"id":"contextTable"})
# tbody 검색
tbody = tb.find("tbody")
print('-'*60)
# trs 검색
trs =tbody.find_all("tr") 
print("trs의 개수 : ",len(trs))
print(trs[1])
# td 검색
tds = trs[1].find_all("td")
print("tds의 개수 : ",len(tds))
seoul = tds[2].text
print("서울특별시인구수 : ",seoul)
tds = trs[4].find_all("td")
incheon = tds[2].text
print("인천광역시인구수 : ",incheon)
tds = trs[9].find_all("td")
kyungggi =tds[2].text
print("경기도인구수 : ",kyungggi)

total = int(seoul.replace(",",""))+int(incheon.replace(",",""))+int(kyungggi.replace(",",""))
print("수도권 인구수 : ",format(total,","))
