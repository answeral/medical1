import P0315_02
member = P0315_02.idpw()
print(member)

# mem.txt 파일에 
# aaa,1111 저장하기

# 파일열기
file = open('mem.txt','w',encoding='utf8')

# 파일 쓰기
# file.write('aaa,1111')

for m in member:
     file.write('\n'.format(m[0],m[1]))
     
print(file)


#파일 닫기
file.close()

