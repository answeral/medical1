select * from students;

select * from students
order by name asc;

--drop table students;
-- �÷��߰�
alter table students add rank number(3);

select * from students;

update students set rank = 0;

commit;

select rank() a over(order by total desc) rank
from students;

update students set total=0;

select * from students;

update students set total=(kor+eng+math);

--1 update ����
update student set rank =(rank);

--2.rank() ����
(select no,rank() over(order by total desc) ranks from students) b;

--3.update ������ rank() ������ no�÷����� ��,rank �÷��� �˻�
update students a set rank =(
select tanks from (students)b
where a.no = b.no);

--4.students ���̺��� ranks�� �� �ִ� ���̺��� �־���.
update students set rank = (
select ranks from (select no,rank() over(order by total desc) ranks from students) b
where a.no = b.no
);


update students a set rank= (select ranks
from(select no,rank() over (order by total desc) ranks
from students) b where a.no = b.no);

select total, rank from students
order by total desc;

--��������
select no, total, rank from students
order by total desc;

--no��������
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

--hire_date ��������, �÷� �����ȣ ����� job_id, �Ի���, ���� �÷� ���
select hire_date, employee_id,emp_name,job_id,salary from employees
order by hire_date asc;

--�޿��� ���� �޴� ������ ���, ������ ������ ��������� ��������
select salary, emp_name,employee_id, hire_date, job_id from employees
order by salary asc, emp_name asc;

--�����Լ� 
--abs
select -10, abs(-10) from dual;
--floor,round
select 34.789, floor(34.789) as f,round(34.789)as r from dual;
--round(���, �ڸ���) ex)round(34.178,2) �Ҽ��� 2�ڸ����� ǥ��, ��° �ڸ����� �ݿø�
select 34.178, round(34.178),round(34.178,2) from dual;

select avg from students;
select round(avg,2) avg from students;
-- 4���� �ݿø�, ������ �� ĭ. -2,-1,1,2,3,4 �ڸ� �� 
select 34.5678, round(34.5678,-1) from dual;

--trunc ������ �ڸ��� ���� ���� //floor�� �ڸ��� ������ �ȵ�
select trunc(34.5678,2) from dual;

select trunc(34.5678,-1) from dual;

select trunc(34.5678) from dual;

--ceil �ø� // �ڸ��� ����X
select ceil(34.123) from dual;

--�������� �ϴ��� �����ؼ� ���
select trunc(kor,-1) from students
order by kor;

--����, ���� ���� ���� �ϴ��� �����ؼ� ���� ���
select trunc(kor,-1) ����, trunc(eng,-1) ����, trunc(math,-1) ����
(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) �հ� from students;

--mod ������
select round(100/7,2) from dual;
select mod(10,7) from dual;
select 10/7 from dual;

-- �����ȣ�� ¦���� ���� ���
select employee_id from employees
where mod(employee_id,2)=0;

--select to_number(employee_id) i from employees
--where mod(employee_id,2)=0 ;

--��
select floor(10/7) from dual;
--������(�������� 0�̸� ¦��, 1�̸� Ȧ��)
select mod(10,7) from dual;

-- �л� �й��� 3�� ����� �͸� ���
select no from students
where mod(no,3)=0 ;

--������
create sequence seq_no
increment by 1  --���� 1�� ��
start with 1    --������ 1����
minvalue 1      -- �ּҰ� 1
maxvalue 9999   -- �ִ밪 9999
nocycle         -- ����Ŭ�� ����
nocache;        -- ĳ�� �����������

--nextval ������ ��ȣ 1�� ����
select seq_no.nextval from dual;
--currval ������ ��ȣ Ȯ��
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
seq_mno.nextval,'ddd','1111','������','010-4444-4444'
);

select * from member;

select sysdate from dual;
select to_char(sysdate,'yy')from dual;
--'00000'�ڸ���
select 's'||to_char(seq_mno.nextval,'00000') from dual;

--�ѱ����б� ko20240001
--������ seq_kono : 1-99999
create sequence seq_kono
increment by 1
start with 1
minvalue 1 
maxvalue 99999
nocycle
nocache
;

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) stuno from dual;

--�Խ���
create table board(
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
bdate date,
bhit number(10),
id varchar2(10)
);

--������ ����1001 ���� 10,1,99999
--5�� ����
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
emp_seq.nextval,'�̼���',sysdate
);

select * from emp01;

commit;

select employee_id, emp_name,job_id,hire_date from employees
order by hire_date desc;

--������� �Ի��� �ϼ��� ����Ͻÿ�.
select emp_name, hire_date, ceil(floor(sysdate-hire_date))||'��' dd from employees
order by hire_date desc;

select emp_name from employees;

-- ����, ����� ���ļ� ���
select job_id||employee_id from employees;

select substr(job_id, 0,2) from employees;

select emp_name,substr(emp_name,1,3) from employees;

--substr : ���ڿ� �ڸ��� �Լ�, substr(���, ������ġ,����)
--2��° �ڸ����� 3���� �߶� �����Ͷ�
select substr('abcde',2,3) from dual;

-- job_id���� �� 2�� ���ڿ� ���5�ڸ� ���ļ� ���
select substr(job_id,0,2),employee_id,to_char(employee_id,'00000'),
substr(job_id,0,2)||trim(to_char(employee_id,'00000'))from employees;
select substr(job_id,1,2)||'00'||employee_id from employees;

--��¥ �Լ�
select sysdate from dual;
select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;
-- �� ��¥ ������ ������ Ȯ��
select MONTHS_BETWEEN(SYSDATE,HIRE_DATE),SYSDATE-HIRE_DATE FROM EMPLOYEES;

--���� ���� �߰�
select sysdate,add_months(sysdate,2) from dual;

--���� ��¥ ���������� �������� ���� �������� ����?
select next_day(sysdate,'������') from dual;

--�Է��� �������� ������ ��¥�� �˷���
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;