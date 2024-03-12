print('2단출력')
for i in range(1,10):
    print('2 * {} = {}'.format(i,2*i))
# 원하는 단을 입력받아서 구구단을 입력하세요

for _ in range(5): # i를 사용하면 안됨
 n = int(input('원하는 숫자를 입력해주세요 >>'))
 for i in range(1,10):
    print('{} * {} = {}'.format(n,i,n*i))

