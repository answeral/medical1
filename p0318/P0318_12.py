# car 클래스를 선언해서
# carNo, 변수는 color = 'white', door = 5, tire = 4 , speed 
# upspeed 함수를 호출하면 10씩 증가
#downspeed 함수 호출하면 -10씩 감소

#carCount 선언해서 클래스 변수 이용해서 숫자 증가 시키기
# c1   carNo = 1'white'5 4 0 ->speed가 30이 되게
# c2 carNo = 2'red' 5 4 0 -> speed가 100이 되게
# c3 carNo = 3'silver' 5 4 0 ->speed가 70이 되게
# car_list 추가

# car_list에 있는 모든 객체의 모든 color door tire speed를 모두 출력

class Car():
     carCount = 0
     carNo = 0
     def __init__(self, color = '',door = 5, tire = 4 , speed = 0 ) :
          
          self.color = color
          self.door = door
          self.tire = tire
          self.speed = speed
     
          Car.carCount += 1
          self.carNo = Car.carCount
          
     def upspeed(self):
          self.speed += 10
               
     def downspeed(self):
          self.speed -= 10
               
     def __str__(self):
          return f'{self.carNo},{self.color},{self.door},{self.tire},{self.speed}'
          
car_list = []          

c1 = Car('white',5,4,0)

for i in range(3): 
    c1.upspeed()


car_list.append(c1)
car_list.append(c1.upspeed)




c2 = Car('red',5,4,0)
for i in range(10):
     c2.upspeed()
car_list.append(c2)
car_list.append(c2.upspeed)


c3 = Car('silver',5,4,0)
for i in range(7):
     c3.upspeed()
     
car_list.append(c3)
car_list.append(c3.upspeed)


print(car_list)