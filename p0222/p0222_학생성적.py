print('-'*35)
print('\t[학생성적프로그램]')
print('-'*35)
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적 삭제')
print('4.학생성적전체출력')
print('5.학생성적전체출력')
print('6.등수처리')
print('0.프로그램 종료')
print('-'*35)

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}'.format(
    1, "홍길동", 100,100,100,300,100.0,1))

# 홍길동 100 100 100
# 유관순 90 100 90
# 두 정보를 입력을 받아서 출력해보세요.

#변수 설정
# 성적을 입력받기 #이름을 입력받기 # 국어, 영어, 수학, 합계, 평균, 등수
#이름


#국어, 영어, 수학 점수
name1 = input("첫번째 학생의 이름을 입력해주세요 >>")
kor_grade1 = int(input("첫번째 학생의 국어 성적을 입력해주세요 >>"))
eng_grade1 = int(input("첫번째 학생의 영어 성적을 입력해주세요 >>"))
math_grade1 = int(input("첫번째 학생의 수학 성적을 입력해주세요 >>"))

name2 = input("두번째 학생의 이름을 입력해주세요 >>")
kor_grade2 = int(input("두번째 학생의 국어 성적을 입력해주세요 >>"))
eng_grade2 = int(input("두번째 학생의 영어 성적을 입력해주세요 >>"))
math_grade2 = int(input("두번째 학생의 수학 성적을 입력해주세요 >>"))

#합계, 평균, 등수  #print("%.2f"%(123.45678))
sum_1 = (kor_grade1 + eng_grade1 + math_grade1)
sum_2 = (kor_grade2 + eng_grade2 + math_grade2)

avg_1 = (kor_grade1 + eng_grade1 + math_grade1)/3
avg_2 = (kor_grade2 + eng_grade2 + math_grade2)/3
#avg1 = sum1/3
#avg2 = sum2/3

print('번호 \t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}'.format(
    1, name1, kor_grade1, eng_grade1, math_grade1, sum_1, avg_1,1))
print('{}\t {}\t {}\t {}\t {}\t {}\t {:.2f}\t{}'.format(
    2, name2, kor_grade2, eng_grade2, math_grade2,sum_2, avg_2,2))
