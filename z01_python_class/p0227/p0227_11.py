from random import *

n1 = randrange(1,10) # 1-9사이의 정수
n2 = randrange(10) # 0-10 사이의 정수
n3 = randint(1,10) # 1-10 사이의 정수    

print(n1,n2,n3)

lotto = []
#lotto에 랜덤한 숫자 6개를 넣어보기 1-10까지의
for i in range(6):
 a = randint(1,10) #위에 있는 n3는 한 번만 선언, for구문 안에 넣어야 6번 반복 선언. 
 lotto.append(a)
print(lotto) 

# for i in range(6):
#     print(randint(1,10), end ='')

mymum = []
#내가 직접 입력한 숫자 6개 입력하기
for i in range(6):
    n = int(input('숫자를 입력하세요 >> '))
    mymum.append(n)
print(mymum)

