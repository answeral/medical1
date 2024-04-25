select * from employees;

select employee_id, emp_name from employees;

select salary from employees;

--타입 : number일 때 +,-,*,/가능
select salary, salary*1400 k_sal, salary*1400*12 as y_sal from employees;

select * from stu_score;

select no,name, kor, eng, math, total, avg, rank from stu_score;

--파이썬 

select department_id from employees;

select nvl(department_id,0) from employees;

--별칭 as,  "":키워드를 있는 그래도 사용
select salary, salary +(salary* nvl(commission_pct,0)) as "Real_sal" from employees;

select salary as 연봉 from employees;

select * from departments;

--부서이름, 부서번호를 출력
select department_id, department_name from departments;

--여러개의 데이터를 1개로 합쳐서 넘겨야 할 경우 concat
--홍길동, 유관순, 이순신, 김구, 강감찬, 김구 ->분리 :split(",") 

select * from stu_score;

select kor||','||eng||','||math stu from stu_score;

select kor+ eng+ math as total,(kor+eng+math)/3 from stu_score;

--중복제거 : distinct
--where : 조건절 not 제거하고 선택하려면 is not null
select distinct department_id from employees where department_id is not null;

--manager_id
select manager_id from employees;
select distinct manager_id from employees where manager_id is not null;

select * from employees;
select employee_id,salary from employees
where employee_id =200 or employee_id =201 or employee_id =202;

--201<=employee_id < 205는 불가능 and 사용할 것
select * from employees
where employee_id >=200 and employee_id <=206;

select * from employees
where employee_id <=150 or employee_id >= 200;

select employee_id,department_id from employees
where department_id =10 or department_id =30 or department_id = 50;

--월급 6000 이상 9000이하
--정렬: order by 컬럼 asc:순차정렬, desc:역순정렬
select employee_id, salary from employees
where salary>=6000 and salary <=9000
order by salary asc;

--월급 6000,7000,8000인 사원을 출력하시오
select employee_id, salary from employees
where salary =6000 or salary=7000 or salary = 8000;

--부서번호가 50이면서 월급이 8000이상인 사원 출력
select department_id,salary from employees
where department_id =50 and salary>=8000;

--stu_score에서 홍길동 출력
select * from stu_score
where name = '홍길동';

--순차정렬
select hire_date from employees
order by hire_date asc;

--역순정렬
select hire_date from employees
order by hire_date desc;

select emp_name,hire_date from employees
where hire_date <='02/01/01'
order by hire_date asc;

select hire_date,hire_date+100 from employees;

--반올림:round
select round(sysdate-hire_date) from employees;
--문자 합치기: + 연산자 불가능, concat : || 사용
select emp_name || email from employees;

--입사일이 05년 이상 06년 이하이면서 월급이 6000달러 이상인 사원을 역순 출력
select emp_name,hire_date,salary from employees
where hire_date>='05/01/01' and hire_date <= '06/12/31' and salary>=6000
order by hire_date desc;

--!=, <>, not, ^=
select department_id from employees
where department_id != 10 and not department_id =50
order by department_id asc;

--5000이상 9000이하
select emp_name,salary from employees
where salary >=5000 and salary <=9000
order by salary asc;

--평균 99이상인 사람 검색
select name,avg from stu_score
where avg>=99
order by avg desc;

select * from students;

update students set name='관순스'
where no=10;

select * from students;
commit;

--students에서 국어가 80이상, 평균 85점이상인 학생 출력
select * from students
where kor>=70 and avg >=75;

--국어점수 80점, 국어 70, 국어 90점 인 학생ㅅ 출력
select name, kor from students
where kor=70 or kor =80 or kor =90;

update students set kor =100
where no = 1;
rollback;
select * from students
where no =1;
--수정
update students set kor=100,total = 100+ eng+ math,avg = (100+eng+math)/3
where no=1;

--국어점수가 70~90 이상 학생을 출력하시오
select name, kor from students
where kor > 70 and kor <= 90;
--100명
select * from students;
--between a and b : a 와 b 사이, a보다 크거나 같고, b보다 작거나 같은 것 검색
--27명
select kor from students
where kor between 80 and 90;

--70보다 작고 90보다 큰것
--73명 not between a and b: a보다 작거나, b보다 큰 것 검색
select kor from students
where kor not between 70 and 90;

--날짜도 between a and b
select hire_date from employees
order by hire_date asc;

--날자가 99년보다 크거나 같고, 01년보다 작거나 같은 것
select hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date asc; 

--in 연산자 : 동일한 필드가 여러개의 값 중에 하나를 검색할 경우
--not in : 제외하고
select name, kor from students
where kor not in(80,70,90);

--이름검색
select * from students
where name = '홍길동';

--like 검색 : 특정단어가 포함되어 있는 것을 검색
--%홍: 홍으로 끝나는 단어, 홍%:홍으로 시작하는 것, %길%:포함되어 있는 단어
select * from students
where name like '%스';

-- _ : 한 칸 공간을 사용, 길 앞에 1개의 담어가 있으면서 길이 포함되어 있는 단어 검색
select * from students
where name like '_길%';

--세 번째 글자에 t가 들어가 있는 이름 찾기
select * from students
where name like'__t%';

--이름이 4자리인 3번째에 r이 들어간 이름 검색
select * from students
where name like '__r_';
--이름길이가 4자리이고, 3번째에 r이 들어간 이름 검색
select * from students
where name like'__r%'
and length (name) = 4;

--이름 길이가 4자리
select name from students
where length(name) = 4;

--이름이 대문자 A로 시작되는 것 검색
select no,name from students
where name like 'A%';

--이름에 a가 들어가 있는 학생 검색
select no,name from students
where name like '%a';

--대소문자 구분없이 a가 들어가 있는 학생 검색
--소문자 치환 lower().대문자 치환 upper(), 첫글자 대문자 initcap()
select no,name from students
where lower(name) like '%a%';
--a가 포함되어 있지 않은 이름 검색
select no,name from students
where lower(name) not like '%a%';

select employee_id, manager_id from employees
where manager_id =100;

select employee_id, emp_name, manager_id from employees
where manager_id = null;

select employee_id, emp_name, manager_id from employees
where manager_id is null;

select employee_id, emp_name, manager_id from employees
where manager_id is not null;

select * from stu_score;

--한글도 순차정렬 가능
select * from stu_score
order by name asc;

--1차 국어점수로 역순정렬 한 다음, 같은 점수인 경우, 영문점수로 순차정렬 진행
select * from students
order by kor desc, eng asc;

select * from students
order by total desc;

--컬럼 추가
alter table students add rank number(3);

--컬럼 타입
desc students;

select * from students;

update students set rank = 0;

commit;

-- 등수
select no,rank() over(order by total desc) as rank from students
;
update students s1 set rank = (select ranks
from (select no no2, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no2 )
;
select * from students;

--수정
update students set rank =13
where no=1;

select * from students;

update students s1 set rank = 13
where no =1;

--select * from(테이블);
select * from (select * from students
where avg >= 70);