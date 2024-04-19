# 산술 연산자
# + - * / 

a = 6
b = 3
result = a+b
result = a-b
result = a*b
result = a/b
print(result)
result = a//b # 몫 4//2 몫 : 2 나머지 : 0
print(result)
result = a%b # 나머지 
print(result)
result = a**b #제곱
print(result)

c = 10
d = 20
c,d = 10, 20

# 산술연산자 우선순위
# 곱셈, 나눗셈 먼저 -> 덧셈, 뺄셈 순으로 진행
# 괄호가 없을 경우 왼쪽에서 오른쪽 방향으로 계산
r1 = 2 + 2 - 2 * 2 / 2 * 2 #보기 너무 어려움

# 괄호 사용을 추천
r2 = 2 - (2/2)

#다른 자료형으로 연산
str1 = "문자열"
n1 = 10

print(str1*n1)
# print(str1+n1) #error
#문자열이 정수나 실수일 경우 int() float()를 사용해서 변환
s1 = "100"
s2 = "10.213"
print(int(s1)+1) #정수
print(float(s2)+1) #실수

# 숫자가 아닌 것을 변환 할 수 없다
# n= int("안녕하세요") #error

#숫자를 문자로 바구고 싶으면 str()사용
n1 = 100
n2 = 10.123
print(str(n1)+"1")
print(str(n2)+"1")

p = 123456789
print("010"+str(p))

#숫자 두 개를 입력받아서 나누기, 몫, 나머지 값을 구하세요

n1, n2,

#입력받기
n1 = input("첫번째 숫자를 입력하세요 >>")
n2 = input ("두번째 숫자를 입력하세요 >>")
# 문자를 숫자로 변경
n1 = int(n1)
n2 = int(n2)

result1 = n1/n2
result2 = n1//n2 #몫
result3 = n1%n2 #나머지

print("나누기 값은 {}점 입니다.".format(result1))
print("몫은 {}점 입니다.".format(result2))
print("나머지 값은 {}점 입니다.".format(result3))

# print("나누기:{:.2f}\n몫:{}\n나머지:{}".format(n1/n2,n1//n2,n1%n2)) 

# print("%.2f"%(123.45678))