# 돈을 입력받아
# 5만원권
#만원권
#오천원권
#천원권으로 
#교환해서 출력

money = int(input("교환할 돈을 입력하세요 >>"))

#money = 1586000                             #a//b 몫 a%b 나머지
p50 = money//50000 
p10 = (money%50000)//10000
p5 = ((money%50000)%10000)//5000
p1 = (((money%50000)%10000)%5000)//1000

print('입력한 금액 : {:,}'.format(money))
print('50000원 : {:,}장'. format(p50))
print('10000원 : {:,}장'.format(p10))
print('5000원 : {:,}장'.format(p5))
print('1000원 : {:,}장'.format(p1))


 