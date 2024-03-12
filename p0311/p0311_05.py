# 함수 선언
def plus(n1,n2): # def이름 (매개변수1, 매개변수2)
     result = 0
     result = n1 +n2
     print('결과값 : ',result)
     

print('프로그랜을 실행합니다.')
plus(123456,789123) # 매개변수가 2개면 무조건 2개가 들어와야함. 개수가 맞지않으면 error.
plus(123,456) # 함수호출 : 함수이름(매개변수 개수를 맞춰주면 됨.)

'''
# 함수를 사용하지 않으면
n1, n2 = 10,20
result = 0
result = n1 +n2
print('결과값 : ',result) 

n1, n2 = 50,60     
result = 0
result = n1 +n2
print('결과값 : ',result)
'''