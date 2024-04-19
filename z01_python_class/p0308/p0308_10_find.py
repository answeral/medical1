ss = '파이썬공부는 즐겁습니다. 공부가 모두 재미있지는 않습니다'
#     0 1 2 3 4 5 6 7 8 9

# 존재하는 문자가 몇 번 나왔는지 확인
print(ss.count('공부'))
print(ss.count('자바')) # 없을 때는 0

print(ss.find('공부')) # 존재하는 문자열의 위치값 출력 , 3
print(ss.find('자바')) # 없을 때는 -1
print(ss.find('공부',6)) # 문자열 6번째 자리부터 검색시작해서 위치값 출력 , 14
print(ss.rfind('공부')) # 거꾸로 찾기
print('-'*20)

print(ss.index('공부')) # 3
# print(ss.index('자바')) # 존재 하지 않을 때 error 
print(ss.index('재미'))
print(ss.rindex('즐겁'))
print('-'*20)

print(ss.startswith('파이썬')) #맞으면 True
print(ss.startswith('자바')) # 틀리면 False
print('-'*20)
print(ss.endswith('않습니다'))#끝나는 문자열이 맞으면 True
print(ss.endswith('자바')) #틀리면 False