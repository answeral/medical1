# 1. 변수선언
score = [[80,90,85],[70,80,90],[84,92,80],[72,81,76]] # 각자 요소 더해서 
name = ['홍길동','유관순','이순신','김구']
total = []
# total=[sum0, sum1, sum2, sum3] =sum[i]
# 2. 코딩
# 2-1) 요소 하나하나 출력하기 80 90 85 70 80 90...
for i in range(len(score)): # i = 0 1 2 3
    sum = 0
    for j in range(len(score[i])): # j= 0,1,2,3 번째 합 구하기
     sum = sum + score[i][j]
    total.append(sum)

# 3- 2) 250 미만 불합격 250이상 합격 ex)홍길동님 합격입니다 출력
for i in range(4):
    if total[i] >= 250:
        print("{}님, {}점으로 합격입니다".format(name[i],total[i]))
    elif total[i] < 250:
        print('{}님, {}점으로 불합격입니다'.format(name[i],total[i]))

    
# 2- 2) 작은 요소의 합을 구해서 total에 넣어주기

# 3. 출력
# 3 -1) total = [255,240,256,229]

