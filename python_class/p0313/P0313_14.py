import random
c_shape = ['SPADE','DIAMOND','HEART','CLOVER']
c_number = [0]*13
for i in range(13):
     c_number[i] = i+1
     
c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
out_num = []
#랜덤으로 숫자 2개를 뽑아서 출력하라
random.sample(c_number,2)
a = random.sample(c_number,2)
print(a)
# 랜덤숫자가 어디 방에 있는지 출력
for i in a:
     print(i, '위치')
# 큰수 :8 작은수 : 3