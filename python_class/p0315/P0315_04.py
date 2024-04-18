import P0315_02
#10명의 아이디, 패스워드 생성
member = P0315_02.idpw()
# 파일열기
file = open('mem.txt','r',encoding='utf8')

# 로그인
temp = 0
while True:
     if temp == 1:break # 프로그램 종료
     print('\t\t[ 학생성적 프로그램]')
     print('-'*60)
     print('\t\t[ 로그인 ]')
     print('먼저 로그인을 해주세요')
     print()
     c_id = input('ID를 입력하세요. >> ')
     c_pw = input('PASSWORD를 입력하세요. (0.종료) >> ')
     # 로그인 확인
     if c_pw == '0':break
     
     success_flag = 0
     #파일 읽기
     m = []
     while True:
          content = file.readlines()
          if content =='': break
          m = content.split(',')
          m[0] = m[0].strip() 
          m[1] = m[1].strip()
          if c_id == m[0] and c_pw == m[1]:
               success_flag = 1          
    
     #파일 닫기
     file.close()
     
     if success_flag == 1:
          print('로그인이 되었습니다.')
          print()
          while True:
               print('-'*60)
               print('[ 학생성적 프로그램]')
               print('-'*60)
               print('1. 학생성적데이터 읽어오기')
               print('2. 학생성적입력')
               print('3. 학생성적 출력')
               print('0. 프로그램 종료')
               print('-'*60)
               choice  = int(input('원하는 번호를 입력하세요 >> '))
               
               if choice == 1:
                    pass
               if choice == 0: 
                    temp = 1 # 프로그램 종료
                    break
               print()
               

                    
                        
     # 로그인 실패         
     else:
          print('ID 또는 PASSWORD가 일치하지 않습니다. 다시 확인해주세요.')
          
          
print('프로그램을 종료합니다.')