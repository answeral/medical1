-- 테이블 생성
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

--table 구조 및 데이터 복사하기
desc employees;
--테이블 생성 - 구조를 다르게
create table emp02 as 
select * from employees;

select * from emp02;
select * from employees;

--테이블 구조만 복사하기
create table emp03 as
select * from employees where 1=2;

select * from emp03;

--테이블 구조가 다르면서, 데이터만 복사하기(3개->14개)
insert into emp01(emp_id,emp_name,hire_date)
select employee_id, emp_name, hire_date from employees;

--1개 데이터 추가
insert into emp01 values(
207,'홍길동','2024-04-26'
);
--테이블이 구조가 같으면서, 데이터만 복사 (구조가 같은 경우)
insert into emp03(
select * from employees
);
select * from emp03;
select * from emp01
order by emp_id desc;
select * from employees;

--drop table s_info;
--drop table m_date;

desc member;

-- 컬럼 타입변경
alter table member
modify (stu_name varchar2(30)
);

-- 컬럼 삭제
alter table member
drop column pw;

--컬럼 추가
alter table member
add (pw varchar2 (30)
);

select * from member;

select mno,id,pw,stu_name,gender from member;
select * from member;

--컬럼 순서 변경
---컬럼 숨기기
alter table member modify stu_name invisible;
alter table member modify gender invisible;
---컬럼 나타나게 하기
alter table member modify stu_name visible;
alter table member modify gender visible;
--컬럼 일시적 사용 제한
alter table member
set unused(id);

--사용 제한 해제
alter table member
drop unused column;

select * from member;

--drop table emp03;

--테이블 이름 변경
rename emp01 to employees01;

-- 무결성 제약조건

--foreign key는 다른 테이블에서 데이터 입력 시
--선언되어 있는 기존 테이블에 입력하려는 데이터가 있는지 확인

--drop table employees01;
--drop table emp02;
--drop table member;
--drop table board;

create table member (
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6)
);

insert into member values(
'aaa','1111','홍길동','male'
);

insert into member(id,pw,name) values(
'a','1111','홍길동'
);

select * from member;
--제약 조건 : unique - 중복만 제거, null은 허용
create table emp01(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp01 values(
5,'김구',null,null
);

select * from emp01;

insert into emp02 values(
5,'김유신','말머리',17)
;

select * from emp02;

insert into emp03 values(
null,'강감찬','2',2);

select * from emp03;

--1 홍길동 검색하기
select * from emp03
where EMPNO ='1' ;

select * from emp03
where empno is null and ename ='홍길동';

select * from emp03
where empno is not null;

select * from emp03
where empno is null;

--foriegn key(외래키)
--drop table emp01;
--emp01번 테이블 생성
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);

--dept01 테이블 생성
create table dept01(
deptno number(20) primary key,
dept_name varchar2(20)
);

--컬럼의 타입 변경
alter table dept01
modify (deptno number(6));

alter table dept01
modify (dept_name varchar(80));

alter table emp01
modify (deptno number(8));

alter table emp01
modify(deptno number(6));
--컬럼의 내용 추가
insert into dept01(deptno,dept_name)
select department_id, department_name from departments;

insert into emp01 values(
3,'이순신','0002',30
);

--deptno 10-270
insert into emp01 values(
5,'강감찬','0002',280
);
--foreign key 삭제
alter table emp01
drop constraint fk_deptno;
--외래키가 삭제가 되면, deptno에 없는 데이터를 입력을 해도 저장이 됨.


commit;
--emp01에 foiegn key를 추가
--fk_deptno 별칭
--add constraint 별칭 foreign key(현재 컬럼) references 다른테이블(컬럼이름)
alter table emp01
add constraint fk_deptno foreign key (deptno)
references dept01(deptno)
;


desc dept01;
select * from departments;

create table board (
bno number(4) primary key,
id  varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);

alter table board
add constraint fk_id foreign key(id)
references member (id);

insert into board values(
3,'ccc','게시글3','내용'
);
commit;

select * from board;

--comment 테이블 댓글 테이블
create table comments(
cno number(4) primary key,
bno number(4),
cpw varchar2(20),
ccontent varchar2(1000),
constraint fk_bno foreign key(bno)
references board(bno)
);

--cno number(4) primary key
--bno number(4) 
--cpw varchar2(20)
-- ccontent varchar2(1000)

select * from board;
--댓글달기
insert into comments values(
2,1,'1111','댓글내용1'
);
select * from board;
select * from comments;
--댓글 삭제//
--fk를 등록할 때 설정 fk로 등록되어 있는 모든 데이터를 삭제시키는 것
--fk로 등록되어 있는 데이터는 모두 존재 시키는 것.
delete board where bno=1;

alter table board drop constraints fk_id;
select * from board;
select * from comments;

delete comments where cno=2;
delete board where bno=1;

alter table board
add constraint fk_id foreign key(id)
references member(id);

-- fk_cno가 삭제가 되도록 함
alter table comments 
add constraint fk_bno foreign key(cno)
references comments(cno) on delete cascade;


--check 제액조건 특정값의 범위, 특정 값만 입력되도록 함. -- 컬럼에 데이터를 넣지 않으면 자동으로 '0001'이 저장됨.
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', 
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in ('남자','여자'))
);

insert into emp(empno,ename, job, sal, gender) values(
1,'홍길동','0001',3000,'남자'
);
insert into emp(empno,ename, job, sal, gender) values(
2,'유관순','0001',4000,'여자'
);
insert into emp(empno,ename, job, sal, gender) values(
3,'이순신','0004',5000,'남자'
);
insert into emp(empno,ename, job, sal, gender) values(
4,'강감찬','0006',6000,'남자'
);
--2000~20000까지만 가능
insert into emp(empno,ename, job, sal, gender) values(
5,'김구','0006',30000,'남자'
);

insert into emp(empno,ename, job, sal, gender) values(
5,'김구','0006',20000,'남자'
);

insert into emp(empno,ename, job, sal, gender) values(
6,'김유신',10000,'남자'
);


