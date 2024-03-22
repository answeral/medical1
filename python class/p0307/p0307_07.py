import random
fruit = {'peach':'복숭아','orange':'오렌지','apple':'사과', 'pear':'배','grape':'포도',
         'mango':'망고','kiwi':'키위'}

print('개수: ', len(fruit))
#랜덤으로 4개를 출력
#랜덤은 리스트
#key를 리스트 타입으로 변경해야함
print(fruit.keys())
print(random.sample(list(fruit.keys()),4))

#4개의 랜덤 key를 출력하세요
print(random.sample(list))

f_list = random.sample(list(fruit.keys()),4)
f_list2 = ['kiwi','grape','peach','pear']
print(fruit[f_list2[0]])

#value값을 전체 출력

for key in fruit:
     print(fruit[key], end = '\t')




