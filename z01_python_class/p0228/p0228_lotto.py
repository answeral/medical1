from random import *
# 1-45까지의 숫자를 넣어서
#랜덤하게 
# 1. 변수 선언 
mynum = [] # 입력을 1-45사이의 숫자를 입력 받음 (6개)
lotto = [] # 1-45 사이의 랜덤한 숫자 6자리를 저장
ok_num =[] #입력한 숫자와 랜덤숫자를 비교
'''
for i in range(6):
    n = int(input('{}번째 숫자를 입력해주세요 (1-45까지) >>'.format(i+1)))
    mynum.append(n)
print(mynum)
l =[]
for i in range(1,46): # 1~45
 tmp = randint[0,44]
 l.append(i)
 l[0],l[tmp] = l[tmp],l[0]
 
for i in range(6):
 lotto.append(l[i])
print(lotto)
''' 

# 2. 입력받은 숫자 6개
for i in range(6):
    n = int(input('{}번째 숫자를 입력해주세요 (1-45까지) >>'.format(i+1)))
    mynum.append(n)

#3. 로또번호 생성하기
# 1-45까지의 숫자리스트 만들기
l = []
for i in range(1,46):
    l.append(i) # 중복이 없는 1-45까지의 숫자가 들어있음. #l[0]=1

for i in range(200):
    tmp = randint(0,44) # 0번부터 44번까지 랜덤으로 섞은 것
    l[0],l[tmp]=l[tmp],l[0] #l의 0번이랑 랜덤 자리가 같다 = 랜덤으로 방을 섞음

for i in range(6):  #랜덤으로 섞인 l의 리스트를 6번 반복 ->
 lotto.append(l[i]) #랜덤하고 중복이 없는 숫자 6개 생성
    
print('로또숫자:{}'.format(lotto))

# lotto= [1,2,3,4,5,6]mynum = [7,8,9,10,11,12]
ok_num.append

for i in range(6): # i=0,1,2,3,4,5 
    if mynum[i] in lotto:
        ok_num.append(mynum[i])
print('당첨된 숫자 :{}'.format(ok_num))


