fruit = {'peach':'복숭아','orange':'오렌지','apple':'사과', 'pear':'배','grape':'포도',
         'mango':'망고','kiwi':'키위'}
# ex)복숭아 영어로 입력하시오 -> 맞추면 정답입니다./ 정답이 아닙니다. 딕셔너리에 전부 묻고,
# 몇 문제를 맞췄는지 출력

answer = 0
wrong = 0

for f in fruit: # f = 키값, fruit[f] = value값
     eng_in = input(f'{fruit[f]}를 영어로 입력하세요 >> ')
     if eng_in == f:
          
          print(f'입력한 단어는 {eng_in} 입니다.')
          print('정답입니다')
          answer += 1
     else:
          print(f'입력한 단어는 {eng_in}로 정답이 아닙니다. 정답은 {f} 입니다.')
          wrong += 1
print('[문제 결과]')
print('총문제 : ', len(fruit))
print('정답 :', answer)
print('오답 :', wrong)