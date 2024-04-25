--어제, 오늘 , 내일
select sysdate-1, sysdate, sysdate+1 from dual;

--오늘, 이 달의 첫 일, 달의 마지막 일
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;

-- 두 날짜 간 일 수, 두 날짜 간 달 수 
select round(sysdate-hire_date,3),trunc(months_between(sysdate,hire_date),2) from employees;

--trunc 일 단위 자리 버림 gruop by 그룹함수
select trunc(kor,-1) kor ,count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;

--hire_date 날짜에서 월만 출력
select hire_date from employees;
select hire_date, to_char(hire_date,'mm') from employees;

select to_char(hire_date,'mm') hire_date, count(to_char(hire_date,'mm')) from employees
group by to_char(hire_date,'mm')
order by hire_date;

--hire_date 2008년도를 출력하고 년도별 인원수를 출력하시오.
select to_char(hire_date,'yyyy'), count(to_char(hire_date,'yyyy'))from employees
group by to_char(hire_date,'yyyy')
order by hire_date;

--형변환 - number, character, date
-- number 사칙연산기능. 쉼표표시안됨, 원화표시안됨.
--char 사칙연산 안됨. 쉼표표시가능, 원화 표시 가능
--date +,- 가능 날짜출력형태는 변경불가-> to_char로 바꿔야함

--시퀀스 형태로 학번을 부여
--ko+2024+0001
create sequence seq_m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

insert into stu_seq(m_no,m_year) values
('ko'||seq_m_no.nextval||'sysdate+365');

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;

--123,456,678 + 100,000 = 123556789
select to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')) plus from dual;

select to_number('123,456,789','999,999,999') -to_number('100,000','999,999') from dual;

select to_char(salary,'$999,999') from employees;

--숫자타입형태를 날짜타입으로 변경
select 20240425 +3 from dual;
select to_char(20240425 +3) from dual;
select to_date(20240425 +3) from dual;

--숫자타입을 날짜 타입으로 변경
select emp_name,hire_date from employees
where hire_date >= to_date(20070101)
order by hire_date desc;

--사원이름 8월 입사한 사람이며 2번째에 a가 들어가있는사람 출력
select emp_name, hire_date from employees
where emp_name like '_a%';
select emp_name, hire_date from employees
where to_char(hire_date,'mm')=08;

select emp_name, hire_date from employees
where emp_name like '_a%' and 
to_char(hire_date,'mm')=08 ;

-- 20070101 이후 입사한 사원이름 2번째에 a가 들어가 있는 사람
select emp_name, hire_date from employees
where emp_name like '_a%' and
hire_date >= to_date(20070101);

select emp_name, hire_date from employees
where emp_name like '_a%' and 
to_char(hire_date,'mm')=08 or to_char(hire_date,'mm')=05 or to_char(hire_date,'mm')=01;

--01,05,08월에 입사한 사람
select hire_date from employees
where to_char(hire_date,'mm') in ('01','05','08');
--이름
select emp_name from employees
where emp_name like '_a%';
--입사일과 이름 합치기
select emp_name, hire_date from employees
where emp_name like '_a%' and to_char(hire_date,'mm') in ('01','05','08')
order by hire_date;

--문자 타입을 날짜 타입으로 변경
select sysdate - to_date('20240401') from dual;
select sysdate,'2024-04-01', sysdate - to_date('2024-04-01') from dual;

select * from m_date;
select * from m_date;


create table eventDate(
eno number,
e_today date,
e_choice_day date,
period number
);
create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

-- 입력시 날짜 타입에 문자(형태-날짜형태)를 입력해도 저장됨.
-- 날자와 문자를 빼기는 불가능, 그래서 문자를 날짜타입으로 변경해야함.
insert into eventdate values(
seq_mno.nextval, sysdate, '2024-04-01',sysdate - to_date('2024-04-01')
);

--문자타입을 숫자타입으로 변경
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

--null 을 0으로 치환 nvl()
select salary,commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;

--manager_id null ceo
select manager_id from employees
order by manager_id desc;

-- 숫자타입을 문다타입으로 변경
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;
-- 그룹함수 : sum, count(), count(*), min,max
-- count : 개수
select count(emp_name) from employees;
--결과값 : 107개
select count(*) from employees;
--null값이 있으면 제외 - 결과값 : 106개
select count(manager_id) from employees;

select emp_name, manager_id from employees;

-- sum : 총 합
select sum(salary) from employees;

--avg :평균
select avg(salary) avg_sal from employees;

--min : 최소값, max : 최대값
select min(salary),max(salary) from employees;

-- 6461달러보다 높은 사람을 출력하시오, 이중쿼리
select emp_name, salary from employees
where salary > (select avg(salary) avg_sal from employees) ;

select min(salary) from employees;
select * from employees;

--최대월급을 받는 사람의 사번 이름 출력
select employee_id,emp_name,salary from employees
where salary = (select max(salary) from employees);

--부서번호가 50번인 사람만 전체 월급
select department_id ,salary from employees;
select sum(salary) from employees
where department_id = 50;

