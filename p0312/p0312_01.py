# 파이썬 언어는 스크립트 언어, 
# 인터프리터 언어 -  한 줄씩 기계어로 변환-> 속도빠르지않음 ,파이썬, 자바스크립트, 실행파일이 생성 X(보안취약)

# 컴파일러 언어- 전체 코드를 한 번에 기계어(ex>0,1)로 변환 후 실행파일을 만듦 -> 속도빠름, 
# C, C++, 자바, 실행 파일 생성(보안좋음)

# 두 수를 입력받아, 두 수 사이의 합계를 구하시오
# 1. 두 수 입력
# 2. 함수 호출
# 3. 1-10까지
# 4. 합계를 리턴받아서
# 5. 합계 출력

# 1-10까지의 더하기,빼기, 곱하기의 결과값을 출력해라


def cal(s_list):
     #sum
     if s_list[0]>s_list[1]:
          s_list[0],s_list[1] = s_list[1],s_list[0]
     
     
     for i in range(s_list[0],s_list[1]+1): 
          s_list[2] += i
          s_list[3] -= i
          s_list[4] *= i
     


sum = 0
minus = 0
multi = 1
     
n1 = int(input('첫번째 숫자를 입력하세요 >> '))
n2 = int(input('두번째 숫자를 입력하세요 >> '))
s_list = [n1,n2,0,0,1]
cal(s_list)


print('더하기 결과값 :',s_list[2])
print('빼기 결과값 : ',s_list[3])
print('곱하기 결과값 : ',s_list[4])
                    