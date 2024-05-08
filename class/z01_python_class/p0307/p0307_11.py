import operator

# 딕셔너리는 리스트 형태가 아니면 랜덤,정렬을 할 수가 없음
# numbers = [1,2,3,4,5,5,6,7,4,3,2,12,67,8,9]

# counter = {}

# for n in numbers:
#      if n not in counter:
#           counter[n] = 0
#      counter[n] += 1
     
# print(counter)
fruits = [
    "apple","banana","kiwi","pear","peach",
    "apple","apple","kiwi","kiwi","peach", "peach",
    "apple","pear","apple","apple","pear","pear","pear",
     "peach", "banana","banana"    ]

counter = {}
for f in fruits:
     if f not in counter:
          counter[f] = 0
     counter[f]+=1
print(counter)

print('-'*50)
print(counter.items()) 
# dict_items([('apple', 6), ('banana', 3), ('kiwi', 3), ('pear', 5), ('peach', 4)])
#items의 0번째 값을 가지고 순차정렬
print(sorted(counter.items(),key = operator.itemgetter(0)))
#items의 0번째 값을 가지고 역순정렬
print(sorted(counter.items(),key = operator.itemgetter(0),reverse = True))

