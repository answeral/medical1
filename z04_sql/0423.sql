select * from students;

select * from students
order by name asc;

--drop table students;
-- 컬럼추가
alter table students add rank number(3);

select * from students;

update students set rank = 0;

commit;

select rank() a over(order by total desc) rank
from students;

update students set total=0;

select * from students;

update students set total=(kor+eng+math);

--1 update 구문
update student set rank =(rank);

--2.rank() 구문
(select no,rank() over(order by total desc) ranks from students) b;

--3.update 구문과 rank() 구문을 no컬럼으로 비교,rank 컬럼을 검색
update students a set rank =(
select tanks from (students)b
where a.no = b.no);

--4.students 테이블에서 ranks가 들어가 있는 테이블을 넣어줌.
update students set rank = (
select ranks from (select no,rank() over(order by total desc) ranks from students) b
where a.no = b.no
);


update students a set rank= (select ranks
from(select no,rank() over (order by total desc) ranks
from students) b where a.no = b.no);

select total, rank from students
order by total desc;

--역순정렬
select no, total, rank from students
order by total desc;

--no순차정렬
select no from students
order by no asc;

select no,kor,eng,math,total,rank from students
order by kor desc, eng asc;

select manager_id from employees
order by manager_id asc;

select max(hire_date)-min(hire_date) from employees
order by hire_date desc;

select max(kor)-min(kor) from students;
select max(kor),max(math) from students;

--hire_date 오름차순, 컬럼 사원번호 사원명 job_id, 입사일, 월급 컬럼 출력
select hire_date, employee_id,emp_name,job_id,salary from employees
order by hire_date asc;

--급여를 적게 받는 순으로 출력, 월급이 같으면 사원명으로 순차정렬
select salary, emp_name,employee_id, hire_date, job_id from employees
order by salary asc, emp_name asc;

--숫자함수 
--abs
select -10, abs(-10) from dual;
--floor,round
select 34.789, floor(34.789) as f,round(34.789)as r from dual;
--round(대상, 자리수) ex)round(34.178,2) 소수점 2자리까지 표시, 셋째 자리에서 반올림
select 34.178, round(34.178),round(34.178,2) from dual;

select avg from students;
select round(avg,2) avg from students;
-- 4에서 반올림, 음수는 앞 칸. -2,-1,1,2,3,4 자리 값 
select 34.5678, round(34.5678,-1) from dual;

--trunc 지정한 자리수 이하 버림 //floor는 자리수 지정이 안됨
select trunc(34.5678,2) from dual;

select trunc(34.5678,-1) from dual;

select trunc(34.5678) from dual;

--ceil 올림 // 자리수 존재X
select ceil(34.123) from dual;

--국어점수 일단위 절사해서 출력
select trunc(kor,-1) from students
order by kor;

--국어, 영어 수학 점수 일단위 절사해서 합을 출력
select trunc(kor,-1) 국어, trunc(eng,-1) 영어, trunc(math,-1) 수학
(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) 합계 from students;

--mod 나머지
select round(100/7,2) from dual;
select mod(10,7) from dual;
select 10/7 from dual;

-- 사원번호가 짝수인 것을 출력
select employee_id from employees
where mod(employee_id,2)=0;

--select to_number(employee_id) i from employees
--where mod(employee_id,2)=0 ;

--몫
select floor(10/7) from dual;
--나머지(나머지가 0이면 짝수, 1이면 홀수)
select mod(10,7) from dual;

-- 학생 학번이 3의 배수인 것만 출력
select no from students
where mod(no,3)=0 ;

--시퀀스
create sequence seq_no
increment by 1  --증감 1씩 됨
start with 1    --시작이 1부터
minvalue 1      -- 최소값 1
maxvalue 9999   -- 최대값 9999
nocycle         -- 사이클이 없음
nocache;        -- 캐시 사용하지않음

--nextval 시퀀스 번호 1씩 증가
select seq_no.nextval from dual;
--currval 시퀀스 번호 확인
select seq_no.currval from dual;

--drop table member;

--drop table mem;
--drop table mem2;
--drop table mem3;

create table member(
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;
select seq_mno.nextval from dual;

insert into member values (
seq_mno.nextval,'ddd','1111','강감찬','010-4444-4444'
);

select * from member;

select sysdate from dual;
select to_char(sysdate,'yy')from dual;
--'00000'자리수
select 's'||to_char(seq_mno.nextval,'00000') from dual;

--한국대학교 ko20240001
--시퀀스 seq_kono : 1-99999
create sequence seq_kono
increment by 1
start with 1
minvalue 1 
maxvalue 99999
nocycle
nocache
;

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) stuno from dual;

--게시판
create table board(
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
bdate date,
bhit number(10),
id varchar2(10)
);

--시퀀스 시작1001 증감 10,1,99999
--5번 실행
create sequence seq_deptno
increment by 10
start with 1001
minvalue 1001
maxvalue 99999
nocycle
nocache
;

select seq_deptno.nextval from dual;

create table emp01(
empno number(4) primary key,
ename varchar2(30),
hire_date date
);

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;
alter sequence emp_seq
increment by 1001;


insert into emp01 values(
emp_seq.nextval,'이순신',sysdate
);

select * from emp01;

commit;

select employee_id, emp_name,job_id,hire_date from employees
order by hire_date desc;

--현재까지 입사한 일수를 출력하시오.
select emp_name, hire_date, ceil(floor(sysdate-hire_date))||'일' dd from employees
order by hire_date desc;

select emp_name from employees;

-- 직급, 사번을 합쳐서 출력
select job_id||employee_id from employees;

select substr(job_id, 0,2) from employees;

select emp_name,substr(emp_name,1,3) from employees;

--substr : 문자열 자르기 함수, substr(대상, 시작위치,개수)
--2번째 자리부터 3개를 잘라서 가져와라
select substr('abcde',2,3) from dual;

-- job_id에서 앞 2개 문자와 사번5자리 합쳐서 출력
select substr(job_id,0,2),employee_id,to_char(employee_id,'00000'),
substr(job_id,0,2)||trim(to_char(employee_id,'00000'))from employees;
select substr(job_id,1,2)||'00'||employee_id from employees;

--날짜 함수
select sysdate from dual;
select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;
-- 두 날짜 사이의 개월수 확인
select MONTHS_BETWEEN(SYSDATE,HIRE_DATE),SYSDATE-HIRE_DATE FROM EMPLOYEES;

--개월 수를 추가
select sysdate,add_months(sysdate,2) from dual;

--현재 날짜 기준점으로 다음으로 오는 월요일이 언제?
select next_day(sysdate,'월요일') from dual;

--입력한 기준으로 마지막 날짜를 알려줌
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;