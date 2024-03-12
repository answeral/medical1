# while문과 if문을 사용
# 숫자 2 개를 입력 받고,
# 연산자를 입력 받아서( +-*/)
# 계산 결과 출력 (if)
# 무한한 계산하는 계산기를 만드는데
# 첫번째 숫자에 0을 입력하면 프로그램이 종료가 되는 코드를 만들기

while True: # 무조건 참이기 때문에 while안에 있는 것을 계속 반복
    n1 = int(input('첫번째 숫자를 입력해주세요 (0을 입력하면 종료)>> '))
    if n1 ==0:
        print('종료합니다')
        break
    n2 = int(input('두번째 숫자를 입력해주세요 >> '))
    s = input('연산자를 입력해주세요 (+-*/) >>')
    if s == '+':
        print('{} {} {} = {}'.format(n1,s,n2,n1+n2))
    elif s == '-':
        print('{} {} {} = {}'.format(n1,s,n2,n1-n2))
    elif s == '*':
        print('{} {} {} = {}'.format(n1,s,n2,n1*n2))
    elif s == '/':
        print('{} {} {} = {:.2f}'.format(n1,s,n2,n1/n2))
    else:
        print('입력하신 숫자와 문자를 다시 확인 바랍니다')
    
    
