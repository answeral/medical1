#변수 사용
#변수 bool, int, float, str형이 있다
#변수는 대소문자를 구분한다.(대문자는 주로 클래스에서 사용)
#둘이 다른 변수
myvar = 10
MyVar = 20 
# 변수는 언더바를 포함 할 수 있고 숫자로 시작하면 안된다.
number1 =10
my_number = 200
# 1number와 같이 숫자로 시작해서는 안된다

# 변수는 예약어를 사용할 수 없다
# if=200 True = 200

#변수는 마지막으로 입력된 값을 저장한다
a = 10
a = 30
print(a) #30으로 출력됨

a = 1
b = 2
c = 3
print(1+2+3)
print(a+b+c)

var2 = 200
var1 = var2 + 100
print(var1,var2)

a = 1
b = 2
a,b = 1,2 #이렇게 변수로 해도 됨

# 입력 받기
#input() : 입력을 받는 함수

name = input("당신의 이름을 입력하세요 : ")
print("당신의 이름은 "+name+"입니다")

#input()은 문자열로 입력이 된다

age = int(input("나이를 입력하세요 >>"))
print("당신의 내년에 {}살입니다".format(age+1))

#숫자로 바꿔주기
#1.age = int(input("나이를 입력하세요 >>"))
#2. age = int(age) 
age = input("나이를 입력하세요 >>") 

#숫자하나를 입력받아서 구구단을 출력
#2를 입력받으면 2*1=2  2*2=4 2*3=6

