import random
def screen():
     print('-'*60)
     print('[로또 번호 맞추기 프로그램]')
     print('-'*60)
     print('1. 번호 생성 \n')
     print('2. 번호 섞기 \n')
     print('3. 나의 로또 번호 입력 \n')
     print('4. 번호 확인 \n')
     print('-'*60)
     choice = int(input('원하는 번호를 입력하세요 >> '))
     return choice

# 번호 생성 함수
def num_generate(lotto):
     print('[ 번호생성 ]')
     # lotto = [ i for i in range(1,46)] # 지역변수로 변환, 새롭게 재정의
     
     # for i in range(1,46):
     #      lotto.append(i)
     # print(lotto)  
         
     for i in range(45):
          lotto[i] += i+1
     #lotto = [0]*45
     
# 번호 섞기 함수
def num_shuffle(lotto):
     print('[ 번호섞기 ]')
     lotto.random.shuffle(lotto)
     print(lotto)
     
# 로또번호입력 함수
def num_input(my_lotto):
     print('[ 나의로또번호입력 ]')
     for i in range(6):
          my_num = int(input(f'{i+1}번째 로또 번호를 입력하세요 >>'))
          my_lotto[i] = my_num
     print('내가 입력한 번호 :' ,my_lotto[i])

# 로또번호확인 함수
def num_check(lucky_lotto,lotto,my_lotto,win_num,win_amount):
     # win_num = [] # 지역변수로 인식되어서 주소값을 다시 세팅
     for i in range(6):
          lucky_lotto [i] = lotto[i]
     print('[ 번호확인 ]')
     print('로또번호 :', lucky_lotto)
     print('내가 입력한 번호 :', my_lotto)
     
# 몇 개 맞췄는지 확인 소스
     for i in my_lotto:
          if i in lucky_lotto:
               win_num.append(i)
               
     print('당첨된 번호 : ', win_num)     
# 당첨금액출력
     print('당첨금액 : {} 원'.format(win_amount[len(win_num)]))
     print('-'*60)
     print()

#-----------------------------------------------------------------------
lotto = [0]*45 # 전체 45개 숫자 #lotto = [0]*45
lucky_lotto = [0]*6 # 당첨번호 6개 숫자 1 20 30 40 41 45
my_lotto = [0]*6 # 내가 입력한 6개 숫자 1 20 21 23 25 44 
win_num = [] # 맞춘 번호 1 20 -> 2개
win_amount = [0,0,1000,10000,1000000,100000000,10000000000] # 당첨금액

while True:
     
     choice = screen() # 화면출력함수 호출
     
     if choice == 1:
          num_generate(lotto) # 번호생성함수 호출
         
     elif choice == 2:
          num_shuffle(lotto) # 번호섞기함수 호출
          
          
     elif choice == 3:
          num_input(my_lotto) #나의 번호입력
               
     
     elif choice == 4:
          num_check(lucky_lotto,lotto,my_lotto,win_num,win_amount)
          win_num = []
          
     
          
          
     
          
     
     
     
          
#-----------------------------------------------------------------------
lotto = [0]*45 # 전체 45개 숫자 #lotto = [0]*45
lucky_lotto = [0]*6 # 당첨번호 6개 숫자 1 20 30 40 41 45
my_lotto = [0]*6 # 내가 입력한 6개 숫자 1 20 21 23 25 44 
win_num = [] # 맞춘 번호 1 20 -> 2개
win_amount = [0,0,1000,10000,1000000,100000000,10000000000] # 당첨금액

while True:
     
     choice = lotto.screen() # 화면출력함수 호출
     
     if choice == 1:
          lotto.num_generate(lotto) # 번호생성함수 호출
         
     elif choice == 2:
         lotto.num_shuffle(lotto) # 번호섞기함수 호출
          
          
     elif choice == 3:
          lotto.num_input(my_lotto) #나의 번호입력
               
     
     elif choice == 4:
          lotto.num_check(lucky_lotto,lotto,my_lotto,win_num,win_amount)
          win_num = []
          
     
          
          
     
          
     
     
     
          