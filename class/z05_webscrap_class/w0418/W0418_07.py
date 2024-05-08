import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

type_tr = soup.find("tr",{"class":"type1"})

#next, find_next_sibiling(s)
print("th: ",type_tr.th) # 첫번째 th
print("find_next_sibiling : ",type_tr.th.find_next_sibling("th")) # 현재 th에서 다음 th를 찾아줌.
print("th next: ",type_tr.th.next) # 순위
print("th next next: ",type_tr.th.next.next) #\th
print("th next next next: ",type_tr.th.next.next.next) #다음 th 
print("find_next_sibiling : ",type_tr.th.find_next_siblings("th")) # 현재 th에서 다음 th 전부를 찾아줌.

#find_previous_sibling(s) 이전



