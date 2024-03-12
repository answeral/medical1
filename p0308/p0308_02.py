import random
card_list = []
shape_list = ['spade','diamond','heart','clover'] #스페이드 다이아 하트 클로버
num_list = [0]*13 
for i in range(1,14):
     num_list[i-1] = i 

num_list[0]='A' # A K Q J 10~2 순으로 
num_list[10]='J'
num_list[11]='Q'
num_list[12]='K'

print(shape_list)
print(num_list)
#카드 1세트 구현해서 출력 총 52장
card_list=[[0]*2 for i in range(52)]
cnt = 0
for i in shape_list: # 0 1 2 3 ['spade','diamond','heart','clover']
     for j in range(13): # 1 2 3 4 ... 52
          card_list[cnt] = [i,num_list[j]]
          cnt += 1

# 출력 -> 모양: spade 번호 : 1

for i in shape_list:
     for j in range(13):
          card_list[cnt] ={'shape':i,'num':num_list[j]} #딕셔너리 형태로 변환
          cnt += 1
          
print(card_list['shape'],card_list['num'] )
          
          
          

# 카드 랜덤 섞기
random.shuffle(card_list)
arr_num = 0
while True:
     print(' 1. 카드1장 뽑기 ')
     print(' 2. 카드5장 뽑기 ')
     print(' 0. 종료 ')
     c_num = int(input('번호를 선택해주세요 >> '))
     print('현재 남은 카드: ',len(card_list)-arr_num) # len(card_list)52장 - arr_num
     if c_num == 1:
          print(card_list[arr_num])
          arr_num += 1
     elif c_num == 2:
          for i in range(5):
               print(card_list[arr_num])
               arr_num += 1
               





print(card_list)







