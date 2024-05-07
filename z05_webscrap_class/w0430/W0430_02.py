import oracledb

#sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # db와 연결 되어 지시자 생성 

# board 테이블 id 포함 모든 컬럼, memebr테이블의 name 컬럼을 가져와 출력
# board테이블 id, member테이블 name
# sql = "select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile\
#      from board a, member b\
#      where a.id = b.id "

# stu_score avg 90점이상 A 80이상 B 70 C 60 D 60미만 F
# 학번, 이름, 합계, 평균, 학점 출력
# sql = '''select no, name, total, avg,
#      case 
#      when avg >= 90 then  'A'
#      when avg >= 80 then 'B'
#      when avg >= 70 then 'C'
#      when avg >= 60 then 'D'
#      else 'F'
#      end as grade
#      from stu_score  '''

# 평균을 가지고 파이썬에서 프로그램하여 학점을 출력하시오
# 학번0, 이름1, 합계5, 평균6, 학점




# sql = "select * from stu_score"
# cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값: list)
# data = cursor.fetchall() # fetchall() : 모든 데이터를 가져옴. fetchone(): 1개의 데이터 가져옴.
# print("[ 모든 데이터 출력 ]")

# # print(data)
# for d in data:
#      # print("평균 : ",d[6])
#      if d[6] >= 90:
#           print("학번 : ",d[0],"이름 : ",d[1],"합계 : ",d[5]," 평균:" ,d[6],"학점 : ","A")    
#      elif d[6] >=80:
#           print("학번 : ",d[0],"이름 : ",d[1],"합계 : ",d[5]," 평균:" ,d[6],"학점 : ","B")
#      elif d[6] >=70:
#           print("학번 : ",d[0],"이름 : ",d[1],"합계 : ",d[5]," 평균:" ,d[6],"학점 : ","C")
#      elif d[6] >= 60:
#           print("학번 : ",d[0],"이름 : ",d[1],"합계 : ",d[5]," 평균:" ,d[6],"학점 : ","D")
#      else:
#           print("학번 : ",d[0],"이름 : ",d[1],"합계 : ",d[5]," 평균:" ,d[6],"학점 : ","F")

#      print("-"*60)
# print("타입 :", type(data))

# salary 평균을 출력하시오
sql = "select round(avg(salary),2) from employees"
cursor.execute(sql)
data = cursor.fetchone()
print(data[0]) #(6500,) 튜플 형태라 , 붙어있음

for d in data:
     print(d)

conn.close() # 데이터 베이스 연결 해제