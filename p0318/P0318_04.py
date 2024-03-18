def cal(num1,num2):# 어디서 왔는지 알기 위해서 이름을 같게 함
     num1 = num1 + 10
     num2 = num2 + 20
     result = num1 + num2
     return result


# -----------------------------------------------------------------

num1 = 5
num2 = 7

result = cal(num1,num2) # 함수 호출

print('현재 숫자 : ', num1, num2, result)



# 키워드 매개변수 : 키워드 매개변수는 제일 뒤에 와야 함.
def cal(num1,num2=20):
     num1 = num1 + 10
     num2 = num2 + 20
     result = num1 + num2
     return result


# -----------------------------------------------------------------

num1 = 5
num2 = 7

result = cal(num1) # 함수 호출

print('현재 숫자 : ', num1, num2, result)

