# 딕셔너리는 의미 있는 두 값을 연결해 구성
# 딕셔너리 변수 = {키1:값(value)1, 키2:값2, ...} 중괄호로 되어있음 #리스트:[] 대괄호

# a = ['새우깡',90,1200]
# product = {'name':'새우깡','무게':90,'금액':1200}

# students = [1,'홍길동',100,100,100,99] # 각각의 요소가 의미하는 거를 알 수 없음
# s = {'stuNO':1,'name':'홍길동', 'kor':100,'eng':100,'math':100,'sci':99} #요소의 의미를 알 수 있음

# 리스트 대괄호, 출력 idx번호를 사용해서 출력
products =['새우깡',90,1200]
print(products[0])
#딕셔너리 중괄호, 출력 key를 사용해서 출력

students = {'stuNO':1,'name':'홍길동', 'kor':100,'eng':100,'math':100,'sci':99}
print(students(['stuNO']))

students['총합']= 399
print(students)