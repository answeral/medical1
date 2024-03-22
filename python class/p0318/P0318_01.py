# 클래스 : 사용자정의변수 - 함수도 포함 # 객체지향언어 
# 변수와 함수를 모두 넣을 수 있음      
# 클래스는 첫글자를 대문자로 사용
# 클래스 : 설계도

# 클래스 선언
class Car : # 클래스 선언 시 일률적인 공간에 저장 - 찾는 시간이 절약됨.
     color = 'white'
     door = 5
     length = 4710
     width = 1800
     displace = 1600
     speed = 0
     

     def upSpeed(self, sp):
          self.speed += sp
          
     def downSpeed(self,sp):
          self.speed -= sp


# 객체 선언을 할 때마다 제품(Car)이 한 개씩 생산이 됨
c1 = Car() # 객체선언     
print('색상 :' ,  c1.color)
c1. color = 'red'
print('변경 후 색상 :' ,  c1.color)

c2 = Car()     # c1과 c2는 전혀 다른 선언
print('c2 색상 :', c2.color)






# 함수 선언
def func():
     pass

c1 = Car() # 클래스 객체선언 : Car 클래스에 있는 모든 변수를 사용함
# print(c1.color)
c2 = Car()
c3 = Car()
# 변수 선언시 각각의 여분 공간에 저장 되어짐. 
a_l = 4710
a_w = 1800
a_d = 1600

a_l2 = 4710
a_w2 = 1800
a_d2 = 1600

a_l3 = 4710
a_w3 = 1800
a_d3 = 1600




'''
a = 120
b = 1
# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,120]
print(a+1)
print(a+1)
print(a+1)
print(a+1)
print(a+1)
print(a+1)
print(a+1)
print(a+1)
print(a+1)
print(a+1)

for i in range(1,11):
     a = i+1
     print(a)
'''