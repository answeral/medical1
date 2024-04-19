# print("a는 %s입니다"%"입력값")
# a = "입력값"
# print("a는 %s입니다"%a)

# 입력함수 : input() => 문자열로 입력받는다.
# a = input("값을 입력해주세요 >>")
# print("a는 %s입니다"%a)

n1 = input("첫번째 숫자를 입력하세요 >>") 
n2 = input("두번째 숫자를 입력하세요 >>")
print("두 수의 합 : ", n1+n2) #문자형
print("두 수의 합 : ", int(n1)+int(n2)) #숫자로
print("두 수의 합(float 형) : ", float(n1)+float(n2))

#강제 형변환
#int 정수형
#float 실수형
# 

a = 10 # 숫자
b = "10" # 문자
c = 20 # 숫자
d = "20" #문자

print("숫자일때 :",a+c)
print("문자일때:", b+d)
