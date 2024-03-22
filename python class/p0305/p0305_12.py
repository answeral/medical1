import operator #클래스를 정렬하는 형태

# 딕셔너리 정렬
t_dic = {}
t_list = []
t_dic = {'peach':'복숭아','orange':'오렌지','apple':'사과', 'pear':'배','grape':'포도',
         'mango':'망고','kiwi':'키위'}

t_list = sorted(t_dic.items(),key = operator.itemgetter(0),reverse=True)
print(t_list)
print('-'*50)

print(sorted(t_dic.items(),key = operator.itemgetter(0))) #0번 순서대로 정렬
# (peach, 복숭아),(orange,오렌지).......
#    0      1       0       1
# [('apple', '사과'), ('grape', '포도'), ('kiwi', '키위'), 
# ('mango', '망고'), ('orange', '오렌지'), ('peach', '복숭아'), ('pear', '배')]

print('-'*50)
print(sorted(t_dic.items(),key = operator.itemgetter(0),reverse=True)) # 역순정렬
#[('pear', '배'), ('peach', '복숭아'), ('orange', '오렌지'), ('mango', '망고'), 
# ('kiwi', '키위'), ('grape', '포도'), ('apple', '사과')]

print('-'*50)

print(sorted(t_dic.items(),key = operator.itemgetter(1))) # 1번 순서대로 정렬
#[('mango', '망고'), ('pear', '배'), ('peach', '복숭아'), ('apple', '사과'), 
# ('orange', '오렌지'), ('kiwi', '키위'), ('grape', '포도')]


print(t_dic.keys()) #key값
print(t_dic.values()) # value값
print(t_dic.items()) # 튜플






# 3개의 숫자를 입력받아 순서대로 출력하시오
# 17, 50,12 -> 12,17,50
num = []
for i in range(3):
    n = int(input(f'{i+1}번째 숫자를 입력해주세요 >> ')) # f는 format임. 형태 주의 '%d'%100과 같음
    num.append(n)
num.sort()
print(num)

# 최대값
print('최대값 : ',max(num[0],num[1],num[2])) #print('최대값 : ', max(*num)) 같은 값 도출
#최소값
print('최소값 : ',min(num[0],num[1],num[2])) #print('최소값 : ', min(*num)) 같은 값 도출

# a = [5,7,4,8,1,9,3,2]
# a.sort() # 순차정렬
# print(a) 

# b = [5,7,4,8,1,9,3,2]
# b.sort(reverse = True) #역순정렬
# print(b)


