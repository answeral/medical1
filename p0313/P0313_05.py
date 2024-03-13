# import math

# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))
          # import random

# * : 모든 것
from random import * # random모듈명을 만들어도 됨.

          # #0.000000 - 0.9999999 # 랜덤 float 결과값 리턴
          # print(random.random())
print(random())
          # # 10 - 20 사이의 랜덤 float 결과값을 리턴
          # print(random.uniform(10,20))
print(uniform(10,20))
          # # 1-7 (8-1) 까지의 랜덤숫자 리턴 //8 포함하지않음!
          # print(random.randrange(1,8))

          # # 리스트 내에서 랜덤 1개 선택
          # print(random.choice([1,2,3,4,5]))
print(choice([1,2,3,4,5]))
          # # 리스트 내에서 랜덤 k개를 선택, k가 리스트의 개수보다 많으면 에러
          # print(random.sample([1,2,3,4,5], k=3))

          # #리스트의 요소를 랜덤으로 섞기
          # a_list = [1,2,3,4,5]
          # random.shuffle(a_list) # a_list 결과를 저장 # 파괴
          # print(a_list) # 출력

          # # 1-10사이에서 10 포함 /범위 내 랜덤 int를 선택 // range는 포함 X
          # print(random.randint(1,10))
          

