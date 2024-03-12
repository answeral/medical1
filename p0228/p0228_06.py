from random import*

n1 = randrange(1,11) # 1-10까지의 정수
 # 1-10까지의 정수

#랜덤한 숫자 6개 lotto리스트에 넣고
#내가 입력한 숫자 6개는 mynum리스트에 넣기
# 1.변수선언
# 중복 없이 숫자를 입력받고 싶다.
# f= ['딸기','포도']
# if '딸기' in f:
#     # print('딸기가 있습니다')
lotto = []
for i in range(6):
    n2 = randint(1,11)
    if n2 not in lotto: #만약애 랜덤숫자 n2가 리스트에 없다면
     lotto.append(n2)   #추가해라
print(lotto)

mynum = []
for i in range(6):
    n = int(input('{}번째 숫자를 입력해주세요 >> '.format(i+1)))
    mynum.append(n)
print(mynum)

