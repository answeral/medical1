'''
shift + tap (들여쓰기 삭제)
alt + shift + 위아래 방향키(커서있는 문장 복사)

'''
num = [100,200,300,400]
#for문을 사용해서 하나씩 출력해보세요
for i in range(len(num)):
  print(num[i], end = ' \t')
print()
for i in num:
    print(i, end= '\t')
print()   

numlist = [[1,2],[3,4],[5,6]]
# 변수 in 리스트 이름
for i in numlist:
    for a in i:
     print(a, end = '')
print()   

# in range
for i in range(len(numlist)):
    # print(i) # 0,1,2 
    for j in range(len(numlist[i])):
        print(numlist[i][j])  
    #  print(numlist[i][0], end= '\t')
    
f = [['딸기',100,1000],['수박',100,500],['사과',100,1200],['귤',100,300]]
#요소 한개 한개를 출력하기
for i in range(len(f)): # 0,1,2,3
    for j in range(len(f[i])): # 0,1,2
        print(f[i][j], end ='\t')
print()
for i in f: 
    for a in i: # 00 01 02 03, 10 11 12 13, 20 21 22 23
     print(a, end = '\t')
print()
#과일이름만 출력     
for i in range(len(f)): # 0,1,2,3
    print(f[i][0])    

score = [90,80,70,100,95,85,100]
total = []

# 점수의 총합을 구하세요
for i in range(len(score)): # 0 +1 +2+ 3+ 4+ 5+ 6
    #  print(score[i]) # 90 80 70 100 95 85 100
    sum = 0
    sum += score[i]
    total.append(sum)
print(total)