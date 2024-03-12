student = [] #여기에 저장하기

for i in range(5): #for 를 사용해서 5번 반복
 print('-'*35)
 print('\t [학생성적프로그램]')
 print('1.학생성적입력')
 print('4.학생성적전체출력')
 print('0.프로그램 종료')
 print('-'*35)
 ch = int(input ('원하는 번호를 입력하세요 >>'))
 print(ch)
 #if 문을 사용해서 1을 누르면 학생성적입력
 #4 누르면 [학생성적전체출력]
 #0 누르면 [프로그램 종료]
 if ch == 1:
     print('학생성적입력')# 이름, 국,영,수 점수를 입력받아
     name1 = input('이름을 입력해주세요 >>')
     kor = int(input('국어 점수를 입력해주세요 >>'))
     eng = int(input('영어 점수를 입력해주세요 >>'))
     math= int(input('수학 점수를 입력해주세요 >>'))
    
     stu1 = [name1, kor, eng, math]
     student.append(stu1)
     
 if ch == 4:
     print('[학생성적전체출력]') 
     print("이름\t 국어\t 수학 \t 영어 \t")
     for i in range(len(student)):
      print("{}\t {}\t {}\t {}\t".format(student[0][0], student[0][1], student[0][2],
            student[0][3]))
      
         
 if ch == 0:
     print('프로그램 종료')  
 else:
     print('잘못입력하셨습니다')
 
 print('*'*35)
 print('*'*35)        
print('프로그램이 종료되었습니다') 
