import random
# 1차원배열 20개의 0으로 리스트 생성,1로 5개널기
#랜덤섞기
# 5*5 2차원 리스트에 넣기
alist=[0 for i in range(25)] #25개의 방 생성
for i in range(5): # 5개의 방을 1로 만들어서
     alist [i]=1 # 25개의 방 중 5개에 집어 넣기
random.shuffle(alist)


checklist = [[0]*5 for i in range(5)] #공간생성
for i in range(5):
     for j in range(5):
          checklist[i][j] = alist[5*i+j] # i =0 1 2 3 4 j = 0 1 2 3 4 
          
# 추첨
viewlist = [['추첨']*5 for i in range(5)]
cnt = 0
count = 0

wrong = 0
while True:
# checklist출력
     print('[5*5 checklist 좌표]')
     print('-'*60)
     print(' ',0,1,2,3,4,sep = ' \t')
     print('-'*60)
     for i in range(5):
          print(i,end='\t')
          for j in range(5):
               print(checklist[i][j],end='\t')
          print()
     print('-'*60)

     # 6.viewlist출력
     print('[5*5 viewlist 좌표]')
     print('-'*60)
     print(0,1,2,3,4,sep = ' \t')
     print('-'*60)
     for i in range(5):
          print(i,end='\t')
          for j in range(5):
               print(viewlist[i][j],end='\t')
          print()
     print('-'*60)
     print('도전 횟수는 5번입니다')
     print(f'현재 도전횟수 :{count+1}번입니다')
     x = int(input('가로 좌표를 입력하세요 >> '))
     y = int(input('세로 좌표를 입력하세요 >> '))
     count += 1
     if checklist[x][y]== 1:
          viewlist[x][y] ='당첨!'
          cnt +=1
          
          if cnt == 5:
               print('5개 모두 맞추셨습니다.')
               break
     else:
          viewlist[x][y] ='[꽝]' 
          wrong += 1    
     
     if count == 5:
          print('5번 도전하셨습니다. 종료합니다')
          print('정답 개수 :',cnt)
          print('오답 개수 :',wrong)
          break


     # for i,j in enumerate(alist): 0부터 4까지
     #      if (i+1)%5 == 0: 
     #           blist.append(j)
     #           blists.append(blist)
     #           blist=[]  
     #      else:
     #           blist.append(j)




     

     # newlist = [['추첨']*5 for i in range(5)]
     # while True:
     #      print('[5*5 좌표]')
     #      print(0,1,2,3,4, sep='')
     #      for i, b in enumerate():
          
     #           pass