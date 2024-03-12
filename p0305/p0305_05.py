#1-25까지 랜덤으로 섞은 다음
#2차원 리스트에 넣기
# [
#[1,2,3,4,5],
# [6,7,8,9,10],
# [11,12,13,14,15],
# [16,17,18,19,20],
# [21,22,23,24,25]
# ] # 2차원 리스트
#랜덤으로 섞어서 출력하기
import random

# 1. 1-25까지 리스트 생성
# 2. 랜덤으로 섞기
# 3. 2차원 리스트에 넣기
# num = random.randint(1,3)
# print(num)

#숫자맞추기 프로그램을 구현
#1-100까지 숫자 랜덤으로 생성, 숫자를 맞추는 프로그램
#몇번째에 맞췄는지 출력
num = random.randint(1,100)
cnt = 0
save_num = []
while True:
    in_num = int(input('1-100까지의 숫자를 입력하세요 >> '))
    save_num.append(in_num)
    if num > in_num:
        print('입력한 숫자보다 큽니다')
    elif num < in_num:
        print('입력한 숫자보다 작습니다')
    elif num == in_num:
        print('정답입니다')
        print('{}번째 도전을 하셨습니다'.format(cnt))
        break
    cnt += 1
print(save_num)




