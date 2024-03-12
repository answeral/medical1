import random
#25*25 # 1차원배열
alist = [[0] for i in range(25)]
for i in range(5):
     alist[i]=1
random.shuffle(alist)
print(alist)

# 2차원 배열
blist = []
bLists=[]
for i,j in enumerate(alist):
     if (i+1)%5 == 0:
          blist.append(j)
          bLists.append(blist)
          blist=[]
     else:
          blist.append(j)
          
print(bLists)
cnt =  0        
# 보여지는 리스트
view_list = [['추첨']*5 for i in range(5)]
while True:
     print('[5*5 추첨 리스트 좌표]')
     print('-'*60)
     print(0,1,2,3,4,sep = '   \t')
     for i in range(5):
          print(i,  end=' \t')
          for j in range(5):
               print(view_list[i][j],end='\t')
          print()          
     x = int(input('x의 좌표를 입력하세요 >> '))
     y = int(input('y의 좌표를 입력하세요 >> '))
     if bLists[x][y] ==1:
          view_list[x][y] == '당첨!' 
          cnt += 1 
         
     else:
         view_list[x][y] == '[꽝]'
          