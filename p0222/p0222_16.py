print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}'.format(
    1, "홍길동", 100,100,100,300,100.0,1))

#학생이름, 국어, 영어 수학 점수를 입력받아서 위와 같이 출력하고
#만약에 평균이 80점이상이면 합격입니다를 출력하세요

name = input("학생의 이름을 입력하세요 >>")
kor1 = int(input("학생의 국어 성적을 입력하세요>>"))
eng1 = int(input("학생의 영어 성적을 입력하세요 >>"))
math1 = int(input("학생의 수학 성적을 입력하세요 >>"))

total = (kor1 + eng1 + math1)
avg = (kor1 + eng1 + math1)/3

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print("{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t". format(
    1,name, kor1, eng1, math1, total, avg, 1))

a = avg
if a >= 80:
    print("합격입니다")
else :
    print("불합격입니다")