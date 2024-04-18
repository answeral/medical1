# 변수
a = False #bool
b = 123  #정수
c = 1.34568 #실수
d = '문자' #문자열
e = [1,2,3] #리스트

#출력
print('안녕하세요')
print(123*456)
str1= "반갑습니다"
print(str1) # 변수를 통한 출력
print('{0:s} : {1:d} \{2:d} = {3:f}'.format ('수식 ', 7,3,7/3))
print( '{}, :{},{}={:.3f}'.format('수식', 7,3,7/3))


#관계연산자
# > :크다 >= : 크거나 같다
# < : 작다 <= : 작거나 같아
# == 같다 ?= 같지 않다
print( 3>5) #결과가 거짓 : False

n1 = 10
n2 = 8
print(n1 != n2) #True
print(3 <n1 < 100) #True

#if n1 < 10

#논리연산자 : and or not

a, b= 10,9
print('and 연산자' ) #둘 다 참이어야 참
if a == 10 and b==9:
  print('첨 and 참 = 참')
else:
    print( '참 and 참 = 거짓')
    
if a == 10 and  b != 9:
    print(' 참 and 거짓 = 참')
else:
    print('참 and 거짓 = 거짓') 
    
if a != 10 and b==9:
    print('거짓 and 참 =참') 
else:
    print('거짓 and 거짓 =거짓')
    
if a != 10 and b!=9:
    print('거짓 and 참 =참')   
else:
    print('거짓 and 거짓 =거짓') 
                  
                  
print ('or 연산자') # 둘 중 하나라도 참이면 참
print( 'not 연산자') # 참 -> 거짓, 거짓 -> 참
if not a == 10 :
  print('첨 and 참 = 참')
else:
    print( '참 and 참 = 거짓')
    

if not a != 10 :
    print('거짓 and 참 =참') 
else:
    print('거짓 and 거짓 =거짓')
    
#조건문 if
#if 조건문1:
# 실행문1:
#elif 조건문2:
# 실행문2
#else:
#  실행문3
#조건문1이 참이면, 실행문1을 실행 후 종료
#wlif가 있으면,
#즉 조건문1이 거짓이고 조건문2가 참이면 실행문2 실행 후 종료
#조건문1, 2가 거짓이면 실행문3 실행 후 종료

num = 5
#숫자가 0이상 이면 양수를 출력하시오
if num >= 0: 
    print("양수입니다")
    
#숫자가 0이상이면 양수를 출력하고, 0미만이면 음수 출력

if num>= 0:
    print('양수입니다')
else:
    print('음수입니다')    

if num > 0:
 print('양수입니다')
elif num == 0:
    print('0입니다')
else : 
    print('음수입니다')
    
print("-"*25) 
 # 실행문을 비우고 싶을때 :pass
if 1 ==1 :
    pass   
else :
    print('else문 실행')     

print("-"*25) 

#중첩 if문 : if문 안에 ifans 사용
if num >=0:
    if num == 0:
        print('0입니다')
    else:
        print('양수입니다')
else:
    print('음수입니다')
    
            
            




    

