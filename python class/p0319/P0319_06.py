stu = [
     ['홍길동',100],  # 0번방 [0]
     ['유관순',87],   # 1번방 [0]
     ['김구',88],     # 2번방 [0]
     ['김유신',43],   # 3번방 [0]
     ['이순신',56] ,  # .... 
     ['강감찬',82]  , # i번방 [0]
     ['홍길순',92],
     ['홍길자',70]
]

# 이름으로 검색해서 홍이 들어가는 사람을 모두 검색해서 출력하시오.
# 이름으로 검색해서 신이 들어가는 사람을 모두 검색해서 출력하시오.

while True:
     print('[  학생 성적 검색 ]')
     print('1. 이름으로 검색')
     print('2. 점수 검색')
     choice = int(input('원하는 번호를 입력하세요. >> '))
     
     if choice == 1:
          search= input('찾고자 하는 학생 이름을 입력하세요. >> ')
          search_list =[] # 1차원
          cnt = 0

          for s in stu:
               if search in s[0] != -1: # -1은 없다 
                    search_list.append(cnt)
               cnt +=1
               
               if search ==len(search_list):
                    print('찾는사람이 없습니다.')  
                    break
               else:
                    for i in search_list:
                         print(stu[i][0], end ='\t')    
     
     elif choice ==2:
          score = int(input('몇 점이상을 검색하시겠습니까 >> '))
          # 80 점이상인 사람의 이름을 출력하기
          s_list = []
          cnt = 0
          for s in stu:
               if score <= s[1]:
                    s_list.append(cnt)
               cnt += 1
               
          if len(s_list)== 0:
               print(f"{score} 보다 큰 점수는 없습니다.8 ")
               break
          else:
               print(f"{score} 보다 큰 점수 : ",end='')
               for i in s_list:
                    print(stu[i][0],stu[i][1], end=" ")
               print()
               print()
          
     
     
     
        
                      
                         
              
               
               
               
     


