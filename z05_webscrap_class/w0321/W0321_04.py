import requests
from bs4 import BeautifulSoup


url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res  = requests.get(url,headers=headers)
res.raise_for_status()

#print(res.text)

soup= BeautifulSoup(res.text,'lxml')
# print(soup)
#  파일저장
# with open ('test.html','w',encoding='utf8') as f:
#      f.write(soup.prettify())

print(soup.title) # soup 태그 사용해서 찾기# <title>랭킹뉴스 : 네이버 뉴스</title>
print(soup.title.text) # 랭킹뉴스 : 네이버 뉴스
print(soup.a)  # soup 태그 사용 # <span>메인 메뉴로 바로가기</span></a>

print(soup.a.attrs) # soup a태그의 속성값 출력
                    # <a href="#lnb" tabindex="1"><span>메인 메뉴로 바로가기</span></a>
                    # {'href': '#lnb', 'tabindex': '1'}

# print(soup.div) # <div id="wrap">
print(soup.a["href"])# soup a태그 선택속성값 출력#  #lnb

print(soup.find("div",{"id":"footer"})) #soup엥서 find태그, 속성값 모두 찾을 수 있음
# print(soup.find("div",attrs={"id":"footer"}))
