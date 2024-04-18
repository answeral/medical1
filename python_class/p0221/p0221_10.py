
#변수 3개로 만들어서 name, city, fruit
#아래와 같이 출력하기
#저의 이름은 name입니다.
#저는 city시에서 태어났습니다
#wjsms fruit를 좋아합니다

name = "안슬기"
print("안녕하세요, 제 이름은",name, "입니다")
print("안녕하세요, 제 이름은 %s입니다." %name)

print("저의 이름은" + "홍길동" +"입니다")

city = "대전"
print("제가 태어난 도시는",city,"입니다")
print("제가 태어난 도시는 %s입니다"%city)

print("제가 태어난" + "도시는" + "대전입니다")

fruit = "딸기"
print("제가 좋아하는 과일은 "+fruit+"입니다")
print("제가 좋아하는 과일은 %s입니다"%fruit)

#변수 선언 - input으로 입력을 받아서 출력
name = input("이름을 입력하세요 >> ")
city = input("도시를 입력하세요 >>")
fruit = input("과일을 입력하세요 >>")

# a = input("입력하세요")
# print(a)
# b = input("적어보세요")
# print(b)

#input
inputval = input("입력하시오 >>")
print("입력하신 글자는 " + inputval) 