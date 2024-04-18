
a, b = 10,8
a,b = b,a #숫자를 바꿀때

n1 =[0,1,2,3,4,5]
#    0의 위치와
#        3의 위치를 바꾸고 싶다
n1[0],n1[3] = n1[3],n1[0]
print(n1)
n1[2],n1[5] = n1[5],n1[2]
print(n1)

con = ['미국','영국','일본','중국','스페인']

con[1],con[3] = con[3],con[1]
print(con)
# 고정된 리스트에서 섞어주기
from random import*
n1 = [1,2,3,4,5,6,7,8,9,10] #랜덤하게 섞으면 #중복없이 섞임
#     0                  9
for i in range (10):
    tmp = randint(0,9) #랜덤한 인덱스
    n1[0],n1[tmp] = n1[tmp],n1[0] #숫자를 서로 섞어주기
    print(tmp)
    print(n1)
    



