students =[
     {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

#학생성적 입력 부분 구현
cnt = len(students)
while True:
     print('-'*40)
     print('[학생성적프로그램]')
     print('-'*40)
     print('1. 학생성적입력')
     print('2. 학생성적전체출력')
     print('3. 학생검색')
     print('4. 학생수정')
     print('5. 등수처리')
     print('6. 학생삭제')
     print('0. 프로그램 종료')
     print('-'*40)
     choice = input('숫자를 입력해주세요 (0.종료 )>> ')
     if choice == '0':
          print('입력을 종료합니다.')
     if not choice.isdigit:
          print('숫자만 입력가능합니다')
          continue
     
     if choice == '1':
          print('학생성적입력을 선택하셨습니다.') 
          print('-'*60)    
          while True:
               name = input('학생의 이름을 입력해주세요 (0.취소) >> ')
               if name == '0':
                    print('입력을 취소하셨습니다')
                    break
               kor = int(input('학생의 국어점수를 입력해주세요 >> '))
               eng = int(input('학생의 영어점수를 입력해주세요 >> '))
               math = int(input('학생의 수학점수를 입력해주세요 >> ' ))
               total = kor + eng + math
               avg = float('{:.2f}'.format(total /3))
               cnt += 1
               student = [cnt,name,kor,eng,math,total, avg]
               students.append(student)
               print('입력 데이터 : ',student)
          print(students)
          
     if choice == '2':
          all_count = input('전체출력을 하시겠습니까? (0.취소) >> ')
          if all_count == '0':
               break
          else:
               print('학생성적전체출력을 선택하셨습니다')
               print('-'*60)
               print('학번\t이름\t 국어\t 영어\t 수학\t 총합\t 평균\t 등수 ')
               print(students, end = '\t')
     
     


