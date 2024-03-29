import random
# 클래스 선언 - 설계도

class Card:
     kind = ''
     number = ''
     
     def __init__(self,kind,number):
          self.kind = kind
          self.number = number
          
# 52장
# 모양 SPADE, DIAMOND, HEART, CLOVER
# 숫자 1 2 3 4 5 6 7 8 9 10 11 12 13
kind_list = ["SPADE","DIAMOND","HEART","CLOVER"]
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_list = []

def random_one():
     num = random.randint(0,51)
     # print('랜덤카드 1장 : ',card_list[num].kind,card_list[num].number)
     return card_list[num]

# 52장 카드 생성
for i in range(4):
     for j in range(12):
          card_list.append(Card(kind_list[i],number_list[j]))
          
# 52장 카드 출력      
# for i in range(52):
#      print('카드 : 'card_list[i].kind, card_list[i].number)


# 랜덤으로 1장 뽑기 출력
random_one()

# 랜덤카드 5장을 뽑는데, 중복이 되지 않게
# 1. 0-51 순차적으로 나온 것을 랜덤섞기 후, 뽑으면 중복없이 5장
# 2. 5장을 랜덤으로 뽑기
# 3. 1장 뽑고 기존에 있는 카드와 비교해서 다시 뽑는 방법
print('-'*60)

# 1 card_list shuffle
random.shuffle(card_list)
for i in range(5):
     
     print('1번 랜덤섞기 카드 :',card_list[i].kind,card_list[i].number)
     
print('-'*60)     

# 2. card_list sample 5
ran_list = random.sample(card_list,5) # ran_list
for i in ran_list:
     print('2번 랜덤섞기 카드 :', i.kind, i.number)

print('-'*60)

# 3. temp_list 저장장소를 1개 만들고, 랜덤뽑기 1장의 카드를 저장장소의 리스트와 비교
temp_list = []
print(len(temp_list))
cnt = 0
while True:
     if cnt == 5: break # 랜덤뽑기 카드가 5장일 경우 종료 
     c = random_one()   # 랜덤카드 1장을 뽑기   
     for i in temp_list:
          if c.kind == i.kind and c.number == i.number: # 같은 카드가 있으면 다음으로 진행
               continue
     
     # 중복 카드가 없으면 추가
     temp_list.append(c)
     cnt += 1
     
for i in temp_list:
     print('랜덤뽑기카드 :' , i.kind,i.number)




for i in range(5):
     c = random_one()
     print('랜덤1장뽑기 :',c.kind,c.number)









