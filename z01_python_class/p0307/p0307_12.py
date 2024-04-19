list =[
     [0,0,0],[0,0,0],[0,0,0]]

for i in list:
     for f in i:
          print(f,end = '\t')
     print()
     
# 1차원 리스트에 1부터 9까지 숫자를 입력해라
list1 = []
for i in range(0,9):
     list1.append(i+1)
print(list1)# [1, 2, 3, 4, 5, 6, 7, 8, 9]

list2 = [n+1 for n in range(9)]
print(list2) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

list3 = [[n]*3 for n in range(3)]
print(list3)

numList = [num*num for num in range(1,6)]
print(numList)




#2차원 리스트에 1부터 9까지 숫자를 입력해라
a_lists = []
for i in range(3): # 0,1,2가 들어감
     a_list= []
     for j in range(3): # 0,1,2가 들어감
          a_list.append((3*i)+j+1) # [0,1,2]
     a_lists.append(a_list) #[[0,1,2],[0,1,2],[0,1,2]]
     
print(a_lists)


