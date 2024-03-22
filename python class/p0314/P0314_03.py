# a_list = [1,2,3,4,5,6,7,8,'9',10]

# for i in a_list:
#      try:
#           print(i+1)
#      except:
#           print('데이터 오류가 있습니다.')
#           # pass도 가능 
#      #else:도 있지만 잘 사용하지 않음 # 예외가 발생하지 않았을 때 구현

#예외구문 try, except, else, finally
print('프로그램 실행')
try:
     print(1)
     print(2)
     print(1/0) # 에러가 발생 # 1 2 4 5 6 
     print(3)
except:   # 예외가 발생하면 실행
     print(4) # 에러가 발생하지 않으면 except문은 돌지 않음 # 1 2 3 6
     print(5)
else:     # 예외가 발생하지 않으면 실행
     print(6) # 에러 시 1 2 4 5 #에러 발생하지 않을 때 1 2 3 6
finally: # 예외가 발생하거나, 하지 않거나,  무조건 실행 주로 파일을 닫기 위해 넣는 편
     print(7) #예외 발생 하지 않으면 # 1 2 3 6 7
               # 예외 발생 시 # 1 2  4 5 7
print('프로그램 종료')