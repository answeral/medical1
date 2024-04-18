#//12,1,2월 겨울 3,4,5월 봄 6,7,8 여름 9,10,11 가을  //1월- 겨울입니다.

season3 = input("월을 입력해주세요")
season2 = season3[0:-1]
season = int(season2)
if (1<= season <=2) or (season==12):
    print("겨울입니다")
elif (3<=season<=5):
      print("봄입니다")  
elif (6<=season<=8):
      print("여름입니다")
elif (9<=season<=11):
      print("가을입니다")