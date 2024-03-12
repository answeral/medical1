import random

#random.random() #0-1사이의 랜덤실수를 생성 0.0000~ 0.9999
print(random.random())

# 정수형 랜덤숫자 생성
print(random.randint(0,3)) #0부터 3까지 뒷자리 포함 O

# 1,2까지 랜덤숫자를 생성 뒷자리 포함 X
print(random.randrange(1,3))

# 리스트를 랜덤으로 섞음
list = [1,2,3,4,5,6,7]
random.shuffle(list)
print(list)

# 리스트에서 1개를 랜덤으로 추출
print(random.choice(list))

# 리스트에서 해당되는 개수만큼 랜덤으로 추출 # 중복 불가능
print(random.sample(list,4))

w_list= ['토마토','바나나','사과','배','수박','메론','복숭아']
print(random.sample(w_list,3))