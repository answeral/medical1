--drop table board;
--DROP TABLE board CASCADE CONSTRAINTS;
-- ���Ἲ �������� : �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
--not null, unique, primary jey, foreign key, check
create table member(
memno number(4)not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����','����')),
mdate date default sysdate
);

--������ �Է�, ���, ����, ���� �κ�
insert into member (memno, id,pw, name, gender, mdate) values(
member_seq.nextval,'aaa','1111','ȫ�浿','����',sysdate
);

insert into member(memno, id, pw, name, gender) values (
member_seq.nextval, 'bbb','1111','������','����');

insert into member values(
member_seq.nextval, 'ccc','1111','�̼���','����',sysdate);

select * from member;

--���̺� ����
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
constraint fk_id foreign key(id) --�ܷ�Ű(foreign key)�� ��Ī : fk_id
references member(id) --member ü�̺���primaty key�� id�� ������ �Ǿ�����,
--(foreigm key�� �����Ϸ��� primary key�� ������ �Ǿ��־����)
);  

--alter table board rename column bmo to bno;

--primary key�� �����Ϸ��� foreign key�� ��ϵǾ� �ִ� �����͸� �켱 ������ ��� �ؾ���.
-- 1.primary key ���� �Ǹ� ��� �����ϴ� ��� - on delete cascaed, 2. ��� �����ϴ� ��� - on update cascade

insert into board(bmo,id,btitle, bcontent, bdate, bgroup, bstep,bindent,bhit,bfile) values(
BOARD_SEQ.nextval,'aaa','�����Դϴ�.','�����Դϴ�.',sysdate, board_seq.currval,0,0,1,''
);

insert into board values(
BOARD_SEQ.nextval,'bbb','�����Դϴ�2.','�����Դϴ�2.',sysdate, board_seq.currval,0,0,1,''
);

insert into board(bmo,id,btitle, bcontent, bgroup) values(
BOARD_SEQ.nextval,'aaa','�����Դϴ�.3','�����Դϴ�.3', board_seq.currval
);
--����
delete board where bmo =3;

select * from board;

commit;

delete member where id='aaa';

--decode ���ǹ�
select emp_name, department_id,
decode (department_id,
10,'�ѹ���ȹ��',
20,'������',
30,'����/�����',
40,'�λ��')
from employees
order by department_id asc;

select * from stu_score
order by avg desc;
--90�� A,80�� B, 70�� C

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
 -- sH_clerk salary*15%, ad_asst*10% MK_rop *5% ���� �λ�
 select job_id, salary,
 decode (job_id,
 'SH_CLERK',nvl(salary,0)+ (nvl(salary,0)*0.15),
 'AD_ASST', nvl(salary,0)+ (nvl(salary,0)*0.1),
 'MK_ROP', nvl(salary,0)+(nvl(salary,0)*0.05))
 as salary_up from employees
;

 
-- job_id �߿� clerk�� �� �ִ� job_id�� �˻��ϱ�
-- _�ڸ��� , % ��� ��
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

--case ����, department_id �̸��� ���
select department_id from employees
order by department_id asc;

select department_id,
case 
when department_id = 10 then '�ѹ���ȹ��'
when department_id = 20 then '������'
when department_id = 30 then  '����/�����'
else '������'
end as department
from employees;

--���� ��� job_id
--CLERK ���� :salary*15%, ad_asst *10% rep*5%, man*25%
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
-- ���� ��� ������ ����� 0.15 ����̻��� ����� 0.05 �λ��ؼ� ���
select round(avg(salary)) from employees;

--employees���� �˻�, up,down�� ��Ÿ���� ����
select emp_name, salary,w_sal,
case 
when salary <= (select round(avg(salary)) from employees) then nvl(salary,0)+(nvl(salary,0)*0.15)
when salary > (select round(avg(salary)) from employees) then nvl(salary,0)+(nvl(salary,0)* 0.05)
end as sal
from (
employees
)
order by sal asc;
-- up, down�� ��Ÿ���� ���̺�
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


--case 2�� ���
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

--rank() �Լ� , �÷��� �ϳ� ���Ӱ� ����
select total, rank, rank() over (order by total desc) as ranks from stu_score;
-- ����� ����
select num, rank() over (order by total desc) as ranks from stu_score;

select * from stu_score
order by total desc;

update stu_score set rank =1
where total=295;

--1000�� ������ ���� �Է�
update stu_score a 
set rank = (
select ranks from (
select num, rank() over (order by total desc) as ranks from stu_score
) b
where a.num= b.num
);


--�÷��� 2��
select num, rank() over (order by total desc) as ranks from stu_score;

