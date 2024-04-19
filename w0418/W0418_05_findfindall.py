import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#print(soup)

# 1. 태그로 찾는 방법 title,text(),get,a.attrs, a["href"]

# 2. find:태그 정보 찾기 함수, class로 찾는 방법  
#print(soup.find(attrs={"class":"box_type_l"}))
# find,find_all, class로 찾는 방법
print(soup.find("tr",{"class":"type1"}))
type_tr = soup.find("tr",{"class":"type1"})
type_ths = soup.find("tr",{"class":"type1"})
print("th :",type_ths.th) #th : <th>순위</th> : 첫번째 만나는 th 태그를 찾아줌.
print(type_ths.find_all("th")) # 모든 th를 찾아줌
ths = type_tr.find_all("th")
for th in ths:
     print("제목 : ", th.text)


