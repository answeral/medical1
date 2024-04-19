import requests
from bs4 import BeautifulSoup



year_rate_sum = [0]*3 # 년도별 평점 합계
sum=0
for y_i,y in enumerate(range(2021,2024)):
     url = f"https://search.daum.net/search?w=tot&q={y}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
     res =requests.get(url,headers =headers)

     res.raise_for_status()

     soup = BeautifulSoup(res.text,"lxml")

     movie_list = soup.find('ol',{"class":"movie_list"})
     print("-"*50)
     print(movie_list)
     
     # 30개
     m_list = movie_list.find_all("li")

     for i, m in enumerate(m_list):
          if i == 5:break
          print(f"[번호]: {i+1}")
          print('-'*100)
          print("제목 : ",m.find("div",{"class":"info_tit"}).a.text)
          print("평점 : ",m.find("em",{"class":"rate"}).text)
          
          # 연도별로 합구하기 2021 2022 2023 2024
          
          rate = float(m.find("em",{"class":"rate"}).text)
          sum += rate
          img_screen = m.find("img")["data-original-src"]
          print(img_screen)
          # # 이미지 저장부분
          # with open(f'movie_{y}_{i}.jpg',"wb",) as f:
          #      re_img = requests.get(img_screen)
          #      f.write(re_img.content) # 파일 이름의 내용을 저장
     print(f'{y}년도별 평점합계 :',sum)
     year_rate_sum[y_i] = sum
     # year_rate_avg[y_i] = float("{:.2f}".format(sum/5))
     # print("개수 : ",len(m_list))
     # print("년도별 펑점합계 : ",year_rate_sum)
     # print("년도별 펑점평균 : ",year_rate_avg)
     
     print('종료')
#print(movie_list)


# 파일 쓰기

# 파일 닫기

# 파일 쓰기

# 파일 닫기




