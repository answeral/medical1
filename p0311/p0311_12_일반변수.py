# 함수 선언
def stu_update(stuNo,name,kor, eng, math): #지역변수
     name = '유관순'
     total = kor +eng+ math # 지역변수
     avg = total/3
     stuNo = 2
     return stuNo, name,  total, avg # 순서 중요

# 프로그램 구현
stuNo = 1
name = '홍길동'
kor = 100
eng = 100
math = 100
total = 0
avg = 0

# 함수호출
stuNo, name,  total, avg = stu_update(stuNo,name,kor, eng, math) # 전역변수 # 순서 중요


print('학생1 :',stuNo,name,kor,eng,math, total, avg) # 학생1 : 1 홍길동 100 100 100 300 100.0


