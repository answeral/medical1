students = [] 
cnt = 0 
i = 0
while True:
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1.학생성적입력') #이름, 국, 영, 수 점수를 입력 받으면 [번호, 이름,국,영,수,총합,평균,0]
    print('2.학생성적수정')# 국,영,수 점수를 수정해 볼 수 있음 유의 : 국어 성적을 받으면 평균도 바뀜
    print('3.학생성적 삭제')
    print('4.학생성적전체출력') #전체 출력
    print('5.학생성적검색출력') 
    print('6.등수처리')
    print('0.프로그램 종료') #종료
    print('-'*35)
    choice = int(input('원하는 번호를 입력하세요 >> '))
    print('입력하신 번호는 {}입니다'.format(choice))
    
    if choice == 1:
        print('학생성적입력입니다 ')
        name = input('이름을 입력해주세요 >> ')
        kor = int(input('국어 성적을 입력해주세요 >> '))
        eng = int(input('영어 성적을 입력해주세요 >> '))
        math = int(input('수학 성적을 입력해주세요 >> '))
        total = (kor + eng+ math)
        avg = total/3
        i += 1
        l = [i,name, kor, eng, math, total, avg]
        students.append(l)    
    
    if choice == 2: # =students=[[1. 홍길동, 100,100,100,300,100.0] [2. 유관순, 90,90,90,270,90.0]]
        print('학생성적수정입니다')
        rename = input('수정할 학생의 이름을 입력해주세요 >> ')
        print('입력하신 학생의 이름은 {} 입니다. '.format(rename))
        
        
        
    if choice == 3:
        print('학생성적삭제입니다')
        pass
    
    
    
                  #              00    01    02  03  04  05  06     10  11     12 13 14 15  16
    if choice == 4: # =students=[[1. 홍길동, 100,100,100,300,100.0] [2. 유관순, 90,90,90,270,90.0]]
        print('학생성적전체출력입니다')
        for i in range(len(students)):
            print(students[i][0],students[i][1],students[i][2],students[i][3],students[i][4],
                  students[i][5],students[i][6])
    
    if choice == 5:
        print('학생성적검색출력입니다')
        searchname = input('검색하실 학생의 이름을 입력해주세요 >> ')
        print('검색하신 학생의 이름은 {} 입니다'.format(searchname))
        print('번호\t이름\t국어\t수학\t영어\t총점\t평균')
        for i, stu in enumerate(students):
            if searchname in stu:
                print(students[i][0],students[i][1],students[i][2],students[i][3],students[i][4],
                  students[i][5],students[i][6]) 
    
    
    
    if choice == 6:
        print('등수처리')
    if choice == 0:
        print('프로그램을 종료합니다')
        break
            
            
        
        
