# 1-100까지의 합을 구하세요
'''
s = 0 # s = s+i
for i in range(1,101): # 1+2+3+4+5...+100
   s += i
print(s) 


# 짝수 = 2로 나눴을때 나머지가 0인 수
# 홀수 = 2로 나눴을때 나머지가 1인 수    
sum = 0

for i in range(1,101):
   if i% 2 ==0:
       sum += i
print(sum)

sum1 = 0

for i in range(1,101):
    if i % 2 == 1:
       sum1 += i
print(sum1) 
'''
s,s1,s2 = 0,0,0        # 한 번에 적용 할 수 있음
for i in range(1,101):
   s += i
   if i % 2 ==0:
    s1 += i
   elif i % 2==1:
    s2 += i
print(s)
print(s1)
print(s2)

# 1-10까지의 합

n=0
for i in range(1,11):
  n += i
print(n)

# num리스트 안에 있는 값들의 합
num =[1,2,3,4,5,6,7,8,9,10]
s = 0
for i in num:
    s += i
print(s)

s1 = 0
for i in range(len(num)):
   s1 += num[i]
print(s)   