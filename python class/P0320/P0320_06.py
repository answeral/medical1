import datetime

# input으로 입력받은 데이터를
# p_0320.txt 파일을 생성해서 저장하시오
# p_0320은 현재 날짜를 사용하기
now = datetime.datetime.now()
print(now.month)
print(now.day)

print(now.strftime('%m%d'))


f = open('aaa.txt','w',encoding='utf8')
fileName = 'p_'+now.strftime('%m%d')+".txt"
while True:
     str1 = input('데이터를 입력하세요. >> ')
     if str1 == '0':
          print('파일을 저장합니다')
          break
     f.write(str1+'\n')
     
f.close()