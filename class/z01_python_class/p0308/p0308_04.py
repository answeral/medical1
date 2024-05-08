import random
#1 .0으로 25개 1차원 리스트 생성
list = [0 for i in range(25)]
for i in range(5):
     list[i] =1 
random.shuffle(list)
print(list)
     
#5*5 2차원 리스트를 0으로 채워서 출력
check_list =[[0]*5 for i in range(5) ]
for i in range(5): # 0 1 2 3 4
     for j in range(5): # 0 1 2 3 4
          check_list[i][j] = list[5*i+j]
print(check_list)          

# 추첨 5*5 2차원 배열
view_list = [['추첨']*5 for i in range(5)]

#checklist 출력

for i in range(5):
     print(i,end= '\t')
     for j in range(5):
          print(check_list[i][j], end ='\t' )
          
          
          
# viewlist 출력
for i in range(5):
     print(i, end = '\t')
     for j in range(5):
          print(view_list[i][j], end = '\t')
print()         

# 좌표입력 후 확인
answer = 0
count = 0
my_xy = [] 
while True:
     x = int(input('x좌표를 입력해주세요 >> '))
     y = int(input('y좌표를 입력해주세요 >>'))
     count += 1
     #내가 입력한 좌표 저장
     my_xy.append([x,y])
     for i in range:
          if check_list[x][y] == 1:
               view_list[x][y] = '당첨!'
               answer += 1
               if answer == 5:
                    print('5개 모두 당첨입니다.')
                    break
          elif count == 10:
               print('10번 시도했습니다. 종료합니다.')
               break     
     else:
          view_list[x][y] = '꽝!'
print('저장된 좌표 : ',my_xy)

     

     