
member = []
i=0
#이름만 입력을 받아서, member =[[1.홍길동][2.유관순][3.이순신]]
while True:
    print('-'*25)
    print('1.입력')
    print('2. 전체출력')
    print('3. 검색출력')
    print('4. 검색삭제')
    print('5. 수정')
    print('0. 종료')
    ch = input('원하는 번호를 선택하세요 >> ')
    print('-'*25)
    ch = int(ch)
    if ch == 1:
        print('입력')
        name = input('이름을입력해주세요')
        i += 1
        m = [i,name]
        member.append(m)
    
    
    elif ch ==2:
        print('전체출력')
        # print(member)
        # 번호 이름
        #  1 00  홍길동01
        #  2 10   유관순 11
        for i in range(len(member)):
            print(member[i][0],member[i][1])
   
    # member =[[1.홍길동][2.유관순][3.이순신]]
    elif ch == 3: # 검색출력
        print('검색출력 ')
        searchname = input ('검색하고 싶은 이름을 입력해주세요 >> ')
        print('번호\t이름')
        for i,  m in enumerate(member):
            if searchname  in m:
                print(member[i][0],member[i][1])
            
    elif ch ==4:
        delname = input('삭제하고 싶은 이름을 입력해주세요 >> ')
        
        for i, m in enumerate(member):
            if delname in m:
                del(member[i])
                print('{}님이 삭제되셨습니다'.format(delname))
    
    # member =[[1.홍길동][2.유관순][3.이순신]]            
    elif ch == 5: #누구의 정보를 수정할지 갖고 있는 정보는 번호와 이름, 번호를 수정할건지, 이름을 수정할거니
                  #만약에 번호를 수정한다면 수정값 입력, 이름을 수정한다면 이름도 입력받아야함 
        print('수정입니다')
        rename1 = input('수정할 학생의 이름을 입력해주세요 >> ')
        for i , rename1 in enumerate(member): # member =[[1.홍길동][2.유관순][3.이순신]] 
            if rename1 in m:
             print(rename1,'님을 선택하셨습니다')
             ch_num = input('수정하고 싶은 항목을 선택해주세요 (1. 번호수정 2.이름수정)>>')
            if ch_num == '1':
                 print(rename1 ,'님의 번호수정을 선택하셨습니다')
                 print(rename1,'님의 번호는',member[i][0],'입니다')
                 stu_num = input('새로운 번호를 입력해주세요 >>')
                 stu_num = int(stu_num)
                 member[i][0] = stu_num
            elif ch_num =='2':
                print(rename1, '님의 이름수정을 선택하셨습니다')
                print(rename1,'님의 이름는',member[i][1],'입니다')
                stu_name = input('새로운 이름을 입력해주세요 >>')
                member[i][1] = stu_name
            else:
                print('잘못입력하셨습니다')
                break
    elif ch == 0:
        print('종료')
        break
    else:
        print('다시입력')
        
