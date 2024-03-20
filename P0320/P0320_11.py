def jegob(val):
     return val**2

def func(val):
     return val>=3

def int_change(val):
     return int(val)

str_list = ['1','2','3','4','5']

ss_list = list(map(int_change(str_list)))
print(str_list)

ss_list2 = list(map(lambda val:int(val), str_list))
print(ss_list2)
a_list = [1,2,3,4,5]
# 리스트 전체에 값의 변경이 필요할 때 
map_list =list(map(jegob,a_list)) # 리스트로 타입변경이 필요
print(map_list)

# 조건에 맞는 특정값만 추출
f_list = list(filter(func,a_list))
print(f_list)

