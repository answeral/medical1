##파일을 읽어와서 출력하기

# medical1-1 폴더안 member2.csv
# medical1-1>h0327>aaa 폴더 안 h0327/aaa/member2.csv
# 절대경로 : c:/workspace/medical1-1/h0327/aaa/member2.csv

with open("c:/workspace/medical1-1/h0327/aaa/member2.csv","r",encoding="utf8") as f:
     while True:
          txt = f.readline()
          if txt == "": break
          mem = txt.split(",")
          print(mem[0],mem[1])