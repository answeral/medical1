# 리스트 변수명 = [요소1, 요소2 ,....,요소n]
# 요소가 될 수 있는 타입  : bool, float, string, list

fruits = ['딸기','사과','배','수박','귤']
#귤을 출력
print(fruits[-1])
print(fruits[4])
print([len(fruits)-1])
#리스트에 요소를 추가\
fruits.append(('포도'))
fruits.remove('딸기')
print(fruits) # 사과 배 수박 귤 포도
#리스트에서 3번째 삭제
del(fruits[3])

if '한라봉'in fruits:
    print('있음')
else:
    print('없음')
    
for i in fruits:
    print(i)
    
for i in range(len(fruits)):# i = 0,1,2,3,4
    print(fruits[2])
    
num = [[10,20,30],[100,200,300],[1,2,3] ]

for n in num:
    print(n)

for n in num:
    for a in n:
        print(a)
        
for i in range(len(num)):
    print(num[i])

for i in range(len(num)):
    for j in range(len(num[i])):
        print(num[i][j])
        
# 리스트에 숫자 넣을 때 한 줄로 표현하기
aa = []
for i in range(1,11):
    aa.append(i)
print(aa)

#[표현식 for 항목 in 리스트 if 조건문] 
a = [i for i in range(1,11)] #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0 for _ in range(10)]    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = [ [] for i in range(10)]

a = [ i * j for i in range(1,3) for j in range(1,3)] #[1, 2, 2, 4]

a = [i for i in range(100) if i%2 == 0] #짝수만 99까지
print(a)

b = [ i for i in range(1,11)] #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b)

c = [i+1 for i in b]
print(c) #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# 출력
#1. 홍길동 2. 유관순 3. 이순신 4. 강감찬 5. 김구
name = ['홍길동','유관순','이순신','강감찬','김구']
for i in range(len(name)): # 0123
    print('{}. {}'.format(i+1,name[i]))
print()

# 변수 한 개 더 필요 ->숫자  
i = 0
for n in name: #요소 1,2,3,4 #4번 돌게 됨
   i += 1
   print('{}.{}'.format(i,n))
print()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

#enumerate 함수
#index를 넣고 싶을 때 사용
for i, name in enumerate(name): #index - 0부터 시작
    print('{}.{}'.format(i+1,name))

#start를 넣으면 시작 인덱스를 지정할 수 있다
for i, name in enumerate(name, start = 1):
    print('{}.{}'.format(i,name))
    


name = ['딸기','사과','배','수박','귤']
for n in name: #이름만 알려줌
    print(n)
    
for i, n in enumerate(name): #있는 위치와 이름까지 알려줌
    print(i)
    print(n)