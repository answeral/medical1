# 학번 1000번, 이름 홍길동 학과 컴퓨터 공함,
student = {'학번':1000, '이름':'홍길동','학과':'컴퓨터공학'}

for key in student: #키값
    print('{}:{}'.format(key,student[key]))
    
           
print('-'*50)
    


#연락처 010-1111-1111
student['연락처'] = '010-1111-1111'
print(student)

#수정
student['이름']='유관순'
print(student)

#학과 - 화학과
student['학과']='화학과'
print(student)

# key의 value값 출력
print(student.get('이름')) 
print(student['이름'])

# print(student['성별']) # key값이 존재 하지 않으므로 에러
print(student.get('성별')) # key값이 없을때 None, 에러가 나지 않음.

if "이름" in student:
    print('이름 키값이 있습니다')
    print(student['이름'])
else :
    print('이름 키값이 없습니다.')
    
if '성별' in student:
    print('성별 키값이 있습니다')
    print(student['성별'])
else:
    print('성별 키값이 없습니다')
    

for i in student.keys():
    print(i)
print(type(student.keys()))  # 타입은 class로 출력
print(student.keys()) # 리스트 타입으로 출력
print(list(student.keys()))    # 형변환을 해야 list 타입으로 출력
print('-'*50)

# student.values()딕셔너리의 모든 value를 출력
print(student.values())
print(list(student.values()))

for i in student.values():
    print(i)


# items() 튜플 형태로 데이터를 리턴 # 튜플 형태는 변경, 수정 불가
print(student.items())

if '이름' in student:
    print('키값이 있습니다')
else:
    print('키값이 없습니다')
    
    
    
    
    
