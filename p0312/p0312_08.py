# 자바 같은 경우 매개변수 개수에 따라 다른 함수 인정
# 파이썬은 이름이 무조건 달라야함. 
'''
def func(num1):
     print(num1)
     
def func2(num1,num2,num3):
     print(num1,num2) 

# 매개변수 개수 맞춰주기   
func(1)
func2(1,2) # 매개변수 개수가 달라서 error
'''

def func2(num1=1,num2=10,num3=3): # 키워드 매개변수 - 값이 들어오지 않으면 default값으로 설정
     print(num1,num2,num3)
     
func2(100) #100(첫번째에 100이라는 값을 넣어줌) 10 3 (둘 다 넣어주지 않아서 default값으로 print)



