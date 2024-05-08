import requests
from bs4 import BeautifulSoup

url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent"
# url = "https://www.coupang.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res =requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#----------------------------------------------------------------------------------------
# with open("coupang.html","w",encoding="utf8") as f:
#      f.write(soup.prettify())
# print("완료")

print("제목 : ",soup.find("div",{"class":"name"}).text)
print("가격 : ",soup.find("strong",{"class":"price-value"}).text)
print("평점 : ",soup.find("em",{"class":"rating"}).text)
print("평점 개수 : ",soup.find("span",{"class":"rating-total-count"}).text)

uls = soup.find("ul",{"class":"search-product-list"})
# print(len(soup.find("ul",{"class":"search-product-list"}).find_all("li"))) #63게
lis = uls.find_all("li")
# print("리스트 개수 : ",len(lis))
# print(uls)
# print(lis)
# print("리스트 : ",lis[1].text)
# for ul in uls[0:10]:
#      print(ul)
# for li in lis[1:11]:
#      print(li[i])
#      print('-'*30)

for i,li in enumerate(lis[0:20]):
     #광고상품제외
     if 'search-product__ad-badge' in li['class']  :
          continue
     # 평점이 5.0이상 - 문자와 숫자 비교 에러
     if float(li.find("em",{"class":"rating"}).text) <5.0:
          continue
     #평가 인원수 200명 이상 출력 / [1:-1] : (500)에서 ()를 뺌
     if int(li.find("span",{"class":"rating-total-count"}).text[1:-1])<200:
          continue
     print("[",i+1,"번째 상품]")
     print("li class :", li["class"])
     #왼쪽, 오른쪽 공백 제거
     print("제목 : ",li.find("div",{"class":"name"}).text.strip())
     print("가격 : ",li.find("strong",{"class":"price-value"}).text)
     print("평점 : ",li.find("em",{"class":"rating"}).text)
     print("평가인원수 : ",li.find("span",{"class":"rating-total-count"}).text[1:-1])
     print('-'*60)
          