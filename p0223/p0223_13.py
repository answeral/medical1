# 빈 리스트 생성
'''
cont = []
 
c1 = input('1. 나라를 입력해주세요 >> ')
c2 = input('2. 나라를 입력해주세요 >> ')
c3 = input('3. 나라를 입력해주세요 >> ')
c4 = input('4. 나라를 입력해주세요 >> ')

# [미국, 영국, 일본, 중국]
cont = [c1,c2,c3,c4]

print(cont)

contA = []
contA.append(c1)
contA.append(c2)
contA.append(c3)
contA.append(c4)

print(contA)

# 미국 - 영국 - 프랑스 - 이탈리아

contB = ['미국', '영국','프랑스','이탈리아']

print('{} - {} - {} - {}'.format(contB[0],contB[1],contB[2],contB[-1]))

'''
# 내가 입력한 과일들로 리스트를 채워보세요 과일 3개 이상
f= []  #과일리스트

a1 = input(' 1. 과일을 입력해주세요 >>')
a2 = input(' 2. 과일을 입력해주세요 >>')
a3 = input(' 3. 과일을 입력해주세요 >>')

f.append(a1)
f.append(a2)
f.append(a3)

print(f[0],f[1],f[-1])

# 내가 좋아하는 과일은 a,b,c입니다
print("내가 좋아하는 과일은 {},{},{} 입니다".format(f[0],f[1],f[2]))
