# 함수선언 : def 이름()
# 함수 호출 : 이름()
# 함수 선언 : def 이름(매개변수) -> 이름 (매개변수), 매개변수의 개수 맞춰야함
# 리턴의 결과값을 받지 않아도 되지만, 리턴의 개수는 맞춰야함.
# 함수 내의 변수는 지역변수여서, 함수가 종료되면 사라짐
# 함수 내의 변경된 변수값을 전역변수에 반영하고 싶으면 return으로 돌려줘야함
# 함수 내 global이라고 하면, 전역변수에 선언되어 있는 변수주소를 가져와서 return을 사용하지 않아도 됨.(잘사용하지 않음)

# def cal(v1,sum): 
#      sum = sum + 500 # 지역변수
#      v1 = 200 # 지역변수
#      return v1, sum

# sum = 10 # 전역변수
# v1 = 100 # 전역변수
# cal(v1,sum) 
# print(v1)
# print(sum) 

# 함수 선언
# def func1():
#      global a # 전역변수를 가져옴 # 잘 쓰지 않음
#      a=100 # 지역변수
#      print('func1 a =',a+10) # 지역변수의 영향
#      #지역변수 값을 전역변수에 적용시키는 방법
       
# def func2():
#      print('fucn2 b =',a+10) # 전역변수의 영향 -> 전역변수가 없다면 error
   
# # 전역변수
# a = 20 
# #함수 호출
# func1() # 전역변수가 100으로 바뀜
# func2()
# print(a)
# print('결과값 : ',a)

#매개변수 리스트,딕셔너리를 사용하는 경우 return을 사용할 필요가 없음.
def func1(a,a_list):
     a = 100 # 지역변수
     a_list[0]=100 # 지역변수
     return a


a = 10 # 전역변수
a_list = [1,2,3] # 전역변수

# 함수 호출 
a = func1(a,a_list) # a_list는 2개 이상의 데이터를 저장하는 변수 : 주소값을 저장함 (리스트, 딕셔너리)

# 데이터 출력
print(a)
print(a_list)
