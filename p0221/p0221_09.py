# 두 수를 입력받아서 사칙연산을 출력해보세요
#예 : 30,6 을 입력받아서
# 출력:
#30 + 6 =36
#30 - 6 =30
#30 *6 = 180
#30 / 6 = 5.0

n1 = input("첫번째 숫자를 입력하세요")
n2 = input("두번째 숫자를 입력하세요")
print(" 두 수의 합 :", int(n1)+int(n2))
print(" 두 수의 차 :", int(n1)-int(n2))
print("두 수의 곱:", int(n1)*int(n2))
print("두 수의 나눗셈:", int(n1)/int(n2))

#print("두 수의 합(float 형) : ", float(n1)+float(n2))

print(" 두 수의 합", float(n1)+float(n2))
print("두 수의 차", float (n1)-float(n2))
print("두 수의 곱", float(n1)*float(n2))
print("두 수의 나눗셈",float(n1)/float(n2))

n1 = 30
n2 = 6
print(str(n1)+"+"+str(n2)+"=" +str(n1+n2))
print(str(n1)+"-"+str(n2)+"=" +str(n1-n2))
print(str(n1)+"*"+str(n2)+"=" +str(n1*n2))
print(str(n1)+"/"+str(n2)+"=" +str(n1/n2))


# ,사용

a = 30
b = 6

print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',a/b)

#input함수를 사용해서 입력받은 거 출력하기
# c = 100 ("아무거나 입력하세요 >>")
# print('c의 값은 : ,c')

#변수를 사용해서 출력하기 2번쩨 방법 (제시문 바꾸기)
n1 = int(input("첫번째 숫자를 입력하세요 >>"))
n2 = int(input("두번째 숫자를 입력하세요 >>"))

print(" 두 수의 합 :", (n1)+(n2))
print("두 수의 차 :", (n1)-(n2))
print("두 수의 곱:", (n1)*(n2))
print("두 수의 나눗셈:" , (n1)/(n2))