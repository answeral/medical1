numbers = [1,2,3,4,5,6,7,8,9,10]

# index : list에 존재하면 위치값을 리턴
print(numbers.index(5))
print(numbers.index(11)) # error 존재하지 않아서
try:
     if 11 in numbers:
          print('리스트에 있습니다.')
except Exception as e:    
     print('리스트에 없습니다')
     print(e)
     
if 11 in numbers:
     print('리스트에 있습니다.')
else:
     print('리스트에 없습니다')