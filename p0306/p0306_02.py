import operator


fruits =['바나나','배','사과','딸기','딸기','딸기','딸기','사과','바나나','바나나',
          '배','사과','딸기','딸기','딸기','딸기','사과','바나나','사과','사과']

counter = {} # 딕셔너리 생성

for f in fruits:
     if f not in counter:  #딕셔너리에 키가 존재하는지 확인
          counter[f] = 0 #딕셔너리 키가 없을때 키추가
     counter[f] += 1 #키의 value값 1씩 증가

print(counter)
#딕셔너리 정렬 - key순으로 정렬 : 순차정렬
print(sorted(counter.items(),key=operator.itemgetter(0)))
#딕셔너리 정렬 - key순으로 정렬 : 역순정렬
print(sorted(counter.items(),key=operator.itemgetter(0),reverse = True))
# 딕셔너리 정렬 - value순 정렬 : 순차정렬
print(sorted(counter.items(),key=operator.itemgetter(1)))
# 딕셔너리 정렬 - value순 정렬 : 역순정렬
print(sorted(counter.items(),key=operator.itemgetter(1),reverse = True))