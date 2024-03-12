 # json형태
students =[ 
     {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]
cnt = len(students)+1
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
     choice = int(input('실행할 번호를 입력해주세요 >> (0. 취소 )'))
     student = {}
     
     if choice == 0:
          break
     if choice == 1:
          print('학생성적 입력을 선택하셨습니다.')
          name = input('학생의 이름을 입력해 주세요 >> ')
          student['name'] = name
          kor = int(input('학생의 국어 성적을 입력해주세요 >> '))
          student['kor'] = kor
          eng =  int(input('학생의 영어 성적을 입력해주세요 >> '))
          student['eng'] = eng
          math = int(input('학생의 수학 성적을 입력해주세요 >> '))
          student['math'] = math
          total = kor + eng + math
          student['total'] = total
          avg = total/3
          student['avg'] =avg
          students.append(student)
          cnt += 1
          print(f'{name} 학생의 성적이 입력되었습니다')
     
     
     elif choice == 2:
          print(' 학생전체출력을 선택하셨습니다.  ')
          ch = int(input('번호를 선택해주세요 (0. 취소 1. 출력 ) >>'))
          if ch == 0:
               print('전체출력을 취소하셨습니다.')
               break
          elif ch == 1:
              print('-'*40)
              print('번호 \t 이름 \t 국어 \t 수학 \t 영어 \t 합계 \t 평균 \t')
              for s_dic in students:
                   for s_key in s_dic:
                        print(s_dic[s_key], end = '\t')
                        
     elif choice == 3:
          print('학생검색을 선택하셨습니다.')
          print('** 학생검색출력')
          print('-'*40)
          while True:
               s_name = input('학생의 이름을 입력해주세요 (0.취소) >> ')
               chk = 0
               if s_name == '0':
                    print('검색을 취소합니다')
                    break          
               for s_dic in students:
                    if chk == len(students):
                         print('찾는 학생이 없습니다. 다시 확인해주세요')
                    if s_dic['name'] == s_name:
                         break
                    else:
                         print(f'{s_name} 학생의 성적입니다')
                         print(students[chk]['kor'],students[chk]['eng'],students[chk]['math'],
                              students[chk]['total'],students[chk]['avg'])
                         break          
               
              
     elif choice == 4:
          print('학생수정을 선택하셨습니다')
          s_title = ['','국어','수학','영어']
          while True:
               search = input('찾고자 하는 학생 이름을 입력해주세요 (0.취소 )>> ')
               chk = 0
               if search == '0':
                    print('수정을 취소합니다')
                    break
               for s_dic in students:
                    if s_dic['name'] ==search:
                         break
                    chk += 1
               if chk == len(students):
                    print('찾는 학생이 없습니다. 다시 확인해주세요')
               else:
                    print(f'{search} 학생을 찾았습니다.')
                    while True:
                         print('1.국어 2. 수학 3. 영어 ')
                         s_input = int(input('수정할 과목을 입력해주세요 >> '))
                         if s_input == 1 :
                              s_1 = 'kor'
                              score = int(input('수정할 점수를 입력해주세요 >> '))
                              students[chk][s_1] = score
                              students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                              students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))      
                              print(f'{students[chk][s_1]} 점수로 변경되었습니다')
                         if s_input == 2 : 
                              s_2 = 'eng'
                              score = int(input('수정할 점수를 입력해주세요 >> '))
                              students[chk][s_2] = score
                              students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                              students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3)) 
                         if s_input == 3 :
                              s_3 = 'math'
                              score = int(input('수정할 점수를 입력해주세요 >> '))
                              students[chk][s_3] = score
                              students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                              students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))           
                              
     elif choice == 5:    
          
          print('등수처리를 선택하셨습니다')  
          for i,  s_dic in enumerate(students):
             rank_cnt = 1            
          for i_dic in students:
               if s_dic['total']>i_dic['total']:
                    rank_cnt += 1
          s_dic['rank']=rank_cnt
          
          print('등수처리가 완료되었습니다')
          print(students, sep = '\t')
          
     elif choice == 6:
          print('학생삭제를 선택하셨습니다.')
          while True:
               search_name = input('찾고자 하는 학생의 이름을 입력해주세요 (0. 취소 >>)')
               chk = 0
               if search_name == '0':
                    break
               for s_dic in students:
                   if s_dic['name'] == search_name:
                    break 
               
               if search_name == len(students):
                    print('찾으시는 학생이 없습니다.이름을 다시 확인해주세요')
               else:
                    print(f'{search_name} 학생을 찾았습니다')
                    s_input = input('성적을 정말 삭제 하시겠습니까? (0.취소 1. 실행) >>')
                    if  s_input == '0':
                         print('성적삭제를 취소합니다')
                         break
                    elif s_input == '1':
                         del students[chk]
                         print('성적을 삭제 합니다')
                         
               
                                     
                