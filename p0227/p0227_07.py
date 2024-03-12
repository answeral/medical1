# 1-5 까지의 합계를 구하세요 
sum = 1+ 2+ 3+ 4+ 5

total = 0 # t = 0
total = total +1 # t = 1
total = total +2 # t = 1+2
total = total +3 # t = 1+2+3
total = total +4 # t = 1+2+3+4
total = total +5 # t = 1+2+3+4+5

t =0 
for i in range(1,6,1): # i=1,2,3,4,5
    t = t + i  # t +=i
print(t)

# 1~ 10까지의 합을 구해라
n = 0 #초기값을 0이어야 더해져도 0에서부터 더해짐
for i in range(1,11):
    n = n+i
print('1부터 10까지의 합은 {} 입니다'.format(n) )

# 1~100까지의 합을 구해라
s = 0
for i in range(1,101):
    s += i
print('1부터 100까지의 합은 {} 입니다.'.format(s))    
   
# 입력한 수부터 입력한 수까지의 합을 구해보세요
n1 =int(input('첫번째 숫자를 입력해주세요 >>')) #1
n2 =int(input('두번째 숫자를 입력해주세요 >>')) #10
sum=0
for i in range(n1,n2+1):
 sum += i
print('합은 {}입니다.'.format(sum))

