fruits = ['딸기','사과','자몽','포도','수박','자몽']

# 만약에 자몽을 삭제
# 리스트명. remone('요소명')
fruits.remove('자몽')
print(fruits)
# del(리스트명[번호])

del(fruits[5])
print(fruits)

for i, f in enumerate(fruits): # i =index
 print('{}는{} 번째에 있습니다'.format(f,i)) 