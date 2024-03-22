a_list = [1,2,3]
# 얕은 복사
b_list = a_list

b_list[0]=100 # 리스트는 주소값 변경
print(a_list) #[100, 2, 3]

# 깊은 복사
a = 50
b = a
b = 20
print(a) #50