--�÷��� 1��
select ranks from (
select num, rank() over (order by total desc) as ranks from stu_score
) b;

select department_id,
case 
when department_id = 10 then '�ѹ���ȹ��'
when department_id = 20 then '������'
when department_id = 30 then  '����/�����'
when department_id = 40 then  '�λ��'
else '������'
end as department
from employees;

-- �� ���̺� �����ؼ� ���
select emp_name,department_id from employees;
select department_id, department_name from departments;

select emp_name, employees.department_id, department_name from employees, departments
where employees.department_id = departments.department_id;

-- �׷��ռ� sum, avg, count, max, min, stddev ǥ������  varlance �л�

--���� ����
select sum(salary) from employees;

--�������� ����
select sum(kor) from stu_score;

--�μ���ȣ�� 50���� ���
select count(*) from employees
where department_id = 50;

--commission�� �޴� ��� ���� ���϶�
select emp_name, commission_pct from employees;
select count(*) from employees
where commission_pct is not null;

--group by �÷��� // ���ؿ� ���� ���� ��
select * from employees ;
select employees.employee_id from employees;
select e.employee_id from employees e;

-- ��ü ��� �� 
select count(*) from employees;

-- 50���� ��� �� 
select count(*) from employees
where department_id = 50;
-- �μ��� �׷�
select department_id,count(department_id) from employees
group by department_id
order by department_id
;
--stu_score 90���̻� A, 80���̻� B 70���̻� C 60���̻� D 60���̸� F
--�÷��� avg/ grade

select name, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score;

-- stu_score���� A�� �� ������ ���϶� 
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

--total ������ 91, 92, 93...-> 90 91...89->80 �ؼ� ���
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

--�Ϲ��Լ��� �׷��Լ��� ���� �� �� ����
select emp_name, count(emp_name) from employees;

--�μ��� ��� ������ ���Ͻÿ�
select salary, department_id, emp_name from employees;

select department_id,round(avg(salary),-2) from employees
group by department_id
order by department_id;

-- CLERK, REP,MAN �� ��� ����
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

--CLERK�� �����ϴ� �÷� �����, ���ڿ� �ڸ��� substr
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

--�μ��� �ִ���� �ּ� ����, ��� ����

select department_id, max(salary), min(salary),sum(salary) ,round(avg(salary),-2) 
from employees 
where department_id is not null
group by department_id
order by department_id
;

--�μ��� �����, Ŀ�̼��� �޴� ����� ���
select * from employees;

select count(commission_pct) from employees
group by department_id;

select department_id, count(*), count(commission_pct)
from employees
group by department_id;

--having�� group by�� ���� ������, where�� �Ϲ� �÷��� ������
select department_id,round(avg(salary),2) from employees
group by department_id
order by avg(salary);

select department_id,round(avg(salary),2) from employees
group by department_id
having avg(salary)>=6000
order by avg(salary);

--emp_name�� A�� �������� �ʴ� �͸� ��� // ���� ����ϱ�
select department_id,round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary)>=6000
order by avg(salary);

select emp_name from employees
where emp_name not like '_a%';
--��� ���޺��� ���� ������ ���
select avg(salary) from employees;

select department_id,round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary)<=(select avg(salary) from employees)
order by avg(salary);

--�μ��� �ִ� ������ 8000�̻��κμ�, �ִ� ���� ���
select department_id,max(salary) from employees
group by department_id
having max(salary) >= 8000
order by max(salary) desc
;

--���� RDBMS equi  = ���� Į�� ����, non - equl = ����Į���� ���� �ٸ� ���� ��� ,
--outer ���� ���ǿ� �������� �ʴ� ���� ��Ÿ�� , self join - �� ���̺� ������ ����
select emp_name, department_id, salary from employees;

select department_id, department_name from departments;

select count(*) from employees; --107��
select count(*) from departments; -- 27��

select * from employees, departments;
--���̺� 2���� ���� �� ���� ���� �̶�� ��. cross join ���� (�ǹ�X)
select count(*) from employees, departments; --107*27 = 2889 ��

--equi join : �� ���̺� ���� ���� �÷��� ������ ���ؼ� �ش�Ǵ� �����͸� ���

--equi join -106��, null 1�� �˻����� ����.
select department_id, department_name from departments;

select employee_id, emp_name, employees.department_id,department_name ,salary 
from employees, departments
where employees.department_id = departments.department_id;

select * from board;
select * from member;

select id, name from member;
select id, btitle, bcontent from board;

update member set name = 'ȫ����'
where id = 'aaa';

select * from member;

select bno, name, btitle, bcontent ,bdate,bgroup,bstep,bindent,bhit,bfile from board, member
where member.id= board.id;