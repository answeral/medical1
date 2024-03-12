numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7] #1은 두번 2는 한 번...
counter = {}
# counter['1'] = 2
# counter['2'] = 1
# print(counter)

for number in numbers:
    if number not in counter: #count딕셔너리에 키값이 없으면
        counter[number] = 0 #딕셔너리에 추가
    
    counter[number] += 1 # 딕셔너리 1을 증가
    
        
print(counter) #{1: 5, 2: 1, 4: 4, 6: 2, 3: 3, 7: 6}
import operator
# 많이 나온 숫자로 정렬
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))
#[(7, 6), (1, 5), (4, 4), (3, 3), (6, 2), (2, 1)]