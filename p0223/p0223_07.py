# 해보세요
cal = input('수식을 입력하세요 (+,-,*,/) >>')
n1 = 4
n2 = 8

if cal == '+':
    print("입력하신 수식의 값은 {} 입니다.".format(n1 + n2))
elif cal == '-':
    print(n1-n2)
elif cal == '*':
    print(n1*n2)
else:
    print(n1/n2)     
# 숫자도 입력
cal = input('수식을 입력하세요 (+,-,*,/) >>')
n1 = int(input('첫번째 숫자를 입력해주세요 >>'))
n2 = int(input('두번째 숫자를 입력해주세요 >>'))

if cal == '+':
    print("입력하신 수식의 값은 {} 입니다.".format(n1 + n2))
elif cal == '-':
    print(n1-n2)
elif cal == '*':
    print(n1*n2)
else:
    print(n1/n2)     