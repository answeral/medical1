# 해보세요
# 1. 숫자 두개를 입력받아서 나누기값, 몫값, 나머지값을 출력

#2. 3개의 수의 합을 구하세요
s1,s2,s3 = '100', '100.123','99.9'
#1
#1-1 입력받기
num1 = int(input("첫번째 숫자를 입력해주세요 >>"))
num2 = int(input("두번째 숫자를 입력해주세요 >>"))

print(num1/num2)
print(num1//num2)
print(num1%num2)

#r1= num1/num2 r2 = num1//num2 r3 = num1%num2 
# print(r1,r2,r3)

#2 format으로 사용, 정수/실수 구별하기

s1,s2,s3 = '100', '100.123','99.9'  #문자를 숫자로 변환
# s1 = int(s1) , s2 = float(s2) , s3 = float(s3) 
# or a1 = int(s1), a2 = float(s2), a3 = float(s3)
result = int(s1) + float(s2) +float(s3)
print('합은 {}입니다'.format(result)) #문장 사용시 .format 잊지 말기
