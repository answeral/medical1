words = [ {},
     {'airplane':'비행기','apple':'사과','bakery':'빵집','banana':'바나나',
          'bank':'은행','bean':'콩','bicycle':'자전거','boat':'보트','bowl':'그릇',
          'bus':'버스'},{'bake':'굽다', 'mope':'맥이 빠져 지내다','move':'움직이다','blow':'불다',
          'check':'확인하다','chew':'씹다','close':'닫다','dance':'춤추다'},{ "accumulated":"누적된",
    "additional":"추가적인","adequate":"적당한","administrative":"관리의","affordable":"알맞은",
    "alternative":"대체 가능한","annual":"해마다의","different":"다른","local":"지역의",
    "social":"사회의"}]


w_title =['','명사','동사','형용사']
#함수선언
def w_quiz(choice):
  print(f'{w_title[choice]}를 선택하셨습니다.')
  choice == int(input('퀴즈가나갑니다. 준비되셨나요? (0. 취소 1. 실행) >> '))
  if choice == 1:
               #퀴즈프로그램
               for key in words[choice]:
                    # print(key,w_noun[key])
                    answer = input(f'{key}의 한글 단어 뜻을 적으세요 >> ')
                    if answer == words[choice][key]:
                         print('정답입니다')
                         correct += 1
                    elif answer != words[choice][key]:
                         print(f'틀렸습니다. 정답은 {words[choice][key]}입니다')
                         wrong += 1
               print('전체 문제 수 :', len(words[choice] )   )       
               print('맞은 문제 수 : ', correct)
               print('틀린 문제 수 :', wrong)  
               correct = 0
               wrong = 0
                    
  elif choice == 0:
     print('퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다.')           

while True:
     print('[영단어 맞추기 프로그램]')
     print('-'*50)
     print('1. 명사 ')
     print('2. 동사 ')
     print('3. 형용사 ')
     print('0. 종료 ')
     print('-'*50)
     choice = int(input('원하는 번호를 입력하세요. >> '))
     
      
     if choice == 1:
          w_quiz(choice)
     elif choice ==2:
           w_quiz(choice)
     elif choice == 3:
           w_quiz(choice)
     else:
          print('프로그램이 종료됩니다')
          break
