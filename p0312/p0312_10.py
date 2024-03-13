import random

# 카드 종류 : SPADE, DIAMOND, HEART, CLOVER 4종류
# 카드 숫자 : A,2,3,4,5,6,7,8,9,10, J, Q, K 13장
# 총 52장


def card_creat():
     # cnt = 0
     # for i in shape_list: # 0 1 2 3 ['spade','diamond','heart','clover']
     #      for j in range(13): # 1 2 3 4 ... 52
     #           card_list[cnt] = [i,card_num[j]]
     #           cnt += 1
     pass
   

def card_shuffle():
     # random.shuffle()
     pass
def card_share():
     # for i in range(5):
     #      card_sh.append(card_list)
     # print(card_sh)
     pass
          
          

def card_print():
     pass

# card_list = [[0]*2 for i in range(52)]
# shape_list = ['spaed','diamond','heart','clover']
# card_num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# card_sh = [] 

c_shape = ['SPADE','DIAMOND','HEART','CLOVER']
c_number = [0]*13
for i in range(13):
     c_number[i] = i+1
     
c_number[0] = 'A'
c_number[11] = 'J'
c_number[12] = 'Q'
c_number[13] = 'K'





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
          card_creat()
          print()
          
     elif choice == 2:
          card_shuffle()
          print()
          
     elif choice == 3:
          card_share()
          print()
          
          
     elif choice == 4:
          card_print()
          
     else :
          print('종료합니다')
          break