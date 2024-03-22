import operator
# 데이터를 저장하는 방식(~ 딕셔너리까지)
# 변수 - 1개 값 저장하는 타입
# 리스트 - 복수개를 저장하는 타입 []
# 딕셔너리 - 복수개를 저장하는 타입 (key, value) {}
# 토플 - 복수개를 저장하는 타입, 수정 불가능

fruits =['바나나','배','사과','딸기','딸기','딸기','딸기','사과','바나나','바나나',
          '배','사과','딸기','딸기','딸기','딸기','사과','바나나']

counter = {} # 딕셔너리 생성

# 딕셔너리 추가
counter['복숭아'] = 5 # 딕셔너리 추가
counter['바나나'] = 4 # 딕셔너리 추가
counter['바나나'] = 1 # 딕셔너리 수정

# print(counter['딸기']) # 딕셔너리에 없는 키값을 출력할 때 에러     
print(counter['바나나']) # 1

if '딸기' not in counter: #키가 존재하는지 확인
     counter['딸기'] = 0 # 키값을 생성   
else:
     print(counter['딸기']) # 키의 value값을 출력.

del counter['복숭아'] #딕셔너리 삭제
     
print(type(counter.keys())) #class 타입
print(counter.values())
print(counter.items())

a_list = [3,5,7,4,1,2,6]
print(sorted(a_list))
print()