students = []
student = []
cnt = len(students) # 학생수만큼 카운트 되어야함

while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생정렬')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >> (0.종료)')
    
    choice = int(choice)    
    if choice == 1:
        while True:
            print('학생성적을 입력해주세요 >>')
            student= []
            student.append(cnt)
            name = input('이름을 입력하세요 >> (0.취소)')
            student.append(name)
            if name == '0':
                break
            kor = int(input(' 국어 성적을 입력하세요 >>'))
            eng = int(input('영어 성적 >> '))
            math = int(input('수학 성적 >> '))
            total = kor + eng + math
            avg = total / 3
            student = [cnt, name, kor, eng, math, total, avg]
            student.append('{:.2f}'.format(avg))
            student.append(1)
            students.append(student)
            cnt = +1
    
    elif choice == 2:
        print('[학생전체출력]')
        print('-'*55)
        print('학번\t 이름\t 국어\t 영어\t 수학\t 합계\t 평균')
        print('-'*55)
        for stu in students:
            for s in stu:
                print(s, end = '\t')
        print()
    
    elif choice == 3:
        print('[학생검색]')
        print('-'*55)
        
        while True:
            search = input('검색하고 싶은 학생의 이름을 입력해주세요 (0.종료) >>')
            chk = 0        
            count = 0
            if search == '0':
                print('학생검색을 종료합니다')
                break
            
            for stu in students:
                if  search in stu:
                    chk = 1
                    break
                count += 1
            if chk == 0:
                print('찾는 학생이 없습니다. 학생검색을 종료합니다')
            
            if chk == 1:
                print(f'{search}의 학생정보를 찾았습니다')   
                print('-'*50)
                print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
                for i in students[count]:
                    print(i, end = '\t')
                    
    elif choice == 4:
        print('학생수정입니다')
        while True:
            search = input('수정할 학생의 이름을 입력해주세요.(0.종료) >> ')
            if search == '0':
                print('학생수정을 종료합니다')
                break
            chk = 0
            count = 0
            
            for stu in students:
                if search in stu:
                    chk = 1
                    break
                count += 1
            
            if chk == 0:
                print('찾는 학생이 없습니다')
            else:
                print(f'{search} 학생의 정보를 찾았습니다.')
                num = int(input('수정을 원하시는 과목의 번호를 눌러 주세요 . 1.국어 2. 수학 3. 영어 >> '))
                if num == 1:
                    print('국어성적수정선택')
                    print(f'{search}님의 국어 성적은 {students[count]}점입니다.')
                    rekor = int(input('수정할 국어점수 입력>>'))
                    students[count][2] = rekor
            
            
                     
                
        
                 
            
            
    
                                