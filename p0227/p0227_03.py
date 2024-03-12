# list
# 리스트 변수명 = [요소1, 요소2, 요소3, 요소4,....,요소n ]
# 요소 하나하나가 변수 (int, bool, float, string, list)
L1 = ['홍길동', 100]
L2 = [[2,4,6], [1,3,5]]
L3 = [True, False, 3.14, 'hello',[1,2], 5]
#      0      1      2      3      4    5
#      -6     -5    -4      -3    -2    -1

# 파이썬은 대소문자를 구별
# 참, 거짓을 나타내는 True, False는 대문자로 시작한다
# L3 = ['true', False, 3.14, 'hello',[1,2], 5] 

#인덱싱 : 리스트 검색, 접근
# index는 0부터 시작함.
# 홍길동
print(L1[0]) #홍길동
#L2에서 3을 출력
print(L2[1]) #L2에서 3을 출력

#해보기
#L3에서 False를 출력
print(L3[1])
# hello 출력
print(L3[3])
# 1 출력
print(L2[1][0])
print(L3[4][0])
# 5 출력
print(L2[1][2])
print(L3[5])

#인덱싱을 가지고 리스트의 특정 요소의 값을 수정할 수 있다
# L1 = ['홍길동', 100]

L1[1] = 90
print(L1)
L1 [0] = '이순신'
print(L1)
# L2 = [[2,4,6], [1,3,5]]

L2[0][2] = 8 # 6 ->8
L2[1][2] = 7 # 5-> 7

# L3 = [True, False, 3.14, 'hello',[1,2], 5]
# L3에서 True를 False로
L3[0] = False
# 3.14 ->31.4
L3[2] = 31.4
# 'hello ->'hi'
L3[3] ='hi'
# 2 -> 20으로 변경
L3[4][1] = 20
print(L3)

# 슬라이싱 : 리스트 자르기
# 리스트명[(시작인덱스):(끝인덱스 +1)]
num = [0,1,2,3,4,5,6,7]
print(num[1:6]) #1이상 6미만을 출력

str1 = ['a','b','c','d','e','f']
#        0   1   2   3   4   5
#        -6  -5  -4  -3  -2  -1
# [c,d] 출력
print(str1[2:4])
# [b,c,d,e,f]출력
print(str1[1:])
# [a,b,c]출력
print(str1[0:3])
print(str1[:3])
# [a,b,c,d,e,f]를 출력
print(str1[0:])
print(str1[:])
# [b,c,d,e] 출력
print(str1[1:-1])


# 리스트의 길이 len(리스트명)
print(L1, len(L1))
print(L2, len(L2))
print(L3, len(L3))
print(str1, len(str1))

print(L2)
# [[2, 4, 8], [1, 3, 7]]
print(len(L2[0])) #3 #요소의 길이도 출력 가능

# 리스트 값 추가
# 리스트명.append(값)
# num = [0,1,2,3,4,5,6,7]
# 8을 추가
num.append(8)
num.append('숫자')
num.append([0,1,2])
print(num)

# 해보기
# str1에 ㄱ,ㄴ,ㄷ, [1,2,3] 을 추가해보기
# str1 = ['a','b','c','d','e','f']
str1.append('ㄱ')
str1.append('ㄴ')
str1.append('ㄷ')
str1.append([1,2,3])
print(str1)

# 리스트에서 특정값 삭제
# 리스트명.remove(값)
num.remove(7)
print(num)

# 해보기
#str1에서 a,c,f삭제해보기
str1.remove('a')
str1.remove('c')
str1.remove('f')
print(str1)

# 요소확인 : 내부에 포함된 요소 존재 확인
# in, not in
print(1 in num) # -> True or False
print(10 not in num)

lan = ['영어', '한국어','일본어','스페인어','중국어']
print('영어' in lan)
print('한글' not in lan)

if '일본어' in lan:
    print('일본어가 있습니다.')

# 해보기
tmp = [['미국','영국','일본','중국','스페인'],['영어','영어','일본어','중국어','스페인어']]

#일본어를 출력하기
print(tmp[1][2])
#중국을 대만으로 변경
tmp[0][3] = '대만'
print(tmp)
#일본부터 스페인까지 출력
print(tmp[0][2:])
#프랑스와 프랑스어를 추가
tmp[0].append('프랑스')
tmp[1].append('프랑스어')
print(tmp)
