import random
#크기가 10인 리스트 생성하는데, 7개는 0으로 3개는 1로 채우시오
#[1,1,1,0,0,0,0,0,0,0]
list = [0]*10
for i in range(3):
     list[i] = 1
print(list)

#크기가 100인 리스트를 생성, 10개는 1로 채우기
#랜덤으로 섞어서 출력
list2 = [0]*100
for i in range(10):
     list[i] = 1
random.shuffle(list2)
print(list2)

#비파괴 - 돌렸을때 변수의 값이 바뀌지 않음
a =10
print(a+10)
print(a)    
print('-'*60)
# 파괴
a= a+10
print(a)
print('-'*60)

alist = [0 for i in range(100)]
for i in range(10):
     alist[i] = 1
random.shuffle(alist) # 파괴 - 리스트는 파괴형식으로 값이 바뀜
print(alist) 
print('-'*60)
#[10*10] 2차원 배열을 생성하시오[[0,0,0,0,0...0],[],,,.10개]
blist = []
blists = []
for i,j in enumerate(alist): #alist는 크기가 100이고 10개가 1인 랜덤으로 출력
      # 100번 돌때마다 계속 처음으로 초기화
     if (i+1)%10 == 0:
           
          blist.append(j)
          blists.append(blist)
          blist=[]
     else:
          blist.append(j)
# print(blists)
#neslist : 보여지는 리스트
#alist : 확인용 리스트 alist 안에는 1이 10개가 있음
newList = [['추첨']*10 for i in range(10)]
cnt =0 
correct = 0
wrong = 0
while True:
     print(blists)
     print('[10*10 좌표]')
     print('-'*60)
     print(0,1,2,3,4,5,6,7,8,9, sep = '    ')
     print('-'*60)
     for i, b in enumerate(newList):
          print(i,end =' ')
          for bb in b:
               print(bb,end =' ')
          print()
     print('-'*60)
     x = int(input('x좌표를 입력하세요 >> '))
     y = int(input('y좌표를 입력하세요 >> '))
     cnt += 1
     #blists - 값을 비교, newlist - 표시
     if blists[x][y] == 1:#당첨
          newList[x][y] = '[당첨]'    
          correct +=1
     else: #꽝
          newList[x][y] = '[꽝]'
          wrong +=1
     if cnt == 10:
          print('종료합니다')
          break
print('당첨 개수 : ',correct)
print('실패 개수 : ',wrong)


# list1 = [i+1 for i in range(10)] #1-10까지
# list3 = [[n]*3 for n in range(3)] #[[0, 0, 0], [1, 1, 1], [2, 2, 2]]
# numList = [num*num for num in range(1,6)] #[1, 4, 9, 16, 25]
