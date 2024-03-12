students = {"stuNo":1,'stuName':'홍길동','kor' : 100}
students['eng'] = 100 #딕셔너리 추가
students['kor'] = 60 #딕셔너리 수정
del students['stuName'] #딕셔너리 삭제
print(students)

# 타입 list,dict, int, float, str
print(students.keys()) # 클래스 형태 #딕셔너리에 키값만 추출
print(students.values()) # 딕셔너리 value값 추출
print(students.items()) # 딕셔너리 key, value 토플 형태로 추출

# 토플 : 수정, 삭제가 불가능







# list = [1,2,3,4,5]
# list.append(6)
# print(list)
# del list[0]
# print(list)
# list[0] = 100
# print(list)
# # print[5]=1000 # 배열에서 벗어나면 에러
# # print(list) 