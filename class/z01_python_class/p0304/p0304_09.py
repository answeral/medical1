students = [[1,'홍길동',100,100,99,299,99.67,1],[2,'유관순',90,90,90,270,90.0,1],
            [3,'이순신',80,80,80,240,80.0,1],[4,'김구',70,70,70,210,70.0,1],
            [5,'강감찬',50,50,50,150,50.0,1]]

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
    if cnt == len(students): # 0-4에서 찾지 못하면 5까지 가게 됨 # 전체 학생 수
    
        print('{} 학생이 없습니다.'.format(search))
    else :
        print('{}학생을 찾았습니다'.format(search))
        
    print('찾은 위치 :', cnt)
    del students[cnt]
    print(students)
    print('-'*40)
            