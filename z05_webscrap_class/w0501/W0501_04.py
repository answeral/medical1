import oracledb
while True:
     conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
     cursor = conn.cursor()

     id = input("아이디를 입력하세요(-1.종료).>>")
     if id == '-1':
          break
     
     # id를 가지고 검색을 먼저 한 후 데이터를 입력하도록 해야함.
     # id가 존재하면 id 다시 입력, id가 존재하지 않으면 패스워드 입력받기
     
     sql = f'''select * from member where id='{id}' '''
     cursor.execute(sql)
     data =cursor.fetchall()
     # print("id 개수 : ",len(data)) # 0 = 존재하지 않음 1 = 존재
     if len(data) == 1:
          print("동일한 id가 존재합니다. 새로운 id를 입력해주세요")
          continue
     
     
     print("사용가능 한 id 입니다. 비밀번호를 입력해주세요")
     pw = input("비밀번호를 입력하세요.>>")
     name = input("이름을 입력하세요.>>")
     gender = input("성별을 입력하세요.>>")
     # ---hhh,1111,홍길자, 여자 sysdate
 
     sql =f'''
     insert into member values(member_seq.nextval,'{id}','{pw}','{name}','{gender}',sysdate)
     '''
     cursor = conn.curosr()
     cursor.execute(sql)
     cursor.execute('commit')

     print("입력이 완료되었습니다")
     print()

     cursor.close()
     conn.close()