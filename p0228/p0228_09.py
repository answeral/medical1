# 중첩 for
# for 안에 for
for i in range(3):
    print('안녕') #print('i= ',i)
    for j in range(2):
      print('반가워')
      
      # i = 0 일때,           
        # j = 0, j =1 
      # i = 1 일때,
        #  j = 1, j=2  
      # i = 2 일때,
        #  j = 1, j=2   
        
        # 안녕  i
        # 반가워 j
        # 반가워 j
        # 안녕  i
        # 반가워 j
        # 반가워 j
        # 안녕  i
        # 반가워 j
        # 반가워 j







# for문을 사용해서 2단을 출력
# 2*1=2 2*2 =4 2*3= 6...2*9=18 순차적으로 증가 for문 사용
for i in range(1,10):
    print("{}*{}={}".format(2,i,2*i))

# 입력받아서 입력 받은 단을 출력하게 하기
n = int(input('숫자를 입력하세요 >> '))
for i in range(1,10):
    print('{}*{}={}'.format(n,i,n*i))
    
# 구구단 안에 구구단
for i in range(2,10): #2단부터 9단까지 출력
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j))
        
# 출력 형태
# 1 2,3,4,5
for j in range(5): #j가 0 ,1,2,3,4 한 줄로 출력
    print(j,'번째 출력')
    for i in range(1,6): # i = 1,2,3,4,5 한 줄로 출력
        print(i, end='')
    print()   #줄바꿈
print('for 끝') 

for i in range(2,10):
    print('[{}단]'.format(i))  
    for j in range(1,10):
     print(' {}*{}={} '.format(i,i,j,i*j), end ='')
    print()  #줄바꿈
print('구구단 끝')

# 짝수단만 출력하기 if 사용

for i in range(2,10):
    if i % 2 == 0:
        print('[{}단]'.format(i))
        for j in range(1,10):
            print('{}*{}={}'.format(i,j,i*j, end = ''))
        print()
# 홀수 단만 출력
for i in range(2,10):    
    if i % 2 ==1:
        print('[{}단]'.format(i))
        for k in range(1,10):
            print('{}*{}={}'.format(i,k,i*k, end = ''))
        print()

#(*1,3,5,7,9 3*1=3 3*3 3*5)

for i in range(2,10):
        for j in range(1,10):
            if j % 2 ==1:
                print('{}*{}={}'.format(i,j,i*j))
            print()
    
        