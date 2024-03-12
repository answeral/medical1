from random import*
# 변수 10개
lotto = []
#입력받은 숫자 6개
mynum = [1,5,6,9,8,7]
#로또 번호 생성하기


for i in range(6):
    n = randint(1,10)   #중복발생 될 가능성 있음
    lotto.append(n)     # if n not in lotto
                        # lotto.append(n) # 중복이 발생해서 5개만 들어갈 수 있음
# print(lotto)

num = [1,2,3,4,5,6,7,8,9,10] # 중복이 없다. 1-10까지다
for i in range(10):
    tmp = randint(0,9) #0번방에서 9번방까지 0-9까지 랜덤한 숫자 생성
    # print(tmp) 
    num[0], num[tmp] = num[tmp],num[0]
print(num) #[2, 1, 9, 4, 5, 7, 8, 6, 3, 10] # 중복 없는 숫자들이 발생

for i in range(6):
    lotto.append(num[i])
print(lotto) #6자리의 중복없는 랜덤한 숫자

ok = []
for i in range(len(mynum)):
    # print(mynum[i]) #리스트에 있는 숫자 출력
    if mynum[i] in lotto:
        ok.append(mynum[i])
print(ok)


# 1-45까지의 숫자를 넣어서
# 랜덤하게 
# 입력을 1-45사이의 숫자를 입력 받음 (6개)
# 1-45 사이의 랜덤한 숫자 6자리를 저장
#입력한 숫자와 랜덤숫자를 비교

lotto = []
mynum = []
for i in range(6):
  n = int(input('{}번째 숫자를 입력하세요(1-45중)>>'.format(i+1)))
  mynum.append(n)
l= [] 
for i in range(1,46):
  l.append(i)

for i in range(200):
    tmp = randint(0,44)
    l[0],l[tmp] = l[tmp], l[0]  # l에 들어가있는 숫자들 랜덤으로 200번 섞음