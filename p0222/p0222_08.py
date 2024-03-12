# 원의 넓이와 원의 둘레를 출력하시오 pi = 3.141592 r =10
# 원의 넓이 : pi * ( r**2)
# 원의 둘레 2 pi r

# 변수 원의 반지름 r
# pi = 3.141592

r = input("반지름을 입력하세요 >>")
r = int(r)

pi = 3.14159

res1 = (pi * (r**2))
res2 = (2 * pi * r)

print("원의 넓이:{:.2f}\n, 둘레:{:.2f}".format(res1,res2))
# print("원의넓이:{}\n 둘레:{}".format(res1, res2)) 

