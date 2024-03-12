#n단부터 n2단까지 출력하세요
n1 = int(input('숫자 입력 >> '))
n2 = int(input('숫자 입력>> '))
# 크기 비교해서 n1이 더 크면 n2, n1값 바꾸기
# 출력 2단부터 4단까지

if n1 > n2 :
       n1, n2 = n2, n1
for i in range(n1,n2+1):
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j), end = '\t')
    print()

for i in range(1,10): # 1-9
    for j in range(2,10): # 단
        print('{}*{}={}'.format(j,i,i*j), end = '\t')
    print()
   
         