import datetime #날짜 관련 기능을 가져옴
now = datetime.datetime.now() #오늘 날짜 시분초 가져옴
yeat = now.year

#시간을 사용해서
#지금이 오전이면 오전입니다. 오후면 오후입니다.
h = now.hour                               #변수 설정 잊지말기
if h > 12:
    print("현재는 오후입니다")
    print("현재는 {}시로 오후입니다".format(h))
    
else :
    print("현재는 오전입니다") 
    
h1 = now.hour

print("현재는 {}시입니다".format(h1))

# 1.짝수달입니다. 홀수달입니다.

m = now.month
if m%2 ==0:
  print ("짝수달입니다")
else :
    print("홀수달입니다")  
    
# 월-> 겨울입니다. 겨울이 아닙니다.

m = now.month
if 3 <= m <= 11:
    print("겨울이 아닙니다")
else :
    print ("겨울입니다")      

print(type(m)) #type을 알아보는 방법 :<class 'int'>

# print(now) #현재 시간의 시분초가 나옴

# print(now.year) 
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)