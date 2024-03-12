a = 10
b = a #변수 복사
b = 100
print(a) # 값 10
print(b) # 값 100
print('-'*40)


#값이 하나 일때는 복사가 가능하지만 리스트 복사는 그냥 해서는 안됨 # 깊은 복사해야함
a_list = [1,2,3]
b_list = a_list #리스트 복사
b_list[0] = 200

print(a_list[0]) # 값 200
print(b_list[0]) # 값 200