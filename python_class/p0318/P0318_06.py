class Student: #클래스 선언
     # stuNo = 0 # self (__init__) 했을때는 변수를 생략할 수 있음
     # stu_name = ''
     # kor = 0
     # eng = 0
     # math = 0
     # total = 0
     # avg = 0
     # rank = 0
     
 
     def __init__(self,stuNo=0, stu_name='', kor=0, eng=0, math=0):
          self.stuNo = stuNo
          self. stu_name = stu_name
          self. kor = kor
          self. eng = eng
          self. math = math
          self.total = kor + eng + math
          self.avg = float('{:.2f}'.format(self.total/3))
          self. rank = 1
          
          
s1 = Student(1,'홍길동',99,99,87)
print(f'1번학생 : {s1.stuNo},{s1.stu_name},{s1.kor},{s1.eng},{s1.math},{s1.total},{s1.avg},{s1.rank}')

s2 = Student(2,'유관순',98,93,87)
print(f'2번학생 : {s2.stuNo},{s2.stu_name},{s2.kor},{s2.eng},{s2.math},{s2.total},{s2.avg},{s2.rank}')


s3 = Student(3,'이순신', 88, 76, 30)
print(f'3번학생 : {s3.stuNo},{s3.stu_name},{s3.kor},{s3.eng},{s3.math},{s3.total},{s3.avg},{s3.rank}')

# 3명의 학생을 리스트에 추가
stu_list = [s1,s2,s3]
          
     

     
     

# 1. 홍길동 99,99,87,285,95.0,1 
# 2. 유관순 98,93,87,278,92.67,3
# 3. 이순신, 88, 76, 30. 194, 64.67 3


