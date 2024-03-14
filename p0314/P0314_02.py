# try-except문은
# 외부와의 데이터 전송, 데이터 받기, 외부기기 연결, 다른 프로그램 연결에 주로 사용
# 이런 곳 외에는 되도록 프로그램이 오류 발생되지 않도록 하는 것이 좋음.

print('프로그램 실행')
try:
     print(1)
     print(2)
     print(1/0) # 에러가 발생 # 1 2 4 5 6 
     print(3)
except:
     print(4) # 에러가 발생하지 않으면 except문은 돌지 않음 # 1 2 3 6
     print(5)
print(6)

print('프로그램 종료')

