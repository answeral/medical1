import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

#print(soup.find("table",{"class":"type_5"})) #tbody가 자동으롤 붙어서 없을수도 있음 
t_table = soup.find("table",{"class":"type_5"}) #테이블의 모든 내용이 들어옴
trs = t_table.find_all("tr")
#print(trs)
trs[2]
print(trs[2])
tds =trs[2].find_all("td")
print(tds)
for td in tds:
     print((td.text).strip())


