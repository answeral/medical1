import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
s_all = soup.find("div",{"class":"box_type_l"})
# with open ("stock.html","w",encoding='utf8') as f:
#      f.write(soup.prettify())
tr_list = s_all.find_all("tr")
samsung = tr_list[2]
td_list = samsung.find_all("td")
print('순위:',td_list[0].text)
print('종목:',td_list[1].find("a").text)
print('검색비율:',td_list[2].text)
print('현제가:',td_list[3].text)
# print(samsung.find_all("td"))
# print(len(tr_list))
# print(tr_list[2])





# print(soup.prettify())
# print(soup.a.attrs)
# print(soup.a["href"])
# print(soup.find,{"td":"title"})
# samsung_list  = soup.find('td',{"class":"samsung_list"})
# print(samsung_list)
# s_list = samsung_list.find_all("td")
# print(s_list)


