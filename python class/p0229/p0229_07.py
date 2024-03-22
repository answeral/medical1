from random import*
#랜덤한 숫자를 만들어서 1-100사이
#내가 입력한 값이 랜덤한 숫자랑 같으면 당첨,
#아니면 다시 입력해주세요
#를 출력하는 프로그램을 만들어 보세요 while, for, 
# print(randint(1,100))
# print(randint(1,100))
# print(randint(1,100))
# print(randint(1,100))

#입력한 숫자가 랜덤 숫자보다 작으면 작습니다 더 큰 수를 입력해주세요
#입력한 숫자가 랜덤 숫자보다 
# 1.현재 입력한 숫자 모두를 inputlist에 넣으세요
inputlist =[]
# 2. 10회 도전 후 프로그램이 종료가 되게 해주세요.
# 3. 10회 도전아 실패한 사람에게 랜덤숫자 알려주기
ran = randint(1,100) #랜덤한 숫자 발생
i = 0
while i < 10:
    i += 1 
    n = int(input('{}번째 도전 ! 숫자를 입력해주세요 (1-100사이의 수) >>'.format(i))) 
    inputlist.append(n)
    if ran == n:
        print('당첨입니다. ')
        break
    elif ran < n:
        print('입력하신 숫자가 랜덤숫자보다 큽니다. 더 작은 수를 입력해주세요.')
    else:
        print('입력하신 숫자가 랜덤숫자보다 작습니다. 더 큰 수를 입력해주세요')
if i ==10:
    print('10회입력을 초과하셨습니다. 정답은', ran)

print(inputlist)   
         
        

     

