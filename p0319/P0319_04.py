# Student 클래스 생성, 파일불러와서 클래스에 저장 후 출력
class Student:
     count = 1
    
     def __init__(self,name, kor, eng, math, stuNo=0, rank=0):
          if stuNo == 0:
               self.stuNo = Student.count
          else:
               self.stuNo = stuNo
          
          self.name =name
          self.kor = kor
          self. eng = eng
          self. math = math
          self. total = kor + eng + math
          self. avg = float('{:.2f}'.format(self.total/3))
          self. rank = rank
          
               
     def __str__(self): 
          return f' 학생성적 : {self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}'
     

     
          
          
students = []          
f = open('stu.txt','r',encoding='utf8')
while True:
     txt = f.readline()
     if txt =='': break
     txt_list = txt.split(',')
     s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
     students.append(s)    
f.close()
# 파일 불러오기 한 후 학생수에서 +1 추가
Student.count = len(students)+1

# for stu in students:
#      print(stu)
#-------------------------------------------------------------------------     
while True:     
     print('-'*65)
     print('[학생성적프로그램]')
     print('-'*65)
     print('\t1. 학생성적 입력')

     print('\t0. 프로그램 종료')
     print('-'*65)
     choice = input('원하는 번호를 입력하세요: >> ')
     print('-'*65)
     if not choice.isdigit():
          print('숫자만 입력 가능합니다.')
     choice = int(choice)


 
     if choice == '1':   
          while True:   
               print('-'*65)
               print('[학생성적프로그램]')
               print('-'*65)
               print('\t1. 학생성적 입력')
               print('\t0. 프로그램 종료')
               print('-'*65)
               choice = input('원하는 번호를 입력하세요: >> ')
               print('-'*65)
               
               name = name = input(f'{len(students)+1}번째 학생의 이름을 입력하세요 (0. 취소) >> ')
               if name == '0':
                    print('입력을 취소합니다.')
                    break
               kor = int(input('국어 점수를 입력해주세요. >> '))  
               eng = int(input('영어 점수를 입력해주세요, >> '))
               math = int(input('수학 점수를 입력해주세요. >> '))
               # list에 추가
               s= Student(name,kor,eng,math)
               students.append(s)
               print('입력데이터 : ',Student)

     
          
          
     
     
          
          
          
          
          
         
               

       


     
                  
          
               