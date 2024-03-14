# 파일열기
f = open('k001.csv','r',encoding='utf8')

# 파일 읽기
cnt = 0
sum = 0
while True:
     content = f.readline()
     if cnt == 0:
          cnt +=1
          continue
     if content =='':break
     
     s_list = content.split(',')
     # print(s_list)
     s_list[4]= int(s_list[4])
     sum += s_list[4]
print(sum)