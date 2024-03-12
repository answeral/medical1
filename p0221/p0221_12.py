print('안녕'*10)
print('안녕하세요','반갑습니다')
print(30,"살입니다") # ,는 한 칸 띄어쓰기
print("30"+"살입니다") # +는 띄어쓰기 없음
print(30) #숫자
print("30") #문자
print("30"+"살입니다")

print(5>20)

print(False)
print(not (5>10))

print("100+100")
print(100+100)

print("숫자는 %d"%300)
print("%d"%5200)
print("%d+%d=%d"%(3,8,3+8))
print("%d*%d=%d"%(4,5,4*5))

print("%d"%123)
print("%7d"%456)
print("%07d"%456)

print("%d"%123.45)
print("%f"%123.45)
print("%7.1f"%123.45)
print("%8.5f"%456.78)
print("%s"%"반갑습니다")
print("%c"%'a')
print("%s"%"abbb")

print("%010.2f"%25.02)

#정수 %d 실수 %f 문자열은 %s 문자는 %c

print("%d-%05d-%05d"%(123,123,123))
print("{}-{}-{}".format(123,45123,123))
print("{}-{}-{}".format(1,13.6,"안녕")) #안녕은 문자로
print("{}+{}={}".format(1,3,"하이"))

print("오늘은 날씨가 흐림, \n내일은 날씨가 맑음")
print("오늘은 날씨가 흐림 \t내일은 날씨가 맑음")


print("""\
안녕하세요.
반갑습니다\
    """)

str1 = "hello"
print(str1)
var1 =2
print(var1)
str2 = "MARK"

print(str1,str2)#띄어쓰기 있음
print(str1+str2)#띄어쓰기 없음
print(str1+' '+str2)

var4 = 100
var3 = var4
var2 = var3
var1 = var2
print("var1 :",var1) #"" 는 문자 ,는 띄어쓰기
print("var2 :" ,var2)

num = "10"
print("입력하신 숫자는 "+num+"입니다")

num = int(input("숫자를 입력하세요 >>"))
print("입력하신 숫자는",num,"입니다")

#float형: 실수
num6 = 3.14
print(num6)
print("%f"%num6)

print("%f"%123.45)


str1 = "name"
print("이름을 영어로 하면 무엇일까요?", str1)


num4 = 10
num5 = 100.3
num6 = 1000
print("%d+%f+%d=%f"(num4,num5,num6,num4+num5+num6))
print("{}+{}+{}={}".format(num4,num5,num6,num4+num5+num6))






