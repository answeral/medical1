# --------------------------------기본구문-----------------------------
import requests # 웹정보,소스 요청 라이브러리
#url ="http://www.google.com"
url = "https://www.melon/com"
res = requests.get(url)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
#print(res) #<Response [200]> : 정상
#---------------------------------------------------------------------------

#if res.status_code == requests.codes.ok: # 응답코드 :200 
if res.status_code == 200: # 응답코드 :200 
     print("정상적인 페이지 호출")
else:
     print("접근할 수 없음 [에러코드 : ",res.status_code,"]")
     
