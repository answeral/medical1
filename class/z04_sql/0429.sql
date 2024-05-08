--drop table board;
--DROP TABLE board CASCADE CONSTRAINTS;
-- 무결성 제약조건 : 부적합한 자료가 입력되지 않도록 하기 위한 규칙
--not null, unique, primary jey, foreign key, check
create table member(
memno number(4)not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('남자','여자')),
mdate date default sysdate
);

--데이터 입력, 출력, 수정, 삭제 부분
insert into member (memno, id,pw, name, gender, mdate) values(
member_seq.nextval,'aaa','1111','홍길동','남자',sysdate
);

insert into member(memno, id, pw, name, gender) values (
member_seq.nextval, 'bbb','1111','유관순','여자');

insert into member values(
member_seq.nextval, 'ccc','1111','이순신','남자',sysdate);

select * from member;

--테이블 생성
create table board(
bmo number(4) primary key,
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) --외래키(foreign key)의 별칭 : fk_id
references member(id) --member 체이블의primaty key로 id가 선언이 되어있음,
--(foreigm key로 선언하려면 primary key로 선언이 되어있어야함)
);  

--alter table board rename column bmo to bno;

--primary key를 삭제하려면 foreign key로 등록되어 있는 데이터를 우선 삭제를 모두 해야함.
-- 1.primary key 삭제 되면 모두 삭제하는 방법 - on delete cascaed, 2. 모두 존재하는 방법 - on update cascade

insert into board(bmo,id,btitle, bcontent, bdate, bgroup, bstep,bindent,bhit,bfile) values(
BOARD_SEQ.nextval,'aaa','제목입니다.','내용입니다.',sysdate, board_seq.currval,0,0,1,''
);

insert into board values(
BOARD_SEQ.nextval,'bbb','제목입니다2.','내용입니다2.',sysdate, board_seq.currval,0,0,1,''
);

insert into board(bmo,id,btitle, bcontent, bgroup) values(
BOARD_SEQ.nextval,'aaa','제목입니다.3','내용입니다.3', board_seq.currval
);
--삭제
delete board where bmo =3;

select * from board;

commit;

delete member where id='aaa';

--decode 조건문
select emp_name, department_id,
decode (department_id,
10,'총무기획부',
20,'마켓팅',
30,'구매/생산부',
40,'인사부')
from employees
order by department_id asc;

select * from stu_score
order by avg desc;
--90점 A,80점 B, 70점 C

select * from stu_score;

select name, avg,
decode (avg,
90,'A',
80,'B',
70,'C')
from stu_score
order by avg desc;

select department_id, department_name from departments;

select job_id, salary from employees;
 -- sH_clerk salary*15%, ad_asst*10% MK_rop *5% 월급 인상
 select job_id, salary,
 decode (job_id,
 'SH_CLERK',nvl(salary,0)+ (nvl(salary,0)*0.15),
 'AD_ASST', nvl(salary,0)+ (nvl(salary,0)*0.1),
 'MK_ROP', nvl(salary,0)+(nvl(salary,0)*0.05))
 as salary_up from employees
;

 
-- job_id 중에 clerk이 들어가 있는 job_id를 검색하기
-- _자리수 , % 모든 것
select job_id from employees
where job_id like '%CLERK%';

select name, avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
else 'F'
end as grade
from stu_score;

select department_id, department_name from departments;

--case 구문, department_id 이름을 출력
select department_id from employees
order by department_id asc;

select department_id,
case 
when department_id = 10 then '총무기획부'
when department_id = 20 then '마케팅'
when department_id = 30 then  '구매/생산부'
else '나머지'
end as department
from employees;

--월급 출력 job_id
--CLERK 포함 :salary*15%, ad_asst *10% rep*5%, man*25%
select job_id, salary,
case 
when job_id like '%CLERK%' then nvl(salary,0)+ (nvl(salary,0)*0.15)
when job_id like 'AD_ASST' then nvl(salary,0)+ (nvl(salary,0)*0.1)
when job_id like'%REP' then nvl(salary,0)+ (nvl(salary,0)*0.05)
when job_id like '%MAN%' then nvl(salary,0) +(nvl(salary,0)*0.25)
end as salary_up
from employees
order by salary_up asc
;
-- 월급 평균 이하인 사람은 0.15 평균이상인 사랆은 0.05 인상해서 출력
select round(avg(salary)) from employees;

