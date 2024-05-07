import requests
url = "https://www.google.com"
res = requests.get(url)
res.raise_for_status()

print("페이지의 글자 수 : ",len(res.text))
print("[웹페이지 소스코드]")
print(res.text) # 소스를 가져옴. 타입: str

#파일저장
with open('google.html','w',encoding="utf-8") as f:
     f.write(res.text)
     
