# a_list = [1,2,3,4,5]
# print(a_list)  # [1, 2, 3, 4, 5] # 튜플 (1,2,3,4,5)- 리스트타입인데 수정, 삭제 불가능
# print(*a_list) # 1 2 3 4 5
# print('{} {} {} {} {}'.format(*a_list)) # 1 2 3 4 5

# # 함수
# # 가변매개변수 : *b
# def func(a,b,c): 
#      print(a,b,c)
     
# func(1,2,3)

# def func1(a,*b):
#      print(a)
     
# func1(1,2,3,4)

a_tu = (1,2,3)
print(a_tu)
print(a_tu[0])
print(list(a_tu)) # 리스트 타입으로 형변환

