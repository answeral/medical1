# 함수선언 def 이름():
# 함수 값은 return
# 함수 선언 이름()
# 매개변수 : 함수로 데이터 전달하는 변수 ,매개변수 개수는 항상 같아야한다.
# 가변매개변수선언 *values, 갸변매개변수는 일치하지 않아도 된다.
# 리스트, 딕셔너리 매개변수는 주소값이 전달이 된다.

# 함수를 사용하여 두 수를 입력받아, 더하기, 빼기, 곱하기, 나누기 결과값을 출력


#함수호출

def cal(num1,num2,sum,min,multi,div):
     
     for i in range(num1,num2+1):
       sum += i
       min -= i
       multi *= i
       div /= i
     
     return(num1,num2,sum,min,multi,div)
     
sum = 0
min = 0
multi = 1
div = 1


# 두 수를 입력받아 값을 리턴받은 다음, 출력

num1 = int(input('첫번째 숫자를 입력하세요 >> '))
num2 = int(input('두번째 숫자를 입력하세요 >>'))

cal(num1,num2,sum,min,multi,div)

print(f'더하기 결과 : {num1}+{num2}={sum}')
print(f'빼기 결과 : {num1}-{num2}={min}')
print(f'곱하기 결과 : {num1}*{num2}={multi}')
print(f'더하기 결과 : {num1}/{num2}={div}')
'''
def cal(num1,num2,c):
     if c == '1' :
          result = num1 +num2
     elif c == '2' :
          result = num1 -num2
     elif c == '3' : 
          result = num1 *num2
     elif c == '4' :
          result = num1 /num2
          
     return(result)
          
     
     
num1 = int(input('첫번째 숫자를 입력하세요 >> '))
num2 = int(input('두번째 숫자를 입력하세요 >>'))
print('1.+ 2.- 3.* 4./')
c = input('원하는 사칙연산을 입력하세요 >>')
result = cal(num1,num2,c)
print('결과 값 {},{},{}'.format(num1,num2,result))
'''