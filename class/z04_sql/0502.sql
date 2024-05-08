-------equi join
-- 2개 테이블 department_id 가 동일
select *  from employees;
select * from departments;

select employee_id, a.department_id, department_name
from employees a, departments b
where a.department_id = b. department_id
;
-- 
select * from stu_score;
select * from students;

--홍길동 학생
-- 학생성적의 모든 내용과 전화번호, 이메일, 과, 학년
--name이 동일한 항목

select * from stu_score
where name = '홍길동';

select id, name, phone, email,major, grade from students
where name = '홍길동';

desc stu_score;

select no,id,a.name, phone, email, major, grade, kor , eng, math , total, avg, rank
from stu_score a, students b
where a.name = '홍길동' and a.name = b.name;

select count(*) from stu_score;
select count(*) from students;

--alter table students add no number(38);
--insert into students(no) select no from stu_score;

--rownum 만들어진 번호를 no에 넣기
update students b set no= (
select rnum from 
(select rownum rnum,id from students ) a
)
where a.id = b.id;

update sutdents b
set no = a.rnum
from (
select rownum rnum,id from students 
) a
where b.id = a.id
;

select rnum from 
(select rownum rnum, a.* from students a);

drop table students;
drop table stu_score;

select * from students;
select * from stu_score;

--2개 테이블 join 할 때 1개의 동일한 컬럼이 있어야함
--1개의 동일한 컬럼은 중복이 없어야함. 2개 중에 한 곳에는 primary키가 사용이 되어있어야 함.
select a.id, a.name, phone total, avg from students a, stu_score b
where a.id = b.id
order by name;

--self join 
--동일한 테이블을 가지고 서로 join
select a.employee_id,a.department_id,a.job_id ,a.emp_name ,a.manager_id, b.emp_name from employees a, employees b
where a.manager_id = b.employee_id
order by a.department_id;

desc stu_score;
desc students;

drop table students;

select * from stu_score;
select * from students;

update stu_score a
set rank = (select ranks from
(select no,id,rank() over(order by total desc) as ranks ,rank, total from stu_score) b
where a.no = b.no)
;

--rank
select ranks from
(select no,id,rank() over(order by total desc) as ranks ,rank, total from stu_score a) b
;

select no,id,rank() over(order by total desc) as ranks ,rank, total from stu_score;
select * from students;
-----------------------------------------------
select * from member;

alter table member add no number;

select rownum, a.* from member a;
--1.
select rownum rnum,id from member;
-- 2. rnum만 가져오기
select rnum from(select rownum rnum,id from member);
--3. 완성!~
update member a 
set no = (select rnum from(select rownum rnum,id from member) b  where a.id = b.id)
;

select * from member;
update stu_score set rank=0;

commit;

select total, rank from stu_score
order by total desc;

--랭킹을 계산한 것
select total, rank() over(order by total desc) ranks from stu_score;
--가상의 숫자를 붙인 것
select row_number() over(order by total desc) rnum, total from stu_score;
-- stu_score에 랭크 업데이트 하기~
select ranks, total from(select total, rank() over(order by total desc) ranks from stu_score);

update stu_score a set rank = 
(select ranks from
(select no, rank() over(order by total desc) ranks from stu_score) b
where a.no = b.no);

select * from stu_score
order by rank;

--row_number() over()
select * from stu_score;

select rownum rnum, a.* from stu_score a
order by total desc;

select * from(
select rownum rnum, a.* from 
(select * from stu_score order by total desc) a
)
where rnum >= 1 and rnum<=100 ;

select row_number() over(order by total desc) rnum, a.* from ste_score a
where rnum >=1 and rnum <= 10;

select employee_id, emp_name, manager_id from employees
order by employee_id
;

--self join manager_id, 이름 출력
select * from employees; --107개
--outer join :값이 충족되지 않아도출력되도록 함(null값 출력)
--null 값이 있는 반대편 항목에 (+)기호를 넣으면 됨.
select a.employee_id, a.emp_name, a.manager_id,b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id(+);

select manager_id, emp_name from employees
where emp_name ='Diana Lorentz';

--outer join , equi join
--employees 테이블 부서번호 10-110번
select emp_name,b.department_id, department_name 
from employees a, departments b
where a.department_id(+) = b.department_id
order by department_id; --110개

--10번 - 270번까지
select department_id from departments;

--ANSI join
select * from employees cross join departments;
select * from employees, departments;
--1  //1,2,3 같은 결과
select a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id;
--2 inner join - on
select a.department_id, b.department_name 
from employees a inner join departments b
on a.department_id = b.department_id;
--3   join - using
select *
from employees join departments 
using (department_id)
;

select a.*, department_name
from employees a, departments b
where a.department_id = b.department_id;


--ANSI join 중 natural join
select * from employees natural join departments;

-- ANSI join 중 outer join
--left outer join - on
--1
select a.emp_name, a.manager_id, b.emp_name 
from employees a
left outer join employees b
on a.manager_id = b. employee_id;
--2 // 1,2 같은 결과
select a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b. employee_id(+);
--3 right outer join - on 
select a.emp_name, a.manager_id, b.emp_name 
from employees a
right outer join employees b
on a.manager_id = b. employee_id;
--4 // 3,4 같은 결과
select a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id(+) = b. employee_id;
-- 5. full outer join - on은 양쪽 null 값 모두 나타남
select a.emp_name, a.manager_id, b.emp_name 
from employees a
full outer join employees b
on a.manager_id = b. employee_id;

select * from stu_score
where id like '%a'
order by no
;

--row_number() over()
--11-20까지 출력
select * from
(select * from 
(select row_number() over (order by no) rnum,a.* from stu_score a)
where id like '%a%')where rnum>=11 and rnum<=20;

select count(*) from (select row_number() over (order by no ) rnum,a.* from stu_score a
where id like '%a%');


create table melon(
mno number primary key ,
rank number,
v_rank number,
img varchar2(100),
title varchar2(100),
singer varchar2(100),
likeNum number
);

create table yanolja(
yno number primary key,
img varchar2(100),
title varchar2(100),
grade number,
grade_num number,
price number
);

alter table melon modify img varchar2(300);



commit;



