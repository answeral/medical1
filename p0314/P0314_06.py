a_list = [1,2,3]
try: 
     
     print(a_list[5])                                        #타입 :  <class 'IndexError'>
     print(1/0)                                              #타입 :  <class 'ZeroDivisionError'>
     txt =int(input('숫자를 입력하세요 >> ')) #문자 입력시     #타입 :  <class 'ValueError'>
     print(txt)
except IndexError: # Exception위에 종류별로 처리 해야함
     print('리스트의 주소가 잘못 입력되었습니다')
except Exception as e: #EXception 최상위 예외처리 
     print('--예외가 발생했습니다.--')
     print(' 타입 : ',type(e)) 
     print(e)