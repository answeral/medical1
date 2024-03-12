import operator
fruits =['바나나','배','사과','딸기','딸기','딸기','딸기','사과','바나나','바나나',
          '배','사과','딸기','딸기','딸기','딸기','사과','바나나']

counter = {}
for fruit in fruits:
    if fruit not in counter:
        counter[fruit] = 0
        
    counter[fruit] += 1
     
print(counter) #{'바나나': 4, '배': 2, '사과': 4, '딸기': 8}
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))
#[('딸기', 8), ('바나나', 4), ('사과', 4), ('배', 2)]

fruits.sort()
list.sort() # sort는 정렬함수 오름차순으로 정렬
# 숫자리스트.sort() 오름차순 정렬
# 소문자리스트.sort() 알파벳순 정렬