select count(*) from stu_score;
select * from stu_score;
-- kor = 75점 이상인 학생 출력
select kor, name from stu_score
where kor>=80;

select avg(kor) from stu_score;

--국어점수 평균이상, 영어 점수 평균이상인 학생 출력
select count(*) from stu_score
where kor >= (select avg(kor) from stu_score) and
eng >= (select avg(eng) from stu_score);

create table s_info(
sno number,
s_count number
);

insert into s_info values(
stu_seq.nextval,(select count(*) from stu_score
where kor >= (select avg(kor) from stu_score) and
eng >= (select avg(eng) from stu_score))
);

select * from s_info;

--국어점수 최고점인 학생, 영어점수 최고점인 학생 수학 점수 최고점인 학생을 출력해라
select name, kor, eng, math, avg from stu_score
where kor= (select max(kor) from stu_score) 
or eng = (select max(eng) from stu_score)
or math =  (select max(math) from stu_score)
order by avg desc;

--월급이 최대, 최소 , 평균인 사원 출력
select emp_name, salary from employees
where salary = (select max(salary)  from employees)
or salary  = (select min(salary)  from employees)
or salary = (select avg(salary) from employees);

--최대값
select emp_name, salary from employees
where salary = (select max(salary) from employees);

--평균보다 적은 사람 
--56명의 결과값
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc;
--select max(salary) from (테이블)
--56명 중 최대값 : 평균값보다 낮은 사원중에 최대값을 출력하시오
-- 1. 평균값보다 낮은 사람 출력
select emp_name, salary from employees
where salary =6400;

select emp_name, salary from employees
where salary =(select max(salary) from(
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
)
) ;

-- 2. 그 중에 가장 높은 사람 출력
select max(salary) from(
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
);
--power(a,b): a의b제곱

--문자함수
--lpad: 빈공백 채우기 
--: 자리수, 왼쪽빈공백 rpad : 자리수, 오른쪽 빈공백
select emp_name, lpad(emp_name,15,'#') from employees;
select emp_name, rpad(emp_name, 20,'@') from employees; 

--ltrim, rtim 지정한 문자의 왼쪽, 오른쪽 자르기
select emp_name, ltrim(emp_name,'Do') from employees;

select 'ko20240001',ltrim('ko20240001','ko2024') from dual;
--substr(데이터,순서, 개수) ex)substr('abcdefg',3,3) -> cde 
select emp_name, substr(emp_name,3,4) from employees;

select job_id, employee_id from employees;
-- SH와 사원번호를 결합해서 출력하시오
select job_id, substr(job_id,1,2) from employees;
select  substr(job_id,1,2)||employee_id from employees;

--length
select emp_name, length(emp_name) from employees
where length(emp_name)>15;
--날짜 함수, +,- 가능 날짜데이터끼리
--날짜함수 + 1 가능
select sysdate +1 from dual;
--날짜데이터 - 날짜데이터는 가능
select sysdate - hire_date from employees;

--날짜데이터+날짜데이터는 불가능
select sysdate + hire_date from employees;

select round(sysdate,'month') from dual;

select trunc(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

select trunc(sysdate, 'year') from dual;

--개월 수 추가
select sysdate, add_months(sysdate,-2) from dual;
--ceil 올림 floor 버림  mod 나머지 power 제곱
select ceil(-4,2), floor(-4,2), mod(8,3), power(2,10) from dual;
select * from employees;
select emp_name||to_char(hire_date,'yyyy')||'년'||to_char(hire_date,'mm')||'월'||to_char(hire_date,'dd')||'일'||to_char(hire_date,' day') from employees; 

select emp_name||to_char(hire_date,'yyyy'"년" 'mm'"월" 'dd'"일" 'day') from employees;

--사원명, 자리수 9자리빈공백 0으로 표시
--salary*1400앞에 원화표시와 쉼표 넣어서 출력
select to_char(employee_id,'000000000') from employees;
select to_char(salary*1400,'L999,999,999') from employees;

--자신의 생일과 자신의 생일이 속한 달의 마지막날짜
--2010 10 10
select '2010-10-10', last_day('2010-10-10') from dual;
select '2010-10-10',trunc(to_date('2010-10-10'),'month') from dual;

select * from member;

desc member;
--DDL(data definition language)column 추가
--commit, rollback 없음
alter table member add (gender varchar2(6) default 'Female' not null);
select * from member;
update member set gender = 'male';

--컬럼 삭제 : commit, rollback 없음
alter table member drop column phone;
--컬럼 수정 : 이름, 타입, 변경가능
alter table member rename column name to stu_name;
desc member;

--타입변경
alter table member modify(stu_name varchar2(50));
--기존의 데이터가 변경하려는 크기보다 작을 때만 가능
update member set stu_name='홍';
alter table member modify (stu_name varchar2(3));
--varchar2->number은 데이터가 들어가있는 경우는 불가능
--컬럼의 타입을 변경하려면 안에 있는 컬럼 데이터가 빈공백이거나 null일 때 가능
alter table member modify (stu_name number(4));
alter table member modify(stu_name number(100));

desc member;

select * from member;

commit;