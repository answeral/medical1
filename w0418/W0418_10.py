import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

t_table = soup.find("table",{"class":"type_5"})
#print(t_table)

type_tr = soup.find("tr",{"class":"type1"})
#print(type_tr)

trs = t_table.find_all("tr")
#print(trs)

tds = t_table.find_all("td")
# print(tds)

# print(trs[2].text) #2-14

# for trs in range(2,15):
#      print(trs)
     
for i in trs[2:15]:
     print(i.text)
     
# print(tds)

