import oracledb

#DB connect 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # db와 연결 되어 지시자 생성 

# 홍길동 -> 홍

# 프로그램이 반복되는 형태, -1 입력하면 종료


while True:
     # 검색어 입력 부분
     search = input("찾고자 하는 이름을 입력하세요.>> ")
     if search == '-1':
          break
     
     sql = f'''select * from stu_score where name like '%{search}%' '''
     # sql = '''select * from stu_score where name like '%{}%' '''.format(search)
     cursor.execute(sql)
     data = cursor.fetchall()
   
     for d in data:
          print(d)
     print("-"*30)     
     print("검색된 데이터 개수 :",len(data))

print("프로그램을 종료합니다")
     

conn.close() # 데이터 베이스 연결 해제