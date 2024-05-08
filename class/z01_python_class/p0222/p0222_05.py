#국어, 영어, 수학 점수를 입력받아서 평균을 출력하세요
# 출력 : 평균은 95점 입니다.
# 변수" kor, eng, math

kor = 95
eng = 95
math = 95

print('({}+{}+{})/3={})'.format(kor,eng,math,(kor+eng+math)/3))

kor = input("국어점수를 입력하세요 >>")
eng = input("영어점수를 입력하세요 >>")
math = input("수학점수를 입력하세요 >>")

kor = int(kor)
eng = int(eng)
math = int(math)

avg = (kor+eng+math)/3

print("평균은 :{}점 입니다.".format(avg))