students =[
     {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

subject = ['순번','학번','국어','영어','수학','합계','평균','등수']
s_title = ['','국어','영어','수학']
cnt = len(students)+1 #학번

     
while True:
     #먼저 학생찾기
     search = input('찾고자 하는 학생의 이름을 입력해주세요 (0.취소) >> ')
     chk = 0
     if search == '0':
               print('학생찾기를 종료합니다')
               break
     for s_dic in students: #ex)다섯명이 있으면 5번반복 s_dic 키값 s_dic[]= value 값
          if s_dic['name']==search:
               break
          chk += 1
     print('찾고자 하는 학생의 위치 :' , chk)
     
     if chk == len(students): #학생수만큼 for문을 돌면 = 존재하지않는다
          print(f'{search}학생이 존재하지 않습니다. 다시 입력하세요.')     
     else:
          print(f'{search}학생을 찾았습니다')
          while True:
               s_input = int(input('수정하려는 과목을 선택하세요 (0. 취소 1. 국어2. 영어  3. 수학) >> '))
               print('[수정할 과목선택]')
          
               print('-'*50)
               if s_input == 1:
                    s_1 = 'kor'
                    #함수호출
                    #s_update(s_1)
                    print('[ {}수정 ]'.format(s_title[s_input]))#국어가 들어감 s_input = 1
                    print('현재 {}점수 :{}'.format(s_title[s_input],students[chk][s_1]))
                    print('-'*50)
                    score = int(input('수정할 {} 점수를 입력하세요 >> '.format(s_title[s_input])))
                    students[chk][s_1]=score
                    #합계수정
                    total =  students[chk][s_1]+students[chk][s_2]+students[chk][s_3]
                    students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
                    print(f'{s_title[s_input]}점수 {students[chk][s_1]}점으로 수정이 완료되었습니다.')
                    print(students[chk])
               elif s_input == 2:
                    s_2 = 'eng'
                    #함수
                    #s_update(s_1)
                    print('[ {}수정 ]'.format(s_title[s_input]))#국어가 들어감 s_input = 1
                    print('현재 {}점수 :{}'.format(s_title[s_input],students[chk][s_1]))
                    print('-'*50)
                    score = int(input('수정할 {} 점수를 입력하세요 >> '.format(s_title[s_input])))
                    students[chk][s_1]=score
                    #합계수정
                    total =  students[chk][s_1]+students[chk][s_2]+students[chk][s_3]
                    students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
                    print(f'{s_title[s_input]}점수 {students[chk][s_1]}점으로 수정이 완료되었습니다.')
                    print(students[chk])
               elif s_input == 3:
                    s_3 = 'math'
                    #함수
                    #s_update(s_1)
                    print('[ {}수정 ]'.format(s_title[s_input]))#국어가 들어감 s_input = 1
                    print('현재 {}점수 :{}'.format(s_title[s_input],students[chk][s_1]))
                    print('-'*50)
                    score = int(input('수정할 {} 점수를 입력하세요 >> '.format(s_title[s_input])))
                    students[chk][s_1]=score
                    #합계수정
                    total =  students[chk][s_1]+students[chk][s_2]+students[chk][s_3]
                    students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
                    print(f'{s_title[s_input]}점수 {students[chk][s_1]}점으로 수정이 완료되었습니다.')
                    print(students[chk])
               else:
                    print('과목 수정을 취소합니다')
                    break
               
# #함수 선언
# def s_update(s_1):  
#      print('[ 국어수정 ]'.format(s_title[s_input]))#국어가 들어감 s_input = 1
#      print('현재 {}점수 :{}'.format(s_title[s_input],students[chk][s_1]))
#      print('-'*50)
#      score = int(input('수정할 {} 점수를 입력하세요 >> '.format(s_title[s_input])))
#      students[chk][s_1]=score
#      #합계수정
#      total =  students[chk][s_1]+students[chk][s_2]+students[chk][s_3]
#      students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
#      print(f'{s_title[s_input]}점수 {students[chk][s_1]}점으로 수정이 완료되었습니다.')
#      print(students[chk])             
          

          
          
          