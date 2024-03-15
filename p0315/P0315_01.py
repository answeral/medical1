# 로그인
while True:
     print('\t\t[ 학생성적 프로그램]')
     print('-'*60)
     print('\t\t[ 로그인 ]')
     print('먼저 로그인을 해주세요')
     print()
     c_id = input('ID를 입력하세요. >> ')
     c_pw = input('PASSWORD를 입력하세요. (0.종료) >> ')
     
     if c_pw == '0':break
     
     if c_id == 'aaa' and c_pw == '1111':
          pass
     else:
          print('ID 또는 PASSWORD가 일치하지 않습니다. 다시 확인해주세요.')
          
          
print('프로그램을 종료합니다.')