# 관계연산자
# 어떤 것이 크거나 작거나 같은 지를 비교
# 참은 True, 거짓은 False로 표시
# 주로 조건문, 반복문에서 사용. 
# 수식1 == 수식2 : 수식1과 수식2가 같은 지 평가
# 수식1 != 수식2 : 수식1과 수식2가 같지 않음을 평가 !=not 
# 수식1 > 수식2  :  수식1이 수식 2 값보다 큰 거를 평가
# # 수식1 >= 수식2 : 수식1이 수식2 값보다 크거나 같은 가를 평가
# <, <= 작은가, 작거나 같은가
# 등호는 뒤에서 사용

print(3 != 6) 
num = 95
print(num >90)
print(num <=90)
print(num ==90)
print(num !=90)

print(num ==10)

#print(num = 10)
print(90 <= num <100)

#논리연산자
# and (그리고), or(또는), not(부정) 세가지 종류
# and 둘 다 참이어야 참
# or 둘 중 하나라도 참이면 참
# not 참이면 거짓, 거짓이면 참

kor = 90
avg = 80
print(kor > 80) #True
print(avg > 90) #False
print(kor>80 and avg >90) #False # 참 and 거짓 => 거짓
print(kor>80 or avg > 90 ) #True # 참 or 거짓 => 참
print( not avg >=90) #True 거짓이기 때문에 참

 