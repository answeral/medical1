''' 반복문 - for, while
for 변수 in  반복가능한 데이터:
   수행문



for 카운터변수 in range(시작값, 끝값+1, 증감값) :
   수행문

'''
for i in range (0,10,1): #0,1,2,3,4,5,6,7,8,9
    print(i,'증감 1 :수행문입니다.')
print()    
for i in range (0,10,2): #0,2,4,6,8
    print(i,'증감 2 :수행문입니다.')
    
for i in range(0,3): #증가값이 1일때는, 생략 가능
    print('두번째 수행문입니다.')
    
for i in range(5): #5번 반복해라
    print(i,'세번째 수행문입니다')
    
for i in range(3): #3번 반복해라 1씩 증가, 0부터 시작 -> 생략
    print(i)    

# 카운터변수 i를 사용 하지 않을 때 _로 사용 가능    
for _ in range(7): # 안녕하세요를 7번 반복해라
 print('안녕하세요')
 
for i in range (10,0,-2): # -사용
    print(i,'증감 -2 :수행문입니다.')
    
l1 = [100,200,300,400,500]
#      0   1   2   3   4
# 리스트 안 요소 확인 in / not in
'''
for 변수 in 리스트명:
    실행문
    
    
    
for 변수 in range(len(리스트명)) # 리스트 전체를 돌아라
    실행문
    리스트명[변수]

'''
for n in l1: # 100 200 300 400 500이 출력
    print(n)
print()
# for i in range(l1):
#      print(i) #0,1,2,3,4..
#      print(l1[i]) #l1[0],l1[1],l1[2]....
  
#for문을 사용해서 1-100 사이의 홀수를 출력하기
#1)if 사용하지 않음 - 증감이용
for i in range (0,100,2):
  print(i+1, end=' ')
print() 

#2) if 사용 
for i in range (100):
 if (i+1)%2 == 1:
     print(i+1, end=' ')
print()

#50-1 사이의 6의 배수를 역순으로 출력하기
for i in range(50,0,-1) :
    if i%6==0:
     print(i, end=' ')
for i in range(50,0,-6):
    print(i, end = ' ')    
print()    
#input() 사용
# 입력: 두 개의 숫자를 입력받음
# 출력 : 사칙연산 -> a+b =c a-b =d a*b = e a/b = f
# 계산을 10번 반복하는 코드를 만드세요

for i in range(10):
  n1 = int(input('첫번째 숫자를 입력하세요 >>'))
  n2 = int(input('두번째 숫자를 입력하세요 >>'))
  ch = input('기호를 입력해주세요 (+,-,*,/) >>')
  if ch == '+':
   print('{} + {} = {}'.format(n1,n2,n1+n2))
  elif ch == '-': 
   print('{} - {} = {}'.format(n1,n2,n1-n2))
  elif ch == '*': 
   print('{} * {} = {}'.format(n1,n2,n1*n2))
  elif ch == '/':
   print('{} / {} = {:.2f}'.format(n1,n2,n1/n2))
  else:
    print('잘못입력하셨습니다. 다시 입력해주세요.')
    
   


