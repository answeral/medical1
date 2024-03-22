#다른 파일에 있는 함수를 사용할 때
# import math -> 사용방법 math, floor() 이름. 함수명()
# from math import *
# from lotto import *
# import math as m  # 모듈명을 줄여서 사용가능. 별칭부여
# import lotto as lo


import math as m  # 모듈명을 줄여서 사용가능. 별칭부여
import lotto as lo

l = [0]*45
lo.screen(1)
lo.num_generate(1)
# while True:
#      lotto.screen()
lo.num_generate(l)
# # ceil - 올림
print(m.ceil(12.2)) #13

# # floor - 버림
print(m.floor(12.2)) #12

# # round - 반올림
print(round(12.6)) #13 

print(dir(m))

 

 