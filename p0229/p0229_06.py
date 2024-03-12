# continue 예제
# 1 -100까지 합계를 구하는데 3의 배수는 제외하고 더하기
# while문이나 for문 사용

i = 0
s = 0
while i <100:
    i += 1
    if i % 3 == 0:
        continue
    s += i
print(s)    #3367

s1 = 0
for i in range(1,101):
    if i % 3 ==0:
        continue
    s1 += i
print(s1) #3367
    