--employees에서 검색, up,down이 나타나지 않음
select emp_name, salary,w_sal,
case 
when salary <= (select round(avg(salary)) from employees) then nvl(salary,0)+(nvl(salary,0)*0.15)
when salary > (select round(avg(salary)) from employees) then nvl(salary,0)+(nvl(salary,0)* 0.05)
end as sal
from (
employees
)
order by sal asc;
-- up, down이 나타나는 테이블
select emp_name, salary,w_sal,
case 
when salary <= (select round(avg(salary)) from employees) then nvl(salary,0)+(nvl(salary,0)*0.15)
when salary > (select round(avg(salary)) from employees) then nvl(salary,0)+(nvl(salary,0)* 0.05)
end as sal
from (
select emp_name, salary,
case
when salary <=6461 then 'down'
when salary > 6461 then 'up'
end as w_sal
from employees
order by salary asc
)
order by sal asc;

select emp_name, salary,
case
when salary <=6461 then 'down'
when salary > 6461 then 'up'
end as w_sal
from employees
order by salary asc;


--case 2개 사용
select emp_name, salary,
case 
when salary <= (select round(avg(salary)) from employees) then 'up'
when salary > (select round(avg(salary)) from employees) then 'down'
end as salary_updown
,
case 
when salary <= (select round(avg(salary)) from employees) then nvl(salary,0)+(nvl(salary,0)*0.15)
when salary > (select round(avg(salary)) from employees) then nvl(salary,0)+(nvl(salary,0)* 0.05)
end as sal

from (
employees
)
order by sal asc;

select * from stu_score;

select total, rank from stu_score
order by total desc;

--rank() 함수 , 컬럼을 하나 새롭게 만듦
select total, rank, rank() over (order by total desc) as ranks from stu_score;
-- 등수가 나옴
select num, rank() over (order by total desc) as ranks from stu_score;

select * from stu_score
order by total desc;

update stu_score set rank =1
where total=295;

--1000명 순위를 각각 입력
update stu_score a 
set rank = (
select ranks from (
select num, rank() over (order by total desc) as ranks from stu_score
) b
where a.num= b.num
);


--컬럼이 2개
select num, rank() over (order by total desc) as ranks from stu_score;

--컬럼이 1개
select ranks from (
select num, rank() over (order by total desc) as ranks from stu_score
) b;

select department_id,
case 
when department_id = 10 then '총무기획부'
when department_id = 20 then '마케팅'
when department_id = 30 then  '구매/생산부'
when department_id = 40 then  '인사부'
else '나머지'
end as department
from employees;

-- 두 테이블 조인해서 출력
select emp_name,department_id from employees;
select department_id, department_name from departments;

select emp_name, employees.department_id, department_name from employees, departments
where employees.department_id = departments.department_id;

-- 그룹합수 sum, avg, count, max, min, stddev 표준편차  varlance 분산

--월급 총합
select sum(salary) from employees;

--국어점수 총합
select sum(kor) from stu_score;

--부서번호가 50번인 사람
select count(*) from employees
where department_id = 50;

--commission을 받는 사원 수를 구하라
select emp_name, commission_pct from employees;
select count(*) from employees
where commission_pct is not null;

--group by 컬럼명 // 기준에 따라 묶는 것
select * from employees ;
select employees.employee_id from employees;
select e.employee_id from employees e;

-- 전체 사원 수 
select count(*) from employees;

-- 50번인 사원 수 
select count(*) from employees
where department_id = 50;
-- 부서별 그룹
select department_id,count(department_id) from employees
group by department_id
order by department_id
;
--stu_score 90점이상 A, 80점이상 B 70점이상 C 60점이상 D 60점미만 F
--컬럼명 avg/ grade

select name, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score;

-- stu_score에서 A가 몇 명인지 구하라 
select count(*) from (
select name, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score
)
where grade = 'A';

select grade, count(grade) from(
select name, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score
)
group by grade
order by grade asc;

--total 점수를 91, 92, 93...-> 90 91...89->80 해서 출력
--trunc
select kor, trunc(kor,-1) from stu_score
order by kor desc;

