# 리스트에 1 - 25까지 숫자를 리스트에 입력하시오
a = []
for i in range(0,25):
    a.append(i+1)
print(a)
print('-'*60)
# 1-25까지 2차원 리스트 생성
# [[1,2,3,4,5,],[6,7,8,9,10],...,[21,22,23,24,25]]

b =[] # 1차원 리스트
b_i = []# 2차원 리스트 
for i in range(0,25): #
    if (i+1)%5==0:
        b_i.append(i+1) #[1,2,3,4,5]
        b.append(b_i)
        b_i = []
        pass
    else:
        b_i.append(i+1)
print(b)