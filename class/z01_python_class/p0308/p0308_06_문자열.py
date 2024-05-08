# [ 문자열 ] #리스트와 같다
# 인덱싱[0], 슬라이싱[0:][1:4][:], len, upper, lower, swapcase, title
# print('안녕')
# a= '안녕'
# b = 2
# c = 3
# d = '10'
# print(b+int(d)) #타입이 같아야 사칙연산이 가능

# a = 1000000
# b = '안녕하세요.반갑습니다.저는홍길동입니다.'
# print(len(b)) #문자열 길이
# print(b[0])
# print(b[2:5]) #하세요 출력 # 슬라이싱
# print(len(str(a)))

# a = input('문자를 입력하세요 >> ')
# print('현재 입력한 문자 길이 :', len(a))

# a = [1,2,3,4,11111,1,145,20,1323456547]
# #리스트의 각 숫자의 길이를 출력하시오.
# print(len(str(a[4])))
# for i in a:
#     print('리스트의 문자 길이 : ',len(str(i)))
# print()
# #짝수만 문자 길이를 출력
 
# for i in a:
#      if i%2 ==0:
#          print('숫자 : {}, 길이 : {} '.format(i,len(str(i)))) 

# #한글자씩 출력하기
# title = '혼자공부하는파이썬수업'
# for i in range (len(title)):
#      print(title[i])

# print(1,2,3,4,sep = '*') #sep = 중간에 넣어라
# # 역순출력
# title = '안녕하세요'
# for i in range(len(title)): #5
#      print(title[(len(title)-1)-i])

# upper(): 전부 대문자
# lower(): 전부 소문자
shape_list=['spade','diamond','heart','clover']
for i in shape_list:
     print(i.upper()) #전부 대문자로 출력
     print(i.title()) #첫글자만 대문자
     print(i.swapcase()) #소문자->대문자, 대문자->소문자
     print(i.lower()) # 전부 소문자 