#두 수를 입력 받아서 사칙연산을 출력하기
#변수 n1,n2
# 10+3 =13
# 10 -3 = 7
# 10 *3 =30
# 10 /3 =3.3333

n1 = 10
n2 = 3

print('{}+{}={}'.format(n1,n2,n1+n2))
print('{}-{}={}'.format(n1,n2,n1-n2))
print('{}*{}={}'.format(n1,n2,n1*n2))
print('{}/{}={}'.format(n1,n2,"%.3f"%(n1/n2))) 
#print("%.2f"%(123.45678))

n1 = input("첫번째 숫자를 입력하세요 >>")
n2 = input("두번째 숫자를 입력하세요 >>")

n1 = int(n1)
n2 = int(n2)

print('{}+{}={}'.format(n1,n2,n1+n2))
print('{}-{}={}'.format(n1,n2,n1-n2))
print('{}*{}={}'.format(n1,n2,n1*n2))
print('{}/{}={}'.format(n1,n2,"%.3f"%(n1/n2)))