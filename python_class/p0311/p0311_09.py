# def plus(v1,v2):
#      v1 = v1 + 100 # 101 -> 함수 내에 있는 변수는 밖에서는 실효 X
#      v2 = v2 + 200 # 202 -> 함수 내에 있는 변수는 밖에서는 실효 X
#      return v1,v2 # return으로 돌려줘야하지만 함수 밖에서도 동일
#                   # 함수 밖에서 사용하려면 return 값을 돌려줘야 함
     
     
# # 함수 호출
# v1 =1
# v2 =2
# v1, v2 = plus(v1,v2)

# # 함수 출력
# print(v1,v2) # 1 , 2 

# for i in range(10):# i -> 지역변수
#      print(i)
   

def cal(input1, input2):
     result1 = input1 + input2
     result2 = input1 - input2
     result3 = input1 * input2
     result4 = input1 / input2
     return result1, result2, result3, result4

input1 =  int(input('첫번째 숫자를 입력하세요 >> '))
input2 = int(input('두번째 숫자를 입력하세요 >> ')) 

#함수의 return을 사용해서 입력된 두 수의 사칙연산 결과값을 출력하시오.
# 20, 10
# 결과 값 30, 10, 200, 2    
result1, result2, result3, result4 = cal(input1, input2)
print('더하기 :',result1)
print('빼기 :',result2)
print('곱하기 :',result3)
print('나누기 :',result4)

