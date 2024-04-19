# numbers에 있는 수자들이 몇 번 나왔는지
# 딕셔너리로 출력하세요
import operator
numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}

for number in numbers:
     if number not in counter:
          counter[number]= 0
     counter[number] += 1
     
print(counter)
print(sorted(counter.items(),key=operator.itemgetter(0)))
print('-'*50)
array = ["F", "D", "A", "C", "A", "C", "F", "B", "C", "E", "C", "C", "F", "A", "B", "E", "F", "E"]
counter1 = {}
for a in array:
     if a not in counter1:
          counter1[a] = 0
     counter1[a] += 1
     
print(counter1)
print(sorted(counter1.items(),key=operator.itemgetter(0)))


          
