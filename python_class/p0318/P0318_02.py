class Car: # 명사는 변수, 동사는 함수로 구현
     car_name = ''
     color = ''
     door = 0
     length = 0
     width = 0
     speed = 0  # 속도를 더한다는 동사의 개념

     def up_speed(self,s): # 클래스 내의 함수는 self를 꼭 넣어주어야함.
          self.speed += s 

          
c1 = Car()    
c1.car_name = '드뉴아반떼'
c1.color = 'white'
c1.door = 5
c1.length = 2000
c1.width = 1000
c1.up_speed(60) # 현재 speed에서 60을 더해 줌
c1.up_speed(40) # 현재 speed = 100      
c1.up_speed(50) # 현재 speed = 150
c1.speed(50) # 현재 speed = 50 
          
# # 영희의 차를 1대 생산, 색상은 green,나머지 동일,speed = 100으로 설정해서 출력
# car_name2 = '드뉴아반떼'
# color2 = 'green'
# door2 = 5
# length2 = 2000
# width2 = 1000
# speed2 = 100
# print(f'영희의 차 성능 : 색 : {color2}, 문 개수 : {door2}, 길이 : {length2}, 넓이 : {width2}, 속도 : {speed2} ')

c2 = Car()    
c2.car_name = '드뉴아반떼'
c2.color = 'green'
c2.door = 5
c2.length = 2000
c2.width = 1000
c2.up_speed(60) # 현재 speed에서 60을 더해 줌



# #반장
# car_name3 = '디올뉴그랜저'
# color3 = 'white pearl'
# door3 = 5
# length3 = 2500
# width3 = 1400
# speed3 = 150

# print('반장의 차 성능 :',car_name3, color3, door3,length3, width3, speed3)

c3 = Car()    
c3.car_name = '디올뉴그랜저'
c3.color = 'white pearl'
c3.door = 5
c3.length = 2500
c3.width = 1400
c3.up_speed(150) # 현재 speed에서 60을 더해 줌


print('철수 성능 :', c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.up_speed)
print('영희 성능 :',c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.up_speed)
print('반장 성능 :',c3.car_name,c3.color,c3.door,c3.length,c3.width,c3.up_speed)


# a_speed = 0
# def aaa_speed(a):
#      a_speed += a




# # 철수의 차를 1대 생산
# car_name = '드뉴아반떼'
# color = 'white'
# door = 5
# length = 2000
# width = 1000
# speed = 0

# color = 'red'
# speed = 60
# print('철수의 차 성능 : ', color,door, length, width,speed)

