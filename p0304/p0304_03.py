# 이름, 국어, 영어, 수학을 입력받아
# 합계를 출력하시오.
# 2명의 학생의 국어, 영어 수학을 입력받아 합계를 출력하세요
kor = []
eng = []
math = []
total = []

students = []                         #2차원까지만 리스트를 사용하는 것이 좋음
for i in range(2):
    
    student = [] # 이름, 국어, 영어, 수학 00 01 02 03 0// 10 11 12 13/ 20 21 22 23
    student.append(input('이름을 입력하세요 >> ')) # 0
    student.append(int(input('국어 점수를 입력해주세요 >> '))) # 1
    student.append(int(input('영어 점수를 입력해주세요 >> '))) # 2
    student.append(int(input('수학 점수를 입력해주세요 >> '))) # 3
    sum = student[1]+student[2]+student[3]
    student.append(sum)
    student.append('{:.2f}'.format(sum/3))
    # 합계
students.append(student)


# 전체학생출력
print('[ 학생성적 출력 ]')
print('-'*50)
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*50)
# 2차원 리스트는 for문을 2번 사용. 

for stu in students:
    for s in stu:
        print(s, end = '\t')
    print()
print()
print('-'*50)
# 총 학생의 총 국어점수, 영어점수, 수학점수, 총합계, 총평균
# 3명의 국어점수 합계, 평균을 출력하시오.
kors = 0  
engs = 0
maths = 0
totals = 0
avgs = 0

for i, stu in enumerate(students):
    kors += int(stu[1]) #stu의 배열이 1차원이기때문에 [] 한개 사용
    engs += int(stu[2])
    maths += int(stu[3])
    totals +=int(stu[4])
avgs = totals/len(students)
print('\t')
print(kors,engs,maths,totals,avgs,sep='\t')
# 관리가 어렵기때문에 묶기... grooping?

#  print('합계 : ',kor + eng + math)



