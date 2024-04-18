# medical_1.csv 파일을 읽어와서 출력하세요

#1. 파일열기
f = open('medical_1.csv','r',encoding='utf8')
# 2. 파일 읽기
cnt = 0
sum = 0
v_list = []
while True:
     content = f.readline()    
     if cnt == 0:
          cnt += 1
          continue
     if content == '':break
     
     v_list = content.split(',')
     v_list[1] = int(v_list[1])
     sum += v_list[1]
     print(v_list)
print('기초생활수급대상자 현재 수 : ',sum)
     
     
        
#. 3. 파일 닫기
f.close()