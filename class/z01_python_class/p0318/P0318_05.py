# 클래스 선언 # 설계도
class Tv:
     channel = 0
     color = 'black'
     size = 65
     volume = 0
     
     def up_volume(self,volume):
          self.volume += volume
          
     def down_volume(self,volume):
          self.volume-= volume 

     def up_channel(self, channel):
          self.channel += channel

     def down_channel(self,channel):
          self.channel -= channel
# 철수 - 색상:'white',채널10변경, 2증가 
# 영희-'pink',채널7로 , 채널 5증가 
# 반장-'silver', 채널 1, 채널 3증가

t1 = Tv()
t1.channel = 10
t1. color = 'white'
t1. size = 65
t1. volume = 0
t1.up_channel(2)

print('철수 tv : ',t1.channel,t1.color,t1.size,t1.volume )

t2 =  Tv()
t2.channel = 7
t2.color = 'pink'
t2.size = 65
t2. volume = 0
t2.up_channel(5)

print('영희 tv : ', t2.channel,t2.color,t2.size,t2.volume)

t3 = Tv()
t3.channel = 1
t3.color = 'silver'
t3.size = 65
t3.volume = 0
t3.up_channel(3)

print('반장 tv : ', t3.channel,t3.color,t3.size,t3.volume)




class Tv:
     channel = 0
     color = ''
     size = 0
     volume = 0
     
     
     def __init__(self, channel =0, color ='', size = 0, volume = 0):
          self.channel = channel
          self.color = color
          self.size = size
          self.volume = volume
          self.channel += channel 

# 객체선언 # 제품설계
t11 = Tv(10,'white',65,0)
print('철수 tv :', t11.channel,t11.color,t11.size,t11.volume)
t11.up_channel(2)
          
t22 = Tv(7,'pink',65,0)
print('영희 tv :', t22.channel,t22.color,t22.size,t22.volume )
t22.up_channel(5)

t33 = Tv(1,'silver',65,0)
print('반장 tv: ',t33.channel,t33.color,t33.size,t33.volume)
t33.up_channel(1)         
# 철수 - 색상:'white',채널10변경, 2증가 
# 영희-'pink',채널7로 , 채널 5증가 
# 반장-'silver', 채널 1, 채널 3증가