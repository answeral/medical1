# 반복문 
print('안녕하세요'*5)

print('안녕하세요')
'''
for 변수 in 반복가능한데이터:
    수행할 문장
'''
# 순차적으로 커질 때 range를 사용한다.
for i in range(0,5,1): #range(시작값, 끝값+1, 증가값)
                       # i가 1,2,3,4
    print(i,'안녕') 

#0 안녕
# 1 안녕
# 2 안녕
# 3 안녕
# 4 안녕 
    
for i in range(0,5): #증가값이 1인 경우 생략가능
    print(i, 'hi')

# 0 hi
# 1 hi
# 2 hi
# 3 hi
# 4 hi  
    
for i in range(4): #n번 반복할 경우 range(n)을 사용할 수 있다
    print('hello')

for _ in range(2): # i를 사용하지 않을 경우 _를 사용할 수 있다.
    print('반갑습니다') 
    
for i in range(5): #5번 반복해라
    num = int(input('숫자를 입력해주세요 >> '))
    print('입력하신 숫자는 {} 입니다'.format(num))
    
# 숫자 반복해서 5번 입력하게 결과나옴    
    
# i , j 카운터 변수 K , l ... i랑 j를 자주 사용
# 카운터변수는 반복 실행 될때마다 현재 실행 횟수에 해당하는 숫자가
# 들어간다. 가장 처음은 실행한 적이 없으므로 0이 된다.

for i in range(3): #증가값이 1인 경우 생략 # 0 1 2
    print(i)
    
str1 = '안녕하세요'
for i in str1:
    print(i)
    
# 1에서부터 15까지 출력해보세여

for i in range(1,16,1):
 print(i, end = '')

for i in range(15):
 print(i+1, end = '')
print()


for i in range(13):
    print(i, end ='')
print()

for i in range(13):
    print(i+1, end = '')
print()


# 10을 4번 반복해서 출력해주세요
for i in range(4):
    print(10)
    
#helloworld를 6번 반복해서 출력
for i in range (6):
    print('helloworld')    
    
for i in range(6):
    print(i+1,'helloworld')

#4. 1-100사이의 2의 배수를 출력
for i in range (2,100,2):
 print(i, end=' ')
 

print( ) # 줄바꿈된 빈공백
#5. 1-100사이의 5의 배수를 출력
for i in range(5,100,5):
 print(i, end = '')