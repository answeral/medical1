# 숫자를 입력받아서
# 100보다 크거나 같으면 [100보다 크거나 같습니다]
# 아니면 [100보다 작습니다]

n = int(input("숫자를 입력해주세요 >>"))

if n >= 100:
  print("100보다 크거나 같습니다")
  
else  :
    print("100보다 작습니다")
    

if n % 2 == 0:
    print("입력하신 숫자는 짝수입니다.")
    
else :
    print("입력하신 숫자는 홀수입니다.") 
    
# 60점이상이면 합격 아니면 불합격

n1 = int(input("점수를 입력해주세요 >>"))

if n1 >= 60:
  print("합격입니다") 
  
else:
  print("불합격입니다")
  
#5보다 크고 10보다 작은 수 비교
# n이 [5보다 크고 10보다 작은 수 입니다]   

n2 = int(input("숫자를 입력해주세요 >>"))

if 5 < n2 < 10: 
  print("5보다 크고 10보다 작은 수 입니다")
  
#if 5 < n and n <10: <-도 가능
  
else:  #else 뒤에는 조건문을 쓸 수 없다
   print("5이하 10이상 인 수 입니다") 
    
# 3의 배수인지 아닌지

n3 = int(input("숫자를 입력해주세요 >>"))

if n % 3 == 0 : # 3의 배수는 3으로 나눈 나머지가 0이다. 
   print("입력하신 숫자는 3의 배수입니다")
else:
    print("3의 배수가 아닙니다")
     
n4 = int(input("숫자를 입력해주세요 >>"))

if (n % 2==0) and (n % 3 == 0):
    print("2의 배수이며 3의 배수입니다.")