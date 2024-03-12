sum = 0
# n1 부터 n2까지의 합 ,n1,n2비교해서 작은 수를 n1에 넣기
n1 = int(input('첫번째 숫자를 입력하세요 >> '))
n2 = int(input('두번재 숫자를 입력하세요 >> '))
#만약에 n1이 n2보다 크다면 둘의 값을 바꿔라
if n1 > n2+1:
    n1,n2 = n2,n1
for i in range(n1,n2+1):
    sum += i
print('{}에서 {}까지의 합은 {}입니다'.format(n1,n2,sum))

# sum1 =0
# n1 = int(input('첫번째 숫자를 입력하세요 >> '))
# n2 = int(input('두번재 숫자를 입력하세요 >> '))
# n1, n2 = n2, n1    
# for i in range(n1, n2+1):
#     sum1 += i
# print('{}에서 {}까지의 합은 {}입니다'.format(n2,n1,sum1))  
    
odd_list = [] # 3. n1- n2까지의 홀수 값을 저장

n1 = int(input('첫번째 숫자를 입력해주세요 >> '))
n2 = int(input('두번째 숫자를 입력해주세요 >> '))
if n1 > n2:
    n1,n2 = n2,n1
for i in range(n1, n2+1):
    if i % 2 == 1:
        odd_list.append(i)
print(odd_list)



'''
a = 10
b = 8
a,b = b,a  
print('a',a)
print('b',b)
'''