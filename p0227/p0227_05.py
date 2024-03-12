
# 0-20 사이의 홀수를 출력
# 0-20 사이의 5의 배수로 이루어진 리스트를 만들어보세요
num =[]
for i in range(5,21,5):
    # print(i)
    num.append(i) # 여러번 반복해서 나온 결과값을 num에 입력해야하기에 for문 안에 적기
print(num)
print()
     # 3의 배수
n =[]
for i in range(21):
    if i % 3 ==0:
        # print(i) # i의 값이 0,3,6,9...
        n.append(i)
print(n)        
print()

lan = ['c','python','java','jquery','css']
# 하나하나 출력해보기 for문 사용
# 카운터변수는 i
# 1.c 2.python 3. java 4.-- 줄바꿔서 출력해보기
# for i in lan:
#     print(lan[0])
for i in range(len(lan)):  #for문 자체가 반복문이라는 거 기억하기
    print(lan[i])

    
for i in range(len(lan)): # 01234
    # print(i)
    print('{}.{}'.format(i+1,lan[i]))  #format(i, lan[i-1])
    
# for i in range(len(lan)):
#     print('2.{}'.format(lan[1])) 
             
    
# for i in range(5): 
#     print(lan[i]) # lan[0] lan[1]

num = [1,-1,2,3,-4,5,6,-8,9,-10]
# 양수면 양수, 음수면 음수
# 1: 양수 -1: 음수 2: 양수
for i in num:
    if i > 0 :
        print('{} : {}'.format (i,'양수')) #print(n, end= '양수')
    elif i <0 :
        print('{} : {}'.format (i,'음수'))
        
for i in range(len(num)): #012345678
    if num[i] >0 :
        print('{} : {}'.format(num[i],'양수'))
    elif num[i] <0:
        print('{} : {}'.format(num[i],'음수'))
        

         


        