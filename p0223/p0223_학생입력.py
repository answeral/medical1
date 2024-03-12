#학생 성적 입력

#변수 사용
name = '홍길동'
kor = 100
eng = 100
math = 100

#입력을 받아서 총점과 평균을 계산하고, 
name = input('학생 이름을 입력해주세요>>')
kor = int(input('국어 점수를 입력해주세요 >>'))
eng = int(input('영어 점수를 입력해주세요 >>'))
math = int(input('수학 점수를 입력해주세요 >>'))

total = (kor + eng + math)
avg = total/3

# 출력하기
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}'.format( 1 ,name, kor, eng, 
        math, total, avg, 1))

# 홍길동, 100 100 100 300 100.0

stu = [1,'홍길동', 100,100,100,300,100.0,1]
stu1 = [1, name, kor, eng, math, total, avg, 1]

print(stu)
print(stu1)