# 중첩 if

a = 97 
if a> 90:
  print("90보다 큽니다")
else:
    print('90보다 작습니다')
    
  
if a> 90:
    print("90보다 큽니다")
    if a < 95:
      print(" 95보다 작습니다")
    else:
        print('95보다 큽니다')

else:
    print('90보다 작습니다')
    
# 만약 사과의 상태가 good이며
# 1000원 이하이면 [10개 구매]
# 1000원보다 비싸면 [3개 구매]를 출력
# 사과의 상태가 'good'이 아니면 [사과를 구매하지 않습니다]
apple = 'good'
price = 500 

if apple == 'good':
    print('사과를 구매합니다')
    if price <= 1000:    #지정한 변수 잘보기
     print("10개 구매")   #if보다 print를 들여쓰기
    else:
     print("3개 구매")
else:
    print('사과를 구매하지 않습니다')

# 숫자 하나를 입력받아서
# 100보다 큰 수 면서 짝수면 [짝수], 홀수면 [홀수] 출력
# 100보다 작은 경우 [100보다 작다] 출력
# num = 102 > [짝수], num = 4 [100보다 작다]

num = 82
if num > 100:
   if num% 2 ==0:
      print("짝수")
   else:
       print("홀수")
else:
    print("100보다 작다")        