select * from employees;
--ȸ������ ���̺� ����

create table member(
--column ,varchar:���ڿ�,����ڸ�����(�ѱ��� �ѱ��ڿ� 3�ڸ�����)
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

--������ �Է� ���ڶ� ''�־ ���
insert into member(id,pw,name,phone) values(
'aaa','1111','ȫ�浿','010-1111-1111'
);
insert into member values(
'bbb','1111','������','010-2222-2222'
);
insert into member(id,name,phone) values(
'ccc','�̼���','010-3333-3333'
);
--�÷� �� ���� ����
/*insert into member values(
'ddd','������','010-4444-4444'
);*/
--null : ���Ѵ밪
select id,pw,name,phone from member;

commit;

rollback;
select * from member;

insert into member values(
'ddd','1111','������','010-4444-4444'
);

commit;

select * from member;

update member set pw='2222' where id='ccc';

-- ��� ���̺� Ȯ��
select * from tab;

--���̺��� Ÿ�� Ȯ��
desc member;

--����Ŭ Ÿ��
--number-����, date-��¥, char-��������, varchar2-��������, clob-��뷮 ����

--number : ����, �Ǽ�
--number(4):-9999~9999 ����, 5�ڸ� �� �ȵ�
create table mem(
no number, -- ���� �������� ����.���Ѵ����� 21�ڸ�?
no2 number(4),
no3 number(4,2)
);

insert into mem (no) values (1234567890);

insert into mem (no2) values (9999);
insert into mem (no2) values (-9999);
insert into mem (no2) values (-99999);
insert into mem (no2) values (1.11); --1�� ��. �Ҽ��� �ڸ� ����X

insert into mem (no3) values (11.11);
insert into mem (no3) values (111); --111.00 : 5�ڸ� ��

select * from mem;
commit;
create table mem2(
no number(4,2),
mdate date,
mdate2 timestamp --date : ��,��,��,��,��,�� ���� = timestamp : �и��ʱ��� ���尡��.
);

insert into mem2(mdate) values('2024-04-19'); --24/04/19��� �������� 00:00:00�ʷ� ����
insert into mem2(mdate) values (sysdate); --sysdate:����ð�
insert into mem2(mdate2) values(sysdate);
insert into mem2(mdate,mdate2) values (sysdate,sysdate+30);


select * from mem2; 

select to_char(mdate,'yyyy/mm/dd hh:mi:ss') from mem2;
select to_char(mdate2,'yyyy/mm/dd hh:mi:ss:ff') from mem2;

select mdate,mdate2+30 from mem2; --select�� �������� �͸�

select * from employees;

select sysdate-hire_date from employees;

create table mem3 (
no number(4,2),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);
--char, varchar2
--char : ��������
insert into mem3 (tel) values ('11112222');
insert into mem3 (tel) values ('22223333');
insert into mem3 (tel) values ('111');
insert into mem3 (tel) values ('123456789');
insert into mem3 (tel) values ('ȫ');

--varchar2 : ��������
insert into mem3(name) values ('11112222');
insert into mem3(name) values ('ȫ�浿'); --�ѱ�ũ�� :3
insert into mem3(name) values ('�Ż��Ӵ�');-- ũ��:12
INSERT INTO MEM3(NAME) VALUES ('AAA');
insert into mem3(name) values ('aaa');

commit;

select * from mem,mem2;

--select,from 2���� Ű����� ������.
--��� �÷��� ���
-- ��ҹ��ڸ� �������� ����.
select * from mem3;
SELECT * FROM MEM3;
--sql������ ��ҹ��� ���о���, �����ʹ� ��ҹ��� ���е�
select name from mem3 where lower (name)='aaa'; --��� �ҹ��ڷ� �˻� 1.AAA 2.aaa
select * from mem3 where name ='AAA'; -- AAA
select * from mem3 where name ='aaa'; -- aaa

select emp_name,department_id from employees;
--distinct : ���� ���� 1���� ���
select distinct department_id from employees; --107��-> 12�μ�

select department_id, department_name from departments;
--����Ʈ�� ��ųʸ� ���·� ������
select * from departments; 
select * from employees;
select * from jobs;
select * from products; 
select job_id, min_salary from jobs;

select * from mem3;
select no, mdate2,name,mdate from mem3; --�÷��� ��ġ�� �ٲ� ����

select * from employees;

--�����ȣ, ����̸�, �޿�, �Ի�����
select employee_id,emp_name,salary, hire_date from employees;

desc employees; --�÷���, Ÿ���� ����

select * from stu_score;
--���̺� ����
drop table stu_score;

create table stu_score(
no number,
name varchar2(30),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(5,2),
rank number
);

insert into stu_score values(
1,'ȫ�浿',100,100,100,300,100,1
);

insert into stu_score values(
5,'�豸',100,100,100,300,100,1
);

commit;

select * from stu_score;

--��������� numberŸ���� ��츸 ����

select * from stu_score;

insert into stu_score values(
6,'������',100,95,96,(100+95+96),(100+95+96)/3,1
);

select * from stu_score;

insert into stu_score values(
7,'ȫ����',100,100,99,(100+99+100),(100+100+99)/3,1
);

--��ȣ, �̸�, ��������, ��������-20, ���,����-20�� �� ���
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select * from employees;
select commission_pct, salary from employees;

--salary �޷� -> ��ȭ ȯ��
select employee_id, emp_name,salary from employees;
select employee_id,emp_name, salary*1381.79 from employees;

select * from employees;
--Ŀ�̼�, ���� ���� =���� +Ŀ�̼�
select employee_id, emp_name, (salary*12*1381.79)+(commission_pct*1381.79) from employees;

select employee_id, emp_name, salary+(salary*commission_pct) from employees;
--nvl(�÷�,0)
select employee_id, emp_name, nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;

-- ���� *12 ->����
select employee_id, emp_name,(salary*12),(salary*12*1381.79),(commission_pct*1381.79) from employees;

commit;

