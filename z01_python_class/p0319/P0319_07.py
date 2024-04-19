class Students:
     count = 1
     def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
          self.name = name
          self. kor = kor
          self. eng = eng
          self. math = math
          self. total = kor + eng + math
          self. avg = float('{:.2f}'.format(self.total/3))
          self.rank = rank
          if stuNo == 0:
               self.stuNo = Students.count
          else:
               self.stuNo = stuNo 
               
     def __str__(self):
          return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}]t{self.rank}"

student = []     

f = open('stu.txt','r',encoding='utf8')
while True:
     txt = f.readline()
     if txt =='':break
     txt_list = txt.split(',')
     # 1,홍길동,99,99,87,285,95.0,1 # 클래스랑 순서 맞춰서
     s = Students(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]))
     student.append(s)
f.close()
     
     
print("-"*40)
print("[ 학생성적프로그램 ]")
print("-"*40)
print("1. 학생성적입력")
print("2. 학생성적전체출력")
print("3. 학생검색")
print("4. 학생성적수정")
print("5. 학생성적삭제")
print("6. 학생등수처리")
print("0. 종료")
print("-"*40)
choice = input("원하는 번호를 입력하세요.>> ")
choice = int(choice)
while True:
     if choice == 1:
          print('학생성적 입력입니다. ')
     
          name = input(f'{len(student)+1} 학생의 이름을 입력하세요. (0. 취소)')
          if (name == '0'):
               print('입력을 취소합니다.')
               break
          kor = int(input('국어성적을 입력해주세요. >> '))
          eng = int(input('영어성적을 입력해주세요. >> '))
          math = int(input('수학성적을 입력해주세요. >> '))
          s = Students(name,kor,eng,math)
          student.append(s)
          print('입력데이터 : ' , s)
               
     
     elif choice == 2:
          print('-'*70)
          print('[ \t학생성적전체출력\t ]')
          print('-'*70)
          print("학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수" )
          for i in student:
               print(i)
          break
     
     elif choice == 3 :
          print("-"*40)
          print("\t[ 학생성적 검색 ]")
          print("-"*40)
          print("1. 학생이름으로 검색")
          print("2. 총점이상 검색")
          print("3. 총점이하 검색")
          print("0. 이전화면 이동")
          print("-"*40)
          # 검색할 학생 이름 입력
          choice = int(input("원하는 번호를 입력해주세요. >>"))
          # 학생 대조
          s_list = []
          if choice == 1:
               search = input('학생 이름을 입력해주세요. >> ')
               for i in student:
                    if i.name.find(search) != -1:
                         s_list.append(i)
                         
          elif choice ==2:
               search = int(input('점수를 입력해주세요. >> '))
               for i in student:
                    if i.total >= search:
                         s_list.append(i)
                         
          elif choice == 3:
               search = int(input("점수를 입력해주세요. >> "))
               for i in student:
                    if i.total <= search:
                         s_list.append(i)
          elif choice == 0:
               print('초기화면으로 돌아갑니다')               
                         
          if len(s_list) != 0:
               for i in s_list:
                    print(i)
          else:
               print("찾고자 하는 학생이 없습니다. 다시 검색하세요.")
                    
     elif choice == 4: # 학생성적수정
          # 1.  학생 이름 찾기
          search = input("성적 수정할 학생의 이름을 입력해주세요. >> ")
          cnt = 0
          # 1.1 학생의 이름을 student리스트에서 찾기 (for문으로!!!)
          for i in student:
               if i.name == search:
                    break
               cnt += 1
               
          if cnt >= len(student):
               print('찾고자 하는 학생이 없습니다. 다시 입력해주세요')
               
          else:
               print(f"{search} 학생을 찾았습니다.")
          # 성적 수정 하기
          print("수정할 과목을 선택새주세요.")
          print('1. 국어 성적 수정')
          print('2. 영어 성적 수정')
          print('3. 수학 성적 수정')
          choice = int(input("원하는 번호를 입력해주세요. >> "))
          if choice == 1:
               print("국어성적을 수정합니다.")
               print(f" 변경 전 국어 점수 : {student[cnt].kor}")
               student[cnt].kor = int(input("변경할 국어점수를 입력해주세요. >> "))
               student[cnt].total = student[cnt].kor + student[cnt].eng + student[cnt].math
               student[cnt].avg = float("{:.2f}".format(student[cnt].total/3))
               print(f"{student[cnt].kor}로 점수가 변경되었습니다.")
               
          if choice ==2:
               print("영어 성적을 수정합니다.")
               print(f"변경 전 영어 점수 :{student[cnt].eng}")
               student[cnt].eng = int(input("변경할 영어 점수를 입력해주세요. >> "))
               student[cnt].total = student[cnt].kor + student[cnt].eng + student[cnt].math 
               student[cnt].avg = float('{:.2f}'.format(student[cnt].total/3))
               
          if choice == 3:
               print("수학 성적을 수정합니다.")
               print(f"변경 전 수학 점수 :{student[cnt].math}")   
               student[cnt].eng = int(input("변경할 영어 점수를 입력해주세요. >> "))
               student[cnt].total = student[cnt].kor + student[cnt].eng + student[cnt].math 
               student[cnt].avg = float('{:.2f}'.format(student[cnt].total/3))
               
     elif choice == 5: # 학생성적삭제
          # 삭제할 학생 검색
          search = input("삭제할 학생의 이름을 입력해주세요. >> ")
          cnt = 0
          for i in student:
               if i.name(search) == search:
                    break
               cnt += 1
               
          if cnt >= len(student):
               print('삭제하고자 하는 학생이 없습니다.')
               
          else:  
               print(f"{search} 학생을 찾았습니다.")
               print('[ 학생 성적 삭제]')
               print('-'*80)
               
               print("1. 삭제")
               print("0. 취소")
               choice = int(input("원하는 번호를 입력해주세요. >> "))
               if choice == 1:
                    print(f"{search} 학생의 성적을 삭제합니다.")
                    del student[cnt]
                    
               else:
                    print("학생성적삭제를 취소합니다.")
               
     elif choice== 6: # 학생등수처리
          pass          
                         
                            
                    
          
          
          
                    
          
             
          
                    
          
          
                    