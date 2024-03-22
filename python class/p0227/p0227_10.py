num = []
#for문을 사용해서 1-10까지 숫자를 채우세요
for i in range(1,11):
    num.append(i)
print(num) #[1,2,3,4,5,6,7,8,9,10]

num1 =[i for i in range(1,11)]
print(num1)
 
num2 = []
# 1-10까지의 짝수를 num2리스트에 넣으세요
for i in range(1,11):
  if i % 2 ==0:
      num2.append(i)
print(num2) #[2,4,6,8,10]

# 1-10까지의 합을 for문을 사용해서 구할 수 있음.
s1 = 0
num = [1,2,3,4,5,6,7,8,9,10]
#num리스트를 사용해서 1-10까지의 합을 구하기
for i in range (len(num)): # 0,1,2,3,4,5,6,7,8,9
    #num[0]+num[1]+num[2]+...+num[9]
   s1 += num[i]
print(s1)  

s2 = 0
for i in num2:
    s2 += i
print(s2)

