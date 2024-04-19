# 파일 입출력
# 파일 만들기  file = open('memo.txt','w',encoding='utf8') w = write
# 쓰기용 : 변수명 = open('파일명','w') #write - 새롭게 정의 !주의할것- 앞에 삭제 될 수 있음
# 쓰기용 : 변수명 = open('파일명','a') #append - 기존 파일에 이어서 씀
# 읽기용 :  변수명 = open('파일명','r') #read
# 텍스트를 제외 나머지 사용 ex)이미지 : 변수명 = open('파일명','b') #binary - 이진모드, 이진파일 처리
# print('[ 메모장 실행]')
# print('-'*60)
# while True:
#      txt = input()
#      if txt == "0":
#           print('메모장을 저장합니다')
#           break
#      print(txt)
#  write
# 파일 열기 
file = open('memo.txt','w',encoding='utf8')
     
# 파일 쓰기
print('[ 학생성적입력]')
print('-'*60)
while True:
     txt = input()
     if txt == "0":
          print('학생성적을 저장합니다')
          break
     print(txt)
     file.write(txt+'\n')

# for i in range(10):
#      file.write(f'안녕하세요.{i+1}\n')

# 파일 닫기

