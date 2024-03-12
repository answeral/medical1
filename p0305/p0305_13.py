import operator
foods = {'떡볶이':'오뎅','짜장면':'단무지','라면':'김치',
         '피자':'피클','맥주':'땅콩','삼겹살':'상추'} #딕셔너리 형태

# 키의 값을 출력하세요
print(foods.keys())

for key in foods:
    print(key,end ='\t')
    
#value 값을 출력하세요
print(foods.values())

for key in foods:
    print(foods[key],end='\t')

# key : value 형태로 모두 출력하시오
print(foods.items())

for key in foods:
    print(f'{key} : {foods[key]}')

print(sorted(foods.items(),key = operator.itemgetter(0)))
print(sorted(foods.items(),key = operator.itemgetter(1)))

