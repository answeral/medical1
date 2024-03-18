class Card:
     kind = ''
     number = ''
     def __init__(self,kind,number):
          self.kind = kind
          self.number = number     

# 클래스를 이용해서 52장의 카드 생성 (보안 가능)
c_list = []

kind = ["SPADE","DIAMOND","HEART","CLOVER"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in range(4):
     for j in range(13):
          c = Card(kind[i],number[j])
          c_list.append(c)


for i in range(52):
     print('카드 출력 : ' , c_list[i].kind,c_list[i].number)


# # 리스트를 이용해서 52장의 카드 생성 (데이터 보안 불가능)

# c_list = []
# kind = ["SPADE","DIAMOND","HEART","CLOVER"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# for i in range(4):
#      for j in range(13):
#           c = [kind[i],number[j]] # 리스트를 생성해서 리스트에 추가
#           c_list.append(c)
          
# for i in range(4):
#      for j in range(13):
#           print("카드 출력 : " , kind[i],number[j])     

# # c1의 숫자를 5로 변경
# c1 = Card('SPADE',1) #객체 변수 선언
# c1.number = 5
# print(c1.kind,c1.number)
          

# # c2 "HEART" "A"
# # 모양을 다이아몬드로 변경 후 출력

# c2 = Card("HEART",1)
# c2.kind = "DIAMOND"
# print(c2.kind,c2.number)