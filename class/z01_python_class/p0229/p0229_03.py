# 반복문 for문 while문
'''
for i in range(시작, 끝+1, 증감값)
    수행할 문장

while 조건식:   # 이 조건이 참일때
    실행할 문장
    
변수 = 시작값
while 변수 < 끝값 : # 이 조건이 참일때
    반복구문
    변수 = 변수 +증가값 # i = i + 1

'''

# for문으로 안녕하세요 3번
for i in range(3):
    print('for : 안녕하세요')
    
# while문으로 작성
i = 0
while i < 3:
    print('while : 안녕하세요')
    i = i + 1
    
#for 문으로 0 에서 10까지
for i in range(0,11):
    print(i, end='\t')
print()
# while 문을 0에서 10까지
i = 0
while i < 11: #참 일 동안만 반복문 시행
    print(i)
    i += 1
print()
# while을 사용해서

# 1-10사이의 3의 배수를 출력하기 3,6,9
i = 1
while i < 11:
    i +=1
    if i % 3 == 0: 
     print(i)

# 1-100사이의 홀수 출력
i = 0
while i < 100: #(0,1,2,3,4,5,6,7,8,9,10...99)
    i += 1 
    if i % 2 == 1:
        print(i, end = ',')
print()
# 1-100까지의 합을 구해보기
s = 0
for i in range(1,101):
    s += i
print(s)

s1 = 0
i = 1
while i <= 100:
    i +=1 
    s1 +=i
print(s1)
# i = 0
# s = 0
# while i <100:
#     i +=1
#     s +=1
# print(s) 
'''
#while 조건문이 참인 경우 반복
# 때문에 while True 무조건 참이기 때문이 무한히 반복됨
# 무한 루프에 들어가면 control + c 를 눌러서 강제종료

# while문을 사용할 때 조건문을 잘 만드는게 중요하다
while True: #무한히 반복시키고자 할 때 사용
    print('z',end = '')
   ''' 


# break, continue
# break 반복문을 빠져나와서 다음단계를 수행한다.
n = 0
while n < 100: # n = 0, n = 1, n =2, n=3 n =4 
    print(n)
    n = n + 1
    if n == 4:
        break

    print('-----------')

breakletter = input('중단할 문자를 입력하세요 >> ')
for letter in 'python':
    if letter == breakletter:
        break
    print(letter)
    
while True:
    n = input('숫자를 입력해주세요(종료:0) >>')
    print(n)
    if n == '0':
        print('종료되었습니다  ')
        break
