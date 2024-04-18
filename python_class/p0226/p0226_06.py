
student = []
# 튜플 (), 딕셔너리 {}, 리스트[]
#두 명 이상의 학생의
# 이름, 국, 영 수 점수를 입력받아
# 리스트를 생성 후,
#student리스트에 넣어주세요
# 리스트 넣는 방법 

''' 리스트 넣는 방법 3
stu1 = []로 설정 후 아래 사용 할 경우 오류 발생
stu1 = ['',0,0,0]#기본값 설정 길이 설정
stu1[0]= input('첫번째 학생의 이름을 입력해주세요 >>')
stu1[1]= int(input('첫번째 학생의 국어 점수를 입력해주세요 >>'))
stu1[2]= int(input('첫번째 학생의 영어 점수를 입력해주세요 >>'))
stu1[3]= int(input('첫번째 학생의 수학 점수를 입력해주세요 >>'))
'''
#studnet 리스트 전체 출력

name1 = input('첫번째 학생의 이름을 입력해주세요 >>')
kor1 = int(input('첫번째 학생의 국어 점수를 입력해주세요 >>'))
eng1 = int(input('첫번째 학생의 영어 점수를 입력해주세요 >>'))
math1 = int(input('첫번째 학생의 수학 점수를 입력해주세요 >>'))
total1 = kor1 + eng1 + math1
avg1 = total1/3

stu1 = [name1, kor1, eng1, math1, total1, avg1 ]

name2 = input('두번째 학생의 이름을 입력해주세요 >>')
kor2 = int(input('두번째 학생의 국어 점수를 입력해주세요 >>'))
eng2 = int(input('두번째 학생의 영어 점수를 입력해주세요 >>'))
math2 = int(input('두번째 학생의 수학 점수를 입력해주세요 >>'))
total2 = kor2 + eng2 + math2
avg2 = ('%.2f')%float(total2/3)

stu2 = [name2, kor2, eng2, math2, total2, avg2]

student = []
student.append(stu1)
student.append(stu2)

print(student)