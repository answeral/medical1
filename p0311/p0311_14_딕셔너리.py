# 함수 선언
def stu_update(student): #지역변수 -> 주소값이 저장되어 있음
     student['stuNo'] = 2
     student['name'] = '유관순'
     student['total'] = student['kor'] +student['eng']+ student['math'] # 지역변수
     student['avg'] = student['total']/3
   

# 프로그램 구현
student = {'stuNo': 1, 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 
           'total': 0, 'avg':0}


# 함수호출
stu_update(student) 


print('학생1 :',student) # 학생1 : {'stuNo': 2, 'name': '유관순', 'kor': 100, 'eng': 99, 
                         #'math': 87, 'total': 286, 'avg': 95.33333333333333}

# 함수를 사용하는 이유 
# - 재사용 하기 위해, 많은 양의 정보처리를 하기 위해, error 찾기 용이, 유지보수 쉬움 등등