select count(*) from (select kor, trunc(kor,-1) from stu_score
order by kor desc)
where trunc(kor,-1) = 90
;

select trunc(kor,-1),count(*) from stu_score
group by trunc(kor,-1)
order by trunc(kor,-1) desc;

select trunc(kor,-1) as k_kor from stu_score;

select k_kor, count(k_kor) from (
select trunc(kor,-1) as k_kor from stu_score
)
group by k_kor;

select department_id, count(*) from employees
group by department_id
order by department_id;

--일반함수와 그룹함수를 같이 쓸 수 없음
select emp_name, count(emp_name) from employees;

--부서별 평균 월급을 구하시오
select salary, department_id, emp_name from employees;

select department_id,round(avg(salary),-2) from employees
group by department_id
order by department_id;

-- CLERK, REP,MAN 별 평균 월급
select round(avg(salary,-2)),salary, job_id from employees
where job_id like '%CLERK%'
group by job_id ;

select job_id,(select round(avg(salary),-2) from employees) from employees
where job_id like '%CLERK%' 
group by job_id ;

select round(avg(salary),-2) from employees
group by job_id ;

select job_id, count(job_id) from employees
where job_id like '%CLERK'
group by job_id;

--CLERK만 존재하는 컬럼 만들기, 문자열 자르기 substr
select substr(job_id,4,5) from employees
where job_id like '%CLERK';

select job_id, substr(job_id,4,length(job_id)-3) from employees;

select substr(job_id,4,7),count(substr(job_id,4,7)) from employees
where substr(job_id,4,7)='CLERK'
group by substr(job_id,4,7);

select substr(job_id,4,7),count(substr(job_id,4,7)) as c_job_id 
from employees
group by substr(job_id,4,7)
order by c_job_id;

--부서별 최대월급 최소 월급, 평균 월급

select department_id, max(salary), min(salary),sum(salary) ,round(avg(salary),-2) 
from employees 
where department_id is not null
group by department_id
order by department_id
;

--부서별 사원수, 커미션을 받는 사원수 출력
select * from employees;

select count(commission_pct) from employees
group by department_id;

select department_id, count(*), count(commission_pct)
from employees
group by department_id;

--having은 group by에 대한 조건절, where은 일반 컬럼의 조건절
select department_id,round(avg(salary),2) from employees
group by department_id
order by avg(salary);

select department_id,round(avg(salary),2) from employees
group by department_id
having avg(salary)>=6000
order by avg(salary);

--emp_name이 A로 시작하지 않는 것만 출력 // 순서 기억하기
select department_id,round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary)>=6000
order by avg(salary);

select emp_name from employees
where emp_name not like '_a%';
--평균 월급보다 작은 월급을 출력
select avg(salary) from employees;

select department_id,round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary)<=(select avg(salary) from employees)
order by avg(salary);

--부서별 최대 월급이 8000이상인부서, 최대 월급 출력
select department_id,max(salary) from employees
group by department_id
having max(salary) >= 8000
order by max(salary) desc
;

--조인 RDBMS equi  = 동일 칼럼 기준, non - equl = 동일칼럼이 없어 다른 조건 사용 ,
--outer 조인 조건에 만족하지 않는 행을 나타냄 , self join - 한 테이블 내에서 조인
select emp_name, department_id, salary from employees;

select department_id, department_name from departments;

select count(*) from employees; --107개
select count(*) from departments; -- 27개

select * from employees, departments;
--테이블 2개를 연결 한 것을 조인 이라고 함. cross join 형태 (의미X)
select count(*) from employees, departments; --107*27 = 2889 개

--equi join : 두 테이블 간의 같은 컬럼을 가지고 비교해서 해당되는 데이터를 출력

--equi join -106개, null 1개 검색되지 않음.
select department_id, department_name from departments;

select employee_id, emp_name, employees.department_id,department_name ,salary 
from employees, departments
where employees.department_id = departments.department_id;

select * from board;
select * from member;

select id, name from member;
select id, btitle, bcontent from board;

update member set name = '홍길자'
where id = 'aaa';

select * from member;

select bno, name, btitle, bcontent ,bdate,bgroup,bstep,bindent,bhit,bfile from board, member
where member.id= board.id;