
student = [[1,'홍길동',100,100,100,300,100.0,1],[2,'유관순',90,90,90,270,90.0,2]]

print('-'*35)
print('\t[학생성적 프로그램]')
print('1.학생성적입력') #1명만 입력 print(student)
print('4.학생성적전체출력') #2명 출력
print('-'*35)

nm = input("추가할 학생의 이름을 입력하세요 >>")
kor = int(input(" 국어 성적을 입력해주세요 >> ")) 
eng = int(input(" 영어 성적을 입력해주세요 >> ")) 
math = int(input(" 수학 성적을 입력해주세요 >> ")) 
total = kor+eng+math
avg = total/3
pr = 3

stu3 = [3, nm, kor, eng, math, total, avg, pr]
student.append(stu3)
print(student)

ch = int(input('원하는 번호를 입력하세요 >>'))
name = input("학생의 이름을 입력하세요 >>")
if ch ==1 :
   if name =='홍길동':
      print(student[0])
   if name == '유관순':
       print(student[1])  
if ch == 4:
   print('[학생 성적 출력]')
   print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
   print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t 입니다'.format(student[0][0],student[0][1],student[0][2],
    student[0][3],student[0][4],student[0][5],student[0][6], student[0][7],))
   print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t 입니다'.format(student[1][0],student[1][1],student[1][2],
    student[1][3],student[1][4],student[1][5],student[1][6], student[1][7]))

'''
if ch == 1:
 print('[학생 성적 입력])
 nm = input("추가할 학생의 이름을 입력하세요 >>")
 kor = int(input(" 국어 성적을 입력해주세요 >> ")) 
 eng = int(input(" 영어 성적을 입력해주세요 >> ")) 
 math = int(input(" 수학 성적을 입력해주세요 >> "))  
stu1 = [3, name, kor, eng, math]

student.append(stu1)
print(student)
'''
