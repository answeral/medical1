import oracledb

#DB connect 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # db와 연결 되어 지시자 생성 

#sql 실행
# employees 테이블에서 사번, 이름, 월급, 실제 월급(월급+(커미션*월급)), 월급*1410 원화로
# 천단위 표시해서 출력 
# sql ='''select employee_id, emp_name, salary, (salary+(salary*nvl(commission_pct,0))),
# to_char(salary*1410,'999,999,999') from employees'''

# print("[ 데이터 출력 ]")
# print("-"*40)
# print("사원번호\t사원명\t월급\t실제월급\t원화환산")
# print("-"*40)
# for d in data:
#      print(d[0],end="\t")
#      print(d[1],end="\t")
#      print(d[2],end="\t")
#      print(d[3],end="\t")
#      print("￦"+d[4].strip())
#      print("-"*40)

# 부서별 평균 월급, 최대 월급, 최소월급 출력
sql = '''
select department_id,round(avg(salary),2), max(salary), min(salary) from employees
where department_id is not null
group by department_id
order by department_id
'''
cursor.execute(sql)
data = cursor.fetchall()
for d in data:
     print("부서 ID : ",d[0],sep="\t")
     print("평균 월급 : ",d[1],sep="\t")
     print("최대 월급 : ",d[2],sep="\t")
     print("최소 월급 : ",d[3],sep="\t")
     print("-"*60)

conn.close() # 데이터 베이스 연결 해제