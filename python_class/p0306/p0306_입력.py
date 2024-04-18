# students = [[S001,'홍길동',100,100,99,299,99.67,1],[S002,'유관순',90,90,90,270,90.0,1],
#             [S003,'이순신',80,80,80,240,80.0,1],[S004,'김구',70,70,70,210,70.0,1],
#             [S005,'강감찬',60,60,60,180,60.0,1]]

students =[
     {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

cnt = len(students)+1
while True:
     name = input(f'{len(students)+1}번째 학생의 이름을 입력하세요 (0. 취소) >> ')
     if (name == '0'):
          print('학생입력을 취소하셨습니다.')
          break
     student = {}
     student['stuNo']= "S"+"{:03d}".format(cnt)
     student['name'] =name # 딕셔너리 추가
     kor = int(input('국어 점수를 입력하세요 >> '))
     student['kor'] = kor
     eng = int(input('영어점수를 입력하세요 >> '))
     student['eng'] = eng
     math = int(input('수학점수를 입력하세요 >>'))
     student['math']= math
     total = kor + eng + math
     student['total']=total
     avg = total/3
     student['avg'] = float('{:.2f}'.format(avg))
     students.append(student)
     cnt += 1 # 학번증가

     print('입력 데이터 : ',student) #list -> dict
     print(students)