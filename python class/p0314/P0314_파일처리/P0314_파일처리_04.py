
# 파일 읽어오기

# 1. 파일 읽기 형태
# read() : 모든 문자열을 가져옴.
# readline() : 1줄씩 가져옴
# readlines() : 1줄씩 리스트 타입에 입력해서 모두 가져옴.
# 3. 파일 닫기

# 파일 확인
import os
if not os.path.exist('str.txt'):
     with open('str.txt','r',encoding='utf8') as f: # 변수명을 뒤에 씀.
      txt_list = f.readlines() #['안녕하세요. 반갑습니다.\n', '저는 홍길동입니다.\n', '파이썬 수업을 열심히 듣고 있습니다.\n']
     
     
     for txt in txt_list:
          print(txt, end ='')
     print()
else:
     print('존재합니다')     
# readline
# f = open("str.txt",'r',encoding='utf8')
# while True:
#      txt = f.readline()
#      if txt == '':break
     
#      print(txt,end = '')
     
# readlines
# f = open('str.txt','r',encoding='utf8')
# txt_list = f.readlines()

# print(txt_list)

# print(txt_list[0])
# f.close() # 파일 종료를 반드시 해야함

# with -  with를 쓰면 f.close 생략 가능

     