import random
fruit = {'peach':'복숭아','orange':'오렌지','apple':'사과', 'pear':'배','grape':'포도',
         'mango':'망고','kiwi':'키위'}


# print(fruit['peach'])
# print(fruit['kiwi'])

# f_list =['peach','pear','kiwi']
# print(fruit[f_list[0]])


# for f in f_list:
#      print(fruit[f],end = '\t')

f_list = list(fruit.keys()) #['peach', 'orange', 'apple', 'pear', 'grape', 'mango', 'kiwi']
print(f_list)

f_list_ran = random.sample(f_list,4)

print('랜덤추출 :', end = '\t')
for f in f_list_ran:
     print(fruit[f],end = '\t')
