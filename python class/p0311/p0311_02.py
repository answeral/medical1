# csv형태는 리스트랑 비슷, 한 줄이 데이터, ','로 구분
students = "1,'홍길동',100,100,99,299,99.67,1"
s_list = students.split() # 쉼표로 구분되어 있는 것은 split으로 만들기
print(s_list) #["1,'홍길동',100,100,99,299,99.67,1"] 