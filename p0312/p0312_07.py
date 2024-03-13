# 가변매개변수 (ex>*txt) - 잘 사용하지 않음. 있다는 정도 알기.

def str_title(num,*txt):
     print('txt type: ',type(txt)) #튜플형태 - 리스트랑 같은데 추가 수정 삭제 불가능
     print(txt)
     for i in range(num):
          for t in txt:
               print(t,end ='\t')
               
str_title(1,'안녕','잘가','안녕하세요','반갑습니다','비가 와요')



     