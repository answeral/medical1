in_file = None
out_file = None

# 파일 자체 복사

in_file = open('C:/workspace/memo.txt','rb') # 읽는파일 # b-binary
out_file = open('C:/a/m1.txt','wb') # 저장하는 파일

while True:
     bin = in_file.read(1)
     if not bin: break 
     out_file.write(bin)
     
in_file.close()
out_file.close()
print('복사가 완료되었습니다')




