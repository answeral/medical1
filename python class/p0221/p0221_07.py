print(200+100)
print(200-100)
print(200*100)
print(200/100)

#200을 50으로 바꿔서 출력

print(50+100)
print(50-100)
print(50*100)
print(50/100)

#100을 10으로 바꿔서
print(50+10)
print(50-10)
print(50*10)
print(50/10)

#변수를 사용 (하나하나 바꿀 필요가 없음)

a = 1000
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print('*'*20)
#함수를 사용하여 사칙연산 계싼
def cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    
cal(100,5)
print('*'*20)
cal(50,2)

num1 = 10
num2 = 5
print(str(num1)+'+'+str(num2)+'='+str(num1+num2))
print(num1,'+',num2,'=',num1+num2)
print('%d+%d=%d'%(num1,num2,num1+num2))
print('{}+{}={}'.format(num1,num2,num1+num2))
    
#수식을 10 - 5 = 5로 출력, 4가지 방법 사용
num1 = 10
num2 = 5

print(str(num1)+'+'+str(num2)+'='+str(num1+num2))
print(num1,"+",num2,'=',num1+num2)
print('%d+%d=%d'%(num1,num2,num1+num2))
print('{}+{}={}'.format(num1,num2,num1+num2))