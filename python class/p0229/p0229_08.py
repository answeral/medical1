# 1-100까지 더하는데 ,
# 총합이 100이 넘었을때 수를 출력하세요 #break
# 1 +2 +3 +...+100까지 더하는 도중 100이 넘는 순간의 수를 출력

i = 0
s = 0
while i <100:
    i += 1
    s += i
    if s > 100:
        break

print(i)
print(s)  

s1 = 0
for i in range(1,101):
    s1 += i
    if s1 > 100:
        break

print(i)
print(s1)
    
    