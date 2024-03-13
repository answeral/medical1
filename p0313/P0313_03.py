# 1~100랜덤으로 숫자 1개 생성
# 입력한 숫자보다 크면 작은수를 입력하시오
# 입력한 숫자보다 작으면 큰수를 입력하시오.라고 멘트가 나오게 
# 정답을 맞추면

# 총 입력한 횟수 : ex) 7회 시도 
# 현재까지 입력한 숫자 ex)1,2,3,4,5,6
# 현재까지 입력했던 숫자를 모두 출력하시오

import random
ran_num = random.randint(1,101)
in_num = 0  
cnt = 1
input_nums = []
while True:
     print('[ 랜덤숫자 맞추기 게임 ]')
     in_num = int(input(f'{cnt}번째 도전 : "1-100까지의 숫자를 입력해주세요. >> '))
     input_nums.append(in_num)
     
     if ran_num > in_num:
          print('입력하신 숫자보다 큰 수를 입력하세요.')
     elif ran_num < in_num :
          print('입력하신 숫자보다 작은 수를 입력하세요.')
     else:
          print('정답입니다')
          break 
     cnt +=1
     
print(f'총 입력한 횟수 : {cnt}')
print(f'현재까지 입력한 숫자 :{input_nums}')
      