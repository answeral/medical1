from typing import Any


class Card: # 4개의 변수 : kind, number, width, height
     
     width = 0 # 클래스변수
     height = 0 # 클래스변수
     kind = ''
     number = ''
     def __init__(self,kind,number) :
          self.kind = kind
          self.number = number
          Card.width = 100
          Card.height = 200
          

# 클래스 5개를 생성해서 kind = 모양, number = 1-13까지
card_list = []
for i in range(13):
     card_list.append(Card('SPADE',i+1))
     

# card_list.append(Card('SPADE','2'))
# card_list.append(Card("SPADE",'3'))
# card_list.append(Card("SPADE",'4'))
# card_list.append(Card("SPADE",'5'))
# ... 
# card_list.append(Card("SPADE",'10'))
# card_list.append(Card("SPADE",'J'))
# card_list.append(Card("SPADE",'Q'))
# card_list.append(Card("SPADE",'K'))
print('리스트 개수 : ',len(card_list))

for i in range(13):
     print('리스트 출력 : ', card_list[i].kind, card_list[i].number)
     




# 52장의 카드 생성
# shape = ['SPADE','DIAMOND',"HEART","CLOVER"]
# number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# Card_list = []


# for i in range(4):
#      for j in range(13):
#           c= Card(shape[i],number[j]) # 객체 선언
#           Card_list.append(c)     #리스트 추가
          
# for i in range(52):
#      # print('카드 출력 : ',Card_list[i]) #주소값으로 출력
#      c = Card_list[i] # Card 객체
#      print('카드 출력 :' ,c.kind, c.number)
