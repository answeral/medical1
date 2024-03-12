import datetime

now = datetime.datetime.now() #현재를 가져옴
print(now)

month = 3 # now. month # 현재 월
#현재가 봄 여름 가을 겨울
#12,1,2 겨울 3,4,5 봄 

if 12<= month <=2 : 
   print("겨울")
elif 3<= month <= 5:
    print("봄")
elif 6<= month <=8:
    print("여름")
else:
    print("가을")        