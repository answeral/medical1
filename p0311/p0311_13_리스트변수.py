# 함수 선언
def stu_update(student): #지역변수 -> 주소값이 저장되어 있음
     student[0] = 2
     student[1] = '유관순'
     student[5] = student[2] +student[3]+ student[4] # 지역변수
     student[6] = student[5]/3
   

# 프로그램 구현
student = [1,'홍길동',100,100,100,0,0] # 2개 이상의 변수 #주소값 저장되어 있음


# 함수호출
stu_update(student) 


print('학생1 :',student) # 학생1 : [2, '유관순', 100, 100, 100, 300, 100.0]

