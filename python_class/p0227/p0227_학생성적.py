student = []
for i in range(3) :
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1.학생성적입력') 
    print('4.학생성적전체출력') 
    print('0. 종료')
    print('-'*35)
    ch = int(input('원하는 번호를 입력하세요 ')) 
    if ch ==1:
        print('[학생 성적 입력]')
        name = input('이름을 입력하세요 >>')
        kor = int(input('국어 성적을 입력하세요 >>'))
        eng = int(input('영어 성적을 입력하세요 >>'))
        math = int(input('수학성적을 입력하세요 >>'))
        total = (kor +eng + math)
        avg = total/3
        stu = [name, kor, eng, math, total, avg]
        student.append(stu)
    elif ch == 4:
       print('이름\t국어\t영어\t수학\t총점\t평균')
    for i in range(len(student)):
       print('{}\t{}\t{}\t{}\t{}\t{}'.format(student[i][0], student[i][1], 
                                          student[i][2],student[i][3],student[i][4],
                                          student[i][5]))
    if ch == 0:
        print('프로그램을 종료합니다.')
    else:
        print('입력하신 숫자를 다시 확인해주세요.')
        
     