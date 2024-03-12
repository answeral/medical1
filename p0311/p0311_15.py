# 함수선언
def cal(num1,num2):
     sum=0
     if num1>num2:
          num1,num2=num2,num1 # 2개 변수 치환
     for i in range(num1,num2+1):
          sum += i
     return sum

'''
def cal(num1,num2):
     sum=0
     temp = 0
     if num1>num2:
         temp =num1
         num1 =num2
         num2 = temp
     for i in range(num1,num2+1):
          sum += i
     return sum
'''



# 두 수를 입력받아, 입력한 사이의 합계를 구하는 프로그램을 구현해라
# ex ) 1-10 ->55 ,1+2+3+...+10

sum = 0                                        
num1 = int(input('첫번째숫자를 입력하세요 >> ')) 
num2 = int(input('두번째숫자를 입력하세요 >>  '))  

sum = cal(num1,num2)
print('합계 :', sum)