# 변수 종류 
# bool, int, float, string
# 데이터베이스 프로그램

students = []# 학생성적저장
students = [[1,'홍길동',100,100,99,299,99.67,1],[2,'유관순',90,90,90,270,90.0,1],
            [3,'이순신',80,80,80,240,80.0,1],[4,'김구',70,70,70,210,70.0,1],
            [5,'이이',60,60,60,180,60.0,1],[6,'강감찬',50,50,50,150,50.0,1]]
cnt = len(students) # 학번 사용
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1.학생성적입력')
    print('2.학생성적전체출력')
    print('3.학생검색')
    print('4.학생수정')
    print('5.등수처리')
    print('6.학생삭제')
    print('0.프로그램종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >> ')
    if not choice.isdigit():
        print('숫자만 입력가능합니다.')
        continue # 반복문 다시 실행
    choice = int(choice)
    # 1. 학생성적입력프로그램
    
    if choice == 1:
        # 무한반복
        while True:# 학생성적 입력 시 다시 번호를 누르지 않고 입력가능하게 
            print('학생성적을 입력합니다.') 
            print('-'*40)
            student = [] # 이름, 국어, 영어, 수학
            name = input('이름을 입력하세요 ( -1. 취소 )>> ')
            if name == '-1':
                break
            cnt += 1 # 학번
            student.append(cnt) # 학번
            student.append(name) # 0
            student.append(int(input('국어 점수를 입력해주세요 >> '))) # 1
            student.append(int(input('영어 점수를 입력해주세요 >> '))) # 2
            student.append(int(input('수학 점수를 입력해주세요 >> '))) # 3
            sum = student[2]+student[3]+student[4] #total = [kor, eng, math]
            # 합계저장
            student.append(sum) # student.append(sum)
            # 평균저장
            student.append('{:.2f}'.format(sum/3)) #student.append(avg)
            students.append(student)   
        # print(students)
        
    # 2. 학생성적출력 프로그램
    elif choice == 2:
        print('[ 학생성적 출력 ]')
        print('-'*50)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        print('-'*50)
        # 2차원 리스트는 for문을 2번 사용. 

        for stu in students:
            for s in stu:
                print(s, end = '\t')
            print()
        print()
        print('-'*50)

        chk = 0 #정보확인 #변수1
        count  = 0       #변수2   
    # 학생성적 검색  
    elif choice == 3:
        while True:
            search = input('검색하고 싶은 학생을 입력해주세요.(0. 취소 )>> ')
            if search == '0':
                break
            for stu in students: #홍길동 유관순 이순신 
                if search in stu:
                    chk =1 #정보를 찾았을때 정보를 1로 변경
                    break
                count += 1
                if search in stu:
                    break
            
            if chk == 1:
                print('[{} 학생정보출력]'.format(search))
                print('-'*50)
                print('{}의 학생 정보를 찾았습니다'.format(search))
                # 전체 학생 정보출력   
                print('[ 학생성적 출력 ]')
                print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
                print('-'*50)         
                for i in students[count]:
                    print(i, end= '\t')
                print()
                
            else:    
                print('찾는 학생이 없습니다.')
   # 4. 학생 성적 수정
        while True:
            search = input('찾는 학생의 이름을 입력하세요. >> ')
            chk = 0 
            count = 0 # 찾는 학생의 위치값
            for stu in students:
                if search in stu:
                    chk = 1
                    break
                count += 1 # 찾는 학생의 위치값 
            if chk == 0:
                print('찾는 학생의 정보가 없습니다.')
            else:
                print('입력한 학생 {}을 찾았습니다.'.format(search))
                print('[변경할 과목 선택]')
                print('-'*20)
                num = int(input('1.국어 2.영어 3. 수학 0.취소 >> '))
                if num == 1:
                    print('국어를 선택하셨습니다.')
                    print('현재 국어 점수 : ',students[count][2])
                    num = int(input('국어 변경 점수를 입력하세요.>> '))
                    students[count][2] = num
                    print('국어 점수가 변경되었습니다.')
                    #합계, 평균 수정
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                
                    students[count][6] ='{:.2f}'.format(students[count][5]/3)
                    print(students)
                    #성적 수정 프로그램 구현
                    
                    
                
                elif num == 2:
                    print('영어를 선택하셨습니다.')
                    print('현재 영어 점수 : ',students[count][3])
                    num = int(input('영어 변경 점수를 입력하세요.>> '))
                    students[count][3] = num
                    print('영어 점수가 변경되었습니다.')
                    #합계, 평균 수정
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                
                    students[count][6] =float('{:.2f}'.format(students[count][5]/3))
                    print(students)
                    #성적 수정 프로그램 구현
                
                elif num == 3:
                    print('수학을 선택하셨습니다.')
                    print('현재 수학 점수 : ',students[count][4])
                    num = int(input('수학 변경 점수를 입력하세요.>> '))
                    students[count][4] = num
                    print('수학 점수가 변경되었습니다.')
                    #합계, 평균 수정
                    students[count][5] = students[count][2]+students[count][3]+students[count][4]
                
                    students[count][6] = float('{:.2f}'.format(students[count][5]/3))
                    #성적 수정 프로그램 구현
                    print(students)
                elif num == 0:
                    print('취소를 선택하셨습니다.')            
    elif choice == 5:
        while True:
            choice = input ('등수처리를 실행하겠습니까? (1.실행 0.취소)')
            if choice == '0':
                print('등수처리를 취소하셨습니다.')
                break
            else:
            # 등수처리 진행
                for i, i_stu in students:
                    no = 1 #초기화
                    for j,j_stu in students:
                        if i_stu[5] < j_stu[5]:
                            no =+ 1 #비교대상이 총합이 더 크면 1증가
                        i_stu[7] = no # 등수위치에 no 저장
                        print('등수처리가 완료되었습니다')
                        print('-'*40)
                        print('[ 등수확인 ]')
                        print(students)            
    elif choice == 6:
        while True:
            #강감찬
            search = input('삭제하려는 학생이름을 입력하세요>> (0.취소)')
            
            #이름찾기
            cnt = 0 # 찾은 학생의 위치
            #전체 학생 검색
            for stu in (students): # 무조건 5번을 돌게 됨
                if stu[1] == search:
                    break    #break만 넣게 되면 첫번째는 가능, 그 다음부터 ㄴㄴ-> cnt추가
                cnt += 1 #강감찬을 넣게 되면, 0 1 2 3에서 찾을 수 없음 4에서 발견
            if cnt == len(students): # 0-4에서 찾지 못하면 5까지 가게 됨
            
                print('{} 학생이 없습니다.'.format(search))
            else :
                choice = input('{}학생을 찾았습니다. 삭제하시겠습니까?(0.취소 1. 삭제)'.format(search))
                if choice =='1':
                    print('{}학생의 데이터가 삭제되었습니다'.format(search))
                    del students[cnt]
                else :
                    print('삭제가 취소되었습니다.')
            
            print(students)
            print('-'*40)                                           
                
                
            
        
    # 0. 프로그램 종료
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break # 반복문 종료
   
