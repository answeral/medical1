# 성적 부분 함수
def score_update(choice,s_title,student):
     print(f' [ {s_title[choice]} 성적 수정 ] ')
     print(f'현재 {s_title[choice]} 성적 : ',student[choice+1])
     print('-'*60)
     student[choice+1] = int(input('수정 점수를 입력하세요 >> '))  
     print('수정된 점수 : ',student[choice+1])
     student[5]=student[2]+student[3]+student[4] # 합계 수정
     student[6] = float('{:.2f}'.format(student[5]/3)) # 평균 수정
     print(f'{s_title[choice]}점수가 수정되었습니다') 
     return(choice,s_title,student)
# 학생성적수정함수
def stu_update(choice,s_title,student): 
     print(' [ 학생성적수정 ] ')
     print('1. 국어 2. 영어 3. 수학')
     choice = int(input('원하는 번호를 입력하세요 >> '))
     if choice == 1:
          score_update(choice,s_title,student)

     elif choice == 2:
         score_update(choice,s_title,student)
          
     elif choice == 3:
         score_update(choice,s_title,student)
 

