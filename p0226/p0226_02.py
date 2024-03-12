#해보기
#나이가 10살이상이고 150이상만 탑승가능
#나이, 키를 입력받아
#[탑승가능], [탑승불가능]을 출력하기

age = int(input("나이를 입력해주세요 >> "))
hei = int(input('키를 입력해주세요 >> '))

if age >= 10 and hei >=150:
  print('탑승가능합니다.')
else:
 print('탑승 불가합니다.')
 
# if age >= 10:
      # if hei >= 150
         #print('탑승가능)
#else:
# print('탑승불가능')          


# 2. 숫자 3개 정수를 입력받고, 연산 1개를 입력받아
#+++ === *** ///(나누기값은 둘째자리까지 표현)
#ex) a + b+ c+ d의 형태로 출력

n1 = int(input("첫번째 숫자를 입력해주세요 >>"))
n2 = int(input("두번째 숫자를 입력해주세요 >>"))
n3 = int(input("세번째 숫자를 입력해주세요 >>"))

s1 = input ("기호를 입력해주세요 >>")

if s1 == '+':
    print('{}+{}+{}={}'.format(n1,n2,n3,n1+n2+n3))
elif s1 == "-":
    print('{}-{}-{}={}'.format(n1,n2,n3,n1-n2-n3))
elif s1 == "*":
  print('{}*{}*{}={}'.format(n1,n2,n3,n1*n2*n3))
elif  s1 == "/":
 print('{}/{}/{} = {:.2f}'.format(n1,n2,n3,n1/n2/n3)) 
else:
    print('입력하신 기호를 확인해주세요.')
    

'''

result = 0
if s1 == "+":
  result = a +b +c 
  print('{}+{}+{}={}'.format(n1,n2,n3,result))
elif s1 == '-':
  result = a - b - c
  print('{}-{}-{}={}'.format(n1,n2,n3,result))
elif s1 == '*'
  result  = a*b*c
  print('{}*{}*{}={}'.format(n1,n2,n3,result))
elif s1 = '/'
  result = a/b/c      
  print('{}/{}/{} = {:.2f}'.format(n1,n2,n3,result)) 

'''
