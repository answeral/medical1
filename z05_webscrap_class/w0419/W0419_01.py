import requests
from bs4 import BeautifulSoup

url="https://www.google.com/search?q=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC&oq=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIGCAIQABgeMggIAxAAGA8YHjIICAQQABgFGB4yCAgFEAAYCBgeMggIBhAAGAgYHjIICAcQABgIGB4yCAgIEAAYCBgeMggICRAAGAgYHtIBCTY0MTFqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res =requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#----------------------------------------------------------------------------------------
# with open('google0419.html','w',encoding="utf8") as f:
#      f.write(soup.prettify())

# print(soup)

title = soup.title.text
print("title : ",title)

dollar = soup.find("input",{"class":"lWzCpb ZEB7Fb"})

print(dollar.attrs)
print("미국달러 :" , dollar["value"])

won = soup.find("input",{"class":"lWzCpb a61j6"})
print(won.attrs)
print("한국 원화 :" ,won["value"])

