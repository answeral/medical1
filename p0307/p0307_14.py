# 두 리스트를 묶을 때 zip을 사용
list = [1,2,3]
# alist = list # 두 리스트는 같음, 동기화가 됨 #공간을 같이 씀 # 얕은 복사 [100,2,3]
alist = [*list]#깊은 복사 [1,2,3]
alist = list[:]

list[0] = 100

print(alist)

a= 100
b = a
a= 10
print(b) # b= 100