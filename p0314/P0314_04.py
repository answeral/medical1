# 파일 생성

# file open
file = open('memo.txt','w',encoding='utf8')
try:
     # file write
     file.write('안녕하세요.1\n')
     file.write('안녕하세요.2\n')
     file.write('안녕하세요.3\n')
     print(1/0)
     file.write('안녕하세요.4\n')
except Exception as e : #Exception as e : 에러의 종류에 대해서 설명 (예외에 대한 설명 출력)
     print('저장시 에러가 났습니다.')
     print(e) #division by zero
finally:     
     #파일 닫기
     file.close() # 예외가 발생해도 하지 않아도 무조건 실행
     
     
     
