# str.txt 파일의 내용을 모두 출력하시오
# 1. 파일열기

f= open('str.txt','r',encoding='utf8')
# 2. 파일 읽기
while True:
     content = f.readline()
     if content.strip() =='':break # 읽을 게 없다면 = 빈공간이라면 break # 빈공백 enter키 삭제
     print(content, end='')
     
# 3. 파일 닫기
f.close()


# 4. str 파일 내용을 읽어오기
f = open('str.txt','r',encoding='utf8')
ff = open('str1.txt','a',encoding='utf8')

while True:
     content = f.readline()# 파일내용 읽어오기
     if content.strip()=='':break
     ff.write(content) # 파일내용 추가하기
     
f.close
ff.close

fff= open('str1.txt','r',encoding='utf8')
while True:
     content = fff.readline()
     if content.strip() == '':break
     print(content, end='')
     
fff.close()






# # str.txt 파일 내용을 읽어와서
# file = open('str.txt','r',encoding='utf8')
# while True:
#      txt = file.readline()
#      if txt == "": break
#      print(txt,end="")


# # str1.txt에 내용 추가하기
# file = open('str1.txt','a',encoding='utf8')
# while True:
#      txt_input = input("")
#      if txt_input == '-1': break
#      file.write(txt_input+'\n')

# # str2.txt 생성하고 내용추가
# # 생성
# file = open('str2.txt','w',encoding='utf8')

