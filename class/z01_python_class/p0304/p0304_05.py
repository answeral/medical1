students =[[1,'홍길동',100,100,100,300,100],[2,'유관순',90,90,90,270,90.0],
           [3,'이순신',80,80,80,240,80.0]]


#찾고자 하는 학생찾기
chk = 0 #정보확인 #변수1
count  = 0       #변수2
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

