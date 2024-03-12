#숫자 1개를 입력받아 1개 출력하시오.
# 숫자 1개 입력
# 숫자 1개 출력
num = int(input('숫자를 입력해주세요 >> ')) #str -> int
print(num)

# 숫자 2개 입력
# 숫자 2개 출력
num2 = int(input('숫자를 입력하세요'))
print(num2)
print(num+num2)



# 숫자 5개를 입력받아 출력하세요.

nums = []
for i in range(5):
    nums.append(int(input('숫자를 입력해주세요 (5개) >> ')))
print(nums)

nums = []
sum = 0
for num in nums:
     sum += num
print('합계 : ' ,sum)
     