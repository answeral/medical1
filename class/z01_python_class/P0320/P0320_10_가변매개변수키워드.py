def func(n, *val):
     for i in range(n):
          for v in val:
               print(v)
               
func(5,"안녕","안녕하세요","반갑습니다","집에 보내주세요","수고하셨습니다")


def func(n, *val,a=2): # 기본 매개변수, 가변 매개변수 , 키워드 매개변수 순으로 들어와야함
     for i in range(n):
          for v in val:
               print(v)
               
func("안녕","안녕하세요","반갑습니다","집에 보내주세요","수고하셨습니다")
 
print(5,4,3,2,1,sep=',')
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print([i for i in range(10)]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(1,11,2):
#      print(i)
     
# for i in range(10,1-1,-1):
#      print(i)
     
# a_dic ={
#      'a':1,
#      'b':2,
#      'c':3
# }

# for key in a_dic:
#      print(a_dic[key])
     
# for key in a_dic.keys():
#      print(key)
     
# for val in a_dic.values():
#      print(val)
     
# for k , v in a_dic.items():
#      print(k,v)