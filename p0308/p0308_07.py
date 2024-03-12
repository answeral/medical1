import random

# 주택복권
# 1조740
# 2조711
##6자리
# 1-9조
# 0-999999
#랜덤으로 로또 번호 만들기
first_num = random.randint(1,9)
last_num = random.randint(0,999999)

lotto = str(first_num)+'조'+'{:06d}'.format(last_num)
print(lotto)


lotto = []
l_input = input('복권을 입력하세요 (예:1조740042) >> ')

#입력한 개수와 비교해서 몇 개를 맞았는지 출력하기 예:2조 711000 1개 번호가 맞았습니다.
cnt = 0

for i in range (len(lotto)): # 0 1 2 3 4
     if lotto[i] == l_input[i]:
          cnt += 1
print('맞는 개수 : ', cnt-1 )

