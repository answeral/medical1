#반복문
'''
for 변수 in range(시작값, 끝값+1, 증가값)
'''
for i in range(3):
    print(i, '안녕')
    
    # i = 0 일 때
    # i = 1 일 때
    # i = 2 일 때
    
for i in range(3): # i = 0,1,2 # 순차적으로 증가 
    print(i)

for i in range(100):
 print(i +1, end = ' ')
 
sum = 0
for i in range (1,6,1):
    sum += i
print()  
# 숫자 한 개를 입력받아서 1 부터 입력한 수까지의 합을 구하세요.
n1 = int(input('숫자를 입력해주세요 >>'))
s1 = 0 # 총합을 넣을 변수 선언
for i in range(1,n1+1):
    s1 += i
print('{}부터 {}까지의 총합은 {}입니다.'.format(1,n1,s1))
    
#짝수의 합만 구하기 (2 ~100)
t1 = 0
for i in range(1,101):
    if i % 2 ==0:
        t1 += i # t1=t1+i # i=2 i=4 i= 6...
print('짝수의 합은 {}입니다.'.format(t1))
        
# 1-10까지의 곱
ax = 1
for i in range(1,11):
    ax = ax*i 
print(ax)   
print(1*2*3*4*5*6*7*8*9*10)

