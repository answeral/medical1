
#[0,0,0,0....52개 생성] #1차원 리스트
a_list = [0]*52

c_list = [ 0 for i in range(52)] #컴프리헨션

b_list = []
for i in range(52):
     b_list.append(0)
     
# and = [[0],[0],[0]....[52개 생성]] # 2차원 리스트

aa = [[0]*1*52] #얕은복사
# aa[0][0] = 1 #모든 방이 1로 바뀜
# aa[51][0] = 10 #모든 방이 10으로 바뀜

bb = [[0] for i in range(52)] # 깊은 복사 #컴프리헨션
print(bb)
     
cc = []
for i in range(52):
     dd = []
     for i in range(2):
          dd.append(0)
     cc.append(dd)
print(cc)