import random

# 카드 종류 : SPADE, DIAMOND, HEART, CLOVER 4종류
# 카드 숫자 : A,2,3,4,5,6,7,8,9,10, J, Q, K 13장
# 총 52장


def card_creat(card_list):
     cnt = 0
     for i in shape_list: # 0 1 2 3 ['spade','diamond','heart','clover']
          for j in range(13): # 1 2 3 4 ... 52
               card_list[cnt] = [i,card_num[j]]
               cnt += 1
   
   

def card_shuffle(card_list):
     random.shuffle(card_list)

def card_share(card_list):
     for i in range(5):
          card_sh.append(card_list)
     print(card_sh)
     
          
          

def card_print():
     pass

card_list = [[0]*2 for i in range(52)]
shape_list = ['spaed','diamond','heart','clover']
card_num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_sh = [] 
while True:
     print(''*60)
     print('[ 카드 프로그램 ]')
     print('1.카드생성 ')
     print('2.카드섞기 ')
     print('3.카드 5장 나눠주기')
     print('4.카드 5장 확인하기 ')
     print(''*60)
     choice = int(input('원하는 번호를 입력하세요 >>'))

     if choice == 1:
          card_creat(card_list)
          print(card_list)
          
     elif choice == 2:
          card_shuffle(card_list)
          print(card_list)
          
     elif choice == 3:
          card_share(card_list)
          print(card_sh)
          
          
     elif choice == 4:
          card_print()
          
     else :
          print('종료합니다')
          break