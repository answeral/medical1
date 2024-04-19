import os

# print('현재 폴더내 파일을 표시 : ',os.listdir()) 

# 폴더가 존재하는지 확인
# if os.path.exists('hello'):
#      os.mkdir('hello')
# else:
#      os.rmdir('hello')
     
# # 1. 파일 생성
f = open ('student.txt','w',encoding='utf-8')
f.write("1,'홍길동',100,99,87,286,95.33,2")
f.write("2,'유관순',98,93,87,278,92.67,3")
f.close() # 파일닫기

# # 2. 파일 생성 - with를 사용하면 f.close()를 사용하지 않아도 됨
# with open ('student.txt','w') as f:
#      f.write("1,'홍길동',100,99,87,286,95.33,2")

# 파일 읽어오기 
t_list = []
out_f = open('student.txt','r',encoding='utf-8')
while True:
     txt = out_f.readline() # 1줄씩 읽어오기
     # print(type(txt))
     if txt == '':
          break
     print(txt,end ='')
     t_list.append(txt)
     
print()
print(t_list)
out_f.close()


#파일삭제
os.remove('student.txt')










