import oracledb



# 평균 점수를 입력받아 입력한 평균 점수 이상의 학생을 출력하시오
# 반복해서진행하고 -1 입력시 종료


while True:
     conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
     cursor = conn.cursor()

     search = input("평균 점수를 입력해주세요.(-1:종료) >>")
     
     if search == '-1':
          break
     
     print("1. 평균점수이상")
     print("2. 평균점수이하")
     num_str = input("평균 점수 이상 또는 이하를 선택하세요")
     if num_str == '1':
          sql =f'''select * from stu_score where  avg >= {search}
          order by no'''
     elif num_str == '2':
          sql =f'''select * from stu_score where  avg < {search}  order by no'''
     else:
          print("입력하신 번호를 확인해주세요.") 
     cursor.execute(sql)
     data = cursor.fetchall()

     for d in data:
          print(d)
          print("-"*60)
     
     conn.close()
          
print("프로그램이 종료되었습니다")
conn.close()
