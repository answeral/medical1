# 변수와 함수를 모아서 사용, 함수를 계속해서 사용 가능, 코드 사용 중복방지
# class 속성은 변수(명사), 함수(동사)
# 변수 (- 정수, 실수 , bool ,str ) , 리스트, 딕셔너리 , 클래스
# 객체 선언( 인스턴스 선언) ex) mycar1 = Car(), s1 =Student() - 변수 선언이랑 같은 의미
# 호출 방법 - mycar1.color = 'white',  s1.kor = 100, c1.up_speeds(30), c1.up_speed()
# 클래스는 대문자, 함수는 소문자로 할 것

# 생성자 - 미리 만들어서, 소스코드를 줄일 수 있음 ex)def __init__(self) , def __str__(self),
# # self를 꼭 붙여야지 클래스 변수에 값이 저장이 됨.  

# 클래스 변수 -공통으로 사용, 공통으로 사용해서 객체선언시 클래스변수 값을 바꾼다면 전부 바뀜. 
# # 클래스명.변수명 ex) Car.count             

class Car:
     count = 0 # 클래스 변수 인식        # color = '' - #init 선언시 없어도 됨
                                        # speed = 0
    
     def __init__(self, color='', speed=0): # 생성자함수 #키워드변수 - color = '', speed = 0처럼 값을 미리 정해놓음
          self.color = color # init 안에 변수 선언 - 인스턴스 변수
          self.speed = speed
          # 클래스 변수 선언
          # Car.count = 0
     
# class 사용하기 위해서는 인스턴스 선언하고 사용
c1 = Car() #인스턴스선언
c1.color = 'white' 
print("c1 color : ", c1.color)
print("c1.speed : ", c1.speed)
Car.count =10  # 클래스 변수
print("c1 count : ", c1.count)

c2 = Car()
c2.color = 'red'
print("c2 color : ", c2.color)
print("c1 color : ", c1.color)
print("c2 count : ",  c2.count) # 값을 찍을 때는 c2.count해도 되지만 (1)
Car.count = 200
print("c1 count : ", Car.count)
print("c2 count : ", Car.count) 
c2.door = 4 #변수 설정은 안되어있어도 선언은 됨. / 좋은 코드는 아님/ - 파이썬은 변수 선언을 자유롭게 해놓음
print("c2 door : ",c2.door)
c2.count = 1      # 기존 클래스 변수를 지우고 인스턴스 변수를 다시 생성 (c2만 값이 다름) /이렇게 하지 말 것/(2)
print(c2.count) #1
print(c1.count) #200
c3 =Car()
print(c3.count) #200

# 클래스의 상속 -  !기존 것을 물려받으면서! 추가적인 부분까지 있는 !새로운 클래스를 만드는 것!(많이 사용X)