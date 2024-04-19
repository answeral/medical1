students =[['홍길동',100,100,100,300,100],['유관순',90,90,90,270,90.0],
           ['이순신',80,80,80,240,80.0]]


#찾고자 하는 학생찾기

while True:
    search = input('검색하고 싶은 학생을 입력해주세요.(0. 취소 )>> ')
    chk =0
    if search == '0':
        break
    for stu in students:
        if stu[1] == search:
            print('{}의 학생정보를 찾았습니다'.format(search))
    else:    
        print('찾는 학생이 없습니다.')
            
          
