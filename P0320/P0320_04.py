class Student:

     def __init__(self,name,total):
          self.name = name
          self.total = total
     def __str__(self):
          return f'이름 : {self.name}, 총점 : {self.total}'

     def __del__(self):
          return "클래스가 소멸 될 때 실행" # 사용 안하면 소멸
     
     def __add__(self,s): # 더해지는게 있다면 가장 먼저 호출
          return self.total+ s.total
     
     def __gt__(self,s): # 크거나 같다라고 비교할때
          return self.total>s.total 
     
     def __eq__(self,s):
          return self.name == s.name and self.total == s.total
               
          
#-------------------------------------------
s1 = Student('홍길동',100) # 객체 선언시 클래스가 생성
s2 = Student('유관순',90)
s3 = Student('이순신',80)
s4 = Student('홍길동',100)

print(s1) # 클래스를 출력할 때, str이 없으면 주소값 프린트, str존재하면 호출
print(s1+s2) # 클래스를 더하기 할 때, add함수 호출

print(s1>s2) # 클래스 간 비교는 불가능 하지만, __gt__메소드를 생성하면 호출 #True
print(s2<s3) # False

print(s1) # 주소값 0x000001F4164A65A0>
print(s4) # 주소값 0x000001F4164A64E0> 
print("s1 == s4 : ",s1 == s4) # 함수가 없다면, False라고 뜸->주소값이 같지 않아서 #함수존재 O : True
print("s1 == s2 : ",s1 == s2) # 함수 존재 O : False

