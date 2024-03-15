import stu_file
# stu.txt 파일 열기 호출
students = stu_file.stu_open()
s_title = ['','국어','영어','수학']


# 학생성적 화면 함수
def stu_main_print():
    
    print('-'*65)
    print('[학생성적프로그램]')
    print('-'*65)
    print('\t1. 학생성적 입력')
    print('\t2. 학생성적 전체출력')
    print('\t3. 학생검색')
    print('\t4. 학생수정')
    print('\t5. 등수처리')
    print('\t6. 학생삭제')
    print('\t7. 학생성적 파일저장')
    print('\t0. 프로그램 종료')
    print('-'*65)
    choice = input('원하는 번호를 입력하세요: >> ')
    print('-'*65)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
    choice = int(choice)
    return choice
        

# 학생성적입력 함수
def stu_insert(cnt):
    while True :
            name = input(f'{len(students)+1}번째 학생의 이름을 입력하세요 (0. 취소) >> ')
            if (name == '0'):
                print('학생입력을 취소하셨습니다.')
                break
            student = {}
            student['stuNo']= cnt
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
            
# 학생성적상단출력함수
def stu_top_print():
    print('\t[ 학생성적출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*65)
            

# 학생성적출력 함수
def stu_grade_print(stu_list):
    stu_top_print()
    for s_dic in stu_list:
        for s_key in s_dic:
            print(s_dic[s_key],end="\t")
        print()
    print('-'*65)
    print()

# 학생검색함수
def stu_search():
    # 학생검색 -> 이름으로 검색해서 해당하는 학생이 있으면 해당학생 성적출룍
        #1명 출력
        search_students = []
        print('[ 학생 성적 검색]')
        search = input('찾고자 하는 학생 이름을 입력하세요. >>')
        
        #검색한 이름으로 리스트에서 해당학생 검색
        search_cnt = 0 # 존재하면 1 존재하지 않으면 0?
        for s in students:
            if s['name'] == search:
                break
            search_cnt += 1
        
        if  len(students)== search_cnt:#10명이 존재 -> 9번까지있는데, 10번돌았으니 학생이 없음
            print('찾고자 하는 학생이 없습니다. 다시 검색해주세요')
            
        else:
            print(f'{search} 학생을 찾았습니다. 성적을 출력합니다.')
        
            # 한 명의 학생을 search_students 리스트에 추가    
            search_students.append(students[search_cnt]) #
            stu_grade_print(search_students)  # 학생성적출력 함수 호출
# 학생수정 검색
def stu_subject_update(s_input,chk, s_1):
    print('[ {} 수정 ]'.format(s_title[s_input]))#국어가 들어감 s_input = 1
    print('현재 {}점수 :{}'.format(s_title[s_input],students[chk][s_1]))
    print('-'*50)
    score = int(input('수정할 {} 점수를 입력하세요 >> '.format(s_title[s_input])))
    students[chk][s_1]=score
    #합계수정
    total =  students[chk][s_1]+students[chk][s_1]+students[chk][s_1]
    students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
    print(f'{s_title[s_input]}점수 {students[chk][s_1]}점으로 수정이 완료되었습니다.')
    print(students[chk])

#학생성적 수정 - 전체부분
def stu_update():
    while True:   
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
                s_title = ['','국어','영어','수학']
                while True:
                    s_input = int(input('수정하려는 과목을 선택하세요 (0. 취소 1. 국어2. 영어  3. 수학) >> '))
                    print('[수정할 과목선택]')
                
                    print('-'*50)
                    if s_input == 1:
                            s_1 = 'kor'
                            stu_subject_update(s_input,chk, s_1)
                            #함수호출
                            #s_update(s_1)
                            
                    elif s_input == 2:
                            s_1 = 'eng'
                            #함수
                            #s_update(s_1)
                            stu_subject_update(s_input,chk, s_1)
                    elif s_input == 3:
                            s_1 = 'math'
                            #함수
                            #s_update(s_1)
                            stu_subject_update(s_input,chk, s_1)
                    else:
                            print('과목 수정을 취소합니다')
                            break

# 학생등수처리 함수
def stu_rank():
    for i, s_dic in enumerate(students): #위치 파악 필요 enumerate 사용
        rank_cnt = 1 #등수처리 변수
    
        for i_dic in students:
            print(s_dic['total'])
            if s_dic['total']<i_dic['total']: #등수를 비교해서 
                rank_cnt += 1 # 현재학생의 합계보다 크면 1증가
        s_dic['rank'] = rank_cnt
     
        print('등수처리가 완료되었습니다')
        print(students)


# 학생삭제 함수
def stu_delete():
    while True:
     #먼저 학생찾기
        search = input('삭제 하고자 하는 학생의 이름을 입력해주세요 (0.취소) >> ')
        chk = 0
        if search == '0':
                print('학생찾기를 종료합니다')
                break
        for s_dic in students: #ex)다섯명이 있으면 5번반복 s_dic 키값 s_dic[]= value 값
            if s_dic['name']==search:
                break
            chk += 1
        print('찾고자 하는 학생의 위치 :' , chk)
        
        if chk >= len(students):
            print('찾고자 하는 학생이 없습니다.')
        else:
            print(f'{search}학생을 찾았습니다.')
            s_input = input(f'{search}학생의 성적을 삭제 하시겠습니까?(0. 취소 1. 실행) >> ')
            if s_input != '1':
                print('삭제를 취소합니다.')
                break
            else:
                del students[chk]
                print(f'{search}학생의 성적이 삭제 되었습니다')
                print(students)
          
#학생성적 파일 저장 함수 

# stu.file에 저장되어 있음

#------------------------------------------
#                프로그램시작
#--------------------------------------------




cnt = len(students)+1
# 학생번호 사용
while True:
    #학생성적화면함수 호출
    choice = stu_main_print()
    
    # 1. 학생성적입력 
    if choice == 1 :
        stu_insert(cnt) # 학생성적입력함수 호출
        stu_file.stu_save(students) # 학생성적 파일 저장 함수 호출
    # 2. 학생성적전체출력 프로그램
    elif choice == 2 :
        
        stu_grade_print(students) # 학생성적전체출력함수 호출

    elif choice == 3 :
        stu_search() # 학생성적검색함수 출력
        
       
    #4. 학생 수정    
    elif choice == 4:
        stu_update() #학생성적수정함수 호출
        stu_file.stu_save(students) # 학생성적 파일 저장 함수 호출
        
      #등수처리              
    elif choice == 5:
        
           stu_rank()
           stu_file.stu_save(students)  # 학생성적 파일 저장 함수 호출
        # 학생삭제
    elif choice == 6:
        stu_delete()
        stu_file.stu_save(students) # 학생성적 파일 저장 함수 호출
        # 학생성적 파일 저장  
    
    elif choice == 7:
        stu_file.stu_save(students)  # 학생성적 파일 저장 함수 호출
    
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break  # 반복문 종료
    else:
        print('선택된 서비스가 없습니다.')
        




