#리스트
# 1-10까지 입력하기
list=[]
#for문을 활용한 리스트 기본문법
for i in range(10):
     list.append(i+1)
# print(list)
list = [i for i in range(1,11)]
print(list)

list = [0]*10
for i in range(10):
     list[i] = i+1
print(list)