select * from stu_score order by no;

select * from students;

--drop table students;

update students set id = 'aaa',name='홍길동',gender='M'
where id ='Honey';

update students set id = 'bbb', name='유관순', gender = 'F'
where id = 'Caroline';

update students set id ='ccc', name = '이순신', gender = 'M'
where id = 'Guthrey';

update students set id = 'ddd', name = '강감찬', gender = 'M' where id = 'Marjory';
update students set id = 'eee', name = '김구', gender = 'M' where id = 'Chickie';
update students set id = 'fff', name = '김유신', gender = 'M' where id = 'Edithe';
update students set id = 'ggg', name = '홍길자', gender = 'F' where id = 'Ranna';
update students set id = 'hhh', name = '홍길순', gender = 'F' where id = 'Terry';

commit;
--새롭게 순차적 번호 생성 : rownum
select rownum, a.* from students a
order by grade;
--1. select 구문
select  a.* from students a;
--2. rownum 함수 실행
select rownum,a.* from students a;
--3. order by 구문 실행
select rownum, a.* from students a
order by grade;

--1.select 2. order by 3. rownum
select * from students
order by grade;

select rownum, a.* from (
select * from students
order by grade
) a 
;
-- 평균 85점이상 & no > 500
select * from stu_score
where avg >= 85 and no > 500
order by no;

select * from stu_score
where avg >= 85;

select * from
(select * from stu_score where avg >= 85)
where no>500
order by no
;
-------------------------------------------------------------------
--테이블명 shop_product

select name, amount from shop_product
where pdate>='2024-03-01';

--이름별로 구매내역 합계를 구하시오. sum(acount) 가상으로 만들어진 컬럼

--error
select name, sum(amount),rank from shop_product, customer_rank
where pdate >= '2024-03-01' and 
sum(amount) between lower_amount and high_amount
group by name,rank;

--equi join : 같은 컬럼이 2개의 테이블에 존재하여 2개의 컬럼을 이용해 검색하는 방법
----- non-euqi join : 같은 컬럼이 없으면서 2개 테이블을 사용해 검색하는 방법
select name, s_amount,rank from (
select name, sum(amount) as s_amount from shop_product
where pdate>='2024-03-01'
group by name),customer_rank
where s_amount between lower_amount and high_amount
;

--1.
select name, sum(amount) as s_amount from shop_product
where pdate>='2024-03-01'
group by name
;

select * from customer_rank;

--non-equi join : 같은 컬럼이 없는 것을 합쳐서 보여주는 거 
select * from stu_score;
select * from stu_grade;

select name, avg, grade from stu_score, stu_grade
where avg between low_score and high_score
order by grade;

select * from customer_rank;

select rownum, a.* from students a
order by id;



select rownum rnum ,a.* from (
select * from students  order by id
)a
;


select * from
(select rownum rnum, b.* from (
select * from students a order by id) b
)
where rnum>=11 and rnum<=20
;

--row_number()
select * from(
select  row_number() over(order by id) rnum,a.*
from students a)
where rnum>=31 and rnum<=40;

--self join : 같은 테이블 2개 사용, 자기 자신과 조인
select employee_id, emp_name, a.manager_id, a.department_id, b.department_name from employees a,departments b
where a.manager_id = b.manager_id
order by a.department_id;

--cross join 107*107
--equi join : 2개테이블이 같은 컬럼을 가지고 검색
select emp_name, employee_id, manager_id from employees;

--self join 과 equi join을 함께 사용
select a.employee_id, a.emp_name, a.manager_id,department_name ,a.department_id ,b.emp_name 
from employees a,employees b, departments c
where a.manager_id = b.employee_id and a.department_id = c. department_id
order by a.employee_id
;

--self join
select a.employee_id, a.emp_name, a.manager_id, b.emp_name from employees a, employees b
where a.manager_id = b.employee_id
order by a.employee_id;

--john chen 과 동일한 부서에 근무하는 사람을 출력
select * from employees;
select* from departments;
--john 부서 출력 // 30번
select a.emp_name,a.department_id,b.department_name from employees a, departments b
where emp_name = 'Guy Himuro'  and a.department_id = b.department_id;

--2. 부서번호를 갖고 같은 사람 출력
select a.emp_name, a.department_id, b.department_id, b.emp_name from employees a, employees b
where a. department_id =b.department_id and a.emp_name = 'Guy Himuro';

-- 정답 풀이
select emp_name, department_id from employees
where department_id = 30;

select e1.emp_name, e1.department_id, e2.emp_name
from employees e1, employees e2 
where e1.department_id = e2. department_id and e1.emp_name = 'Guy Himuro'; 

select * from member;

insert into member values(
member_seq.nextval, 'ggg',1111,'홍길순','여자',sysdate
);
desc member;

commit;

rollback;

select * from member;

update member set name='홍길동' where id= 'aaa';

select * from employees
order by emp_name
;
select emp_name from employees
where emp_name like '%h%';

select a.emp_name,a.department_id,c.department_name ,b.emp_name from employees a, employees b,departments c
where a.department_id = b.department_id and a.emp_name ='Pat Fay'
and a.department_id = c.department_id
;

select * from member order by id;
---hhh,1111,홍길자, 여자 sysdate

select * from member;


create table mem(
id varchar2(30) primary key,
pw varchar2(30),
name varchar2(30),
mdate date


);

select * from mem;

--drop table mem;

create table yeogi(
yno number(4) primary key,
title varchar2 (100) not null,
local varchar2(30),
score number,
member number,
img varchar2(100),
price number
)
;

select * from yeogi;

