import requests
from bs4 import BeautifulSoup

url="https://browse.auction.co.kr/list?category=22160000"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res =requests.get(url,headers=headers)
res.raise_for_status()
# 데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")
# 파일저장
# print(soup.prettify())
# with open("yeogi.html","w",encoding="utf8") as f:
#      f.write(soup.prettify())

print("전체 : ",soup.find("div",{"class":"section--itemcard"}).text)

print("제목: ",soup.find("span",{"class":"text--title"}).text)
print("가격:",soup.find("span",{"class":"box__price-seller"}).text)
print("별점:",soup.find("li",{"class":"item awards"}).text)
print("후기 갯수:",soup.find("span",{"class":"text--reviewcnt"}).text)
print("이미지:")

