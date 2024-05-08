-- ���̺� ����
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

--table ���� �� ������ �����ϱ�
desc employees;
--���̺� ���� - ������ �ٸ���
create table emp02 as 
select * from employees;

select * from emp02;
select * from employees;

--���̺� ������ �����ϱ�
create table emp03 as
select * from employees where 1=2;

select * from emp03;

--���̺� ������ �ٸ��鼭, �����͸� �����ϱ�(3��->14��)
insert into emp01(emp_id,emp_name,hire_date)
select employee_id, emp_name, hire_date from employees;

--1�� ������ �߰�
insert into emp01 values(
207,'ȫ�浿','2024-04-26'
);
--���̺��� ������ �����鼭, �����͸� ���� (������ ���� ���)
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

-- �÷� Ÿ�Ժ���
alter table member
modify (stu_name varchar2(30)
);

-- �÷� ����
alter table member
drop column pw;

--�÷� �߰�
alter table member
add (pw varchar2 (30)
);

select * from member;

select mno,id,pw,stu_name,gender from member;
select * from member;

--�÷� ���� ����
---�÷� �����
alter table member modify stu_name invisible;
alter table member modify gender invisible;
---�÷� ��Ÿ���� �ϱ�
alter table member modify stu_name visible;
alter table member modify gender visible;
--�÷� �Ͻ��� ��� ����
alter table member
set unused(id);

--��� ���� ����
alter table member
drop unused column;

select * from member;

--drop table emp03;

--���̺� �̸� ����
rename emp01 to employees01;

-- ���Ἲ ��������

--foreign key�� �ٸ� ���̺��� ������ �Է� ��
--����Ǿ� �ִ� ���� ���̺� �Է��Ϸ��� �����Ͱ� �ִ��� Ȯ��

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
'aaa','1111','ȫ�浿','male'
);

insert into member(id,pw,name) values(
'a','1111','ȫ�浿'
);

select * from member;
--���� ���� : unique - �ߺ��� ����, null�� ���
create table emp01(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp01 values(
5,'�豸',null,null
);

select * from emp01;

insert into emp02 values(
5,'������','���Ӹ�',17)
;

select * from emp02;

insert into emp03 values(
null,'������','2',2);

select * from emp03;

--1 ȫ�浿 �˻��ϱ�
select * from emp03
where EMPNO ='1' ;

select * from emp03
where empno is null and ename ='ȫ�浿';

select * from emp03
where empno is not null;

select * from emp03
where empno is null;

--foriegn key(�ܷ�Ű)
--drop table emp01;
--emp01�� ���̺� ����
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);

--dept01 ���̺� ����
create table dept01(
deptno number(20) primary key,
dept_name varchar2(20)
);

--�÷��� Ÿ�� ����
alter table dept01
modify (deptno number(6));

alter table dept01
modify (dept_name varchar(80));

alter table emp01
modify (deptno number(8));

alter table emp01
modify(deptno number(6));
--�÷��� ���� �߰�
insert into dept01(deptno,dept_name)
select department_id, department_name from departments;

insert into emp01 values(
3,'�̼���','0002',30
);

--deptno 10-270
insert into emp01 values(
5,'������','0002',280
);
--foreign key ����
alter table emp01
drop constraint fk_deptno;
--�ܷ�Ű�� ������ �Ǹ�, deptno�� ���� �����͸� �Է��� �ص� ������ ��.


commit;
--emp01�� foiegn key�� �߰�
--fk_deptno ��Ī
--add constraint ��Ī foreign key(���� �÷�) references �ٸ����̺�(�÷��̸�)
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
3,'ccc','�Խñ�3','����'
);
commit;

select * from board;

--comment ���̺� ��� ���̺�
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
--��۴ޱ�
insert into comments values(
2,1,'1111','��۳���1'
);
select * from board;
select * from comments;
--��� ����//
--fk�� ����� �� ���� fk�� ��ϵǾ� �ִ� ��� �����͸� ������Ű�� ��
--fk�� ��ϵǾ� �ִ� �����ʹ� ��� ���� ��Ű�� ��.
delete board where bno=1;

alter table board drop constraints fk_id;
select * from board;
select * from comments;

delete comments where cno=2;
delete board where bno=1;

alter table board
add constraint fk_id foreign key(id)
references member(id);

-- fk_cno�� ������ �ǵ��� ��
alter table comments 
add constraint fk_bno foreign key(cno)
references comments(cno) on delete cascade;


--check �������� Ư������ ����, Ư�� ���� �Էµǵ��� ��. -- �÷��� �����͸� ���� ������ �ڵ����� '0001'�� �����.
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', 
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in ('����','����'))
);

insert into emp(empno,ename, job, sal, gender) values(
1,'ȫ�浿','0001',3000,'����'
);
insert into emp(empno,ename, job, sal, gender) values(
2,'������','0001',4000,'����'
);
insert into emp(empno,ename, job, sal, gender) values(
3,'�̼���','0004',5000,'����'
);
insert into emp(empno,ename, job, sal, gender) values(
4,'������','0006',6000,'����'
);
--2000~20000������ ����
insert into emp(empno,ename, job, sal, gender) values(
5,'�豸','0006',30000,'����'
);

insert into emp(empno,ename, job, sal, gender) values(
5,'�豸','0006',20000,'����'
);

insert into emp(empno,ename, job, sal, gender) values(
6,'������',10000,'����'
);


