--����, ���� , ����
select sysdate-1, sysdate, sysdate+1 from dual;

--����, �� ���� ù ��, ���� ������ ��
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;

-- �� ��¥ �� �� ��, �� ��¥ �� �� �� 
select round(sysdate-hire_date,3),trunc(months_between(sysdate,hire_date),2) from employees;

--trunc �� ���� �ڸ� ���� gruop by �׷��Լ�
select trunc(kor,-1) kor ,count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;

--hire_date ��¥���� ���� ���
select hire_date from employees;
select hire_date, to_char(hire_date,'mm') from employees;

select to_char(hire_date,'mm') hire_date, count(to_char(hire_date,'mm')) from employees
group by to_char(hire_date,'mm')
order by hire_date;

--hire_date 2008�⵵�� ����ϰ� �⵵�� �ο����� ����Ͻÿ�.
select to_char(hire_date,'yyyy'), count(to_char(hire_date,'yyyy'))from employees
group by to_char(hire_date,'yyyy')
order by hire_date;

--����ȯ - number, character, date
-- number ��Ģ������. ��ǥǥ�þȵ�, ��ȭǥ�þȵ�.
--char ��Ģ���� �ȵ�. ��ǥǥ�ð���, ��ȭ ǥ�� ����
--date +,- ���� ��¥������´� ����Ұ�-> to_char�� �ٲ����

--������ ���·� �й��� �ο�
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

--����Ÿ�����¸� ��¥Ÿ������ ����
select 20240425 +3 from dual;
select to_char(20240425 +3) from dual;
select to_date(20240425 +3) from dual;

--����Ÿ���� ��¥ Ÿ������ ����
select emp_name,hire_date from employees
where hire_date >= to_date(20070101)
order by hire_date desc;

--����̸� 8�� �Ի��� ����̸� 2��°�� a�� ���ִ»�� ���
select emp_name, hire_date from employees
where emp_name like '_a%';
select emp_name, hire_date from employees
where to_char(hire_date,'mm')=08;

select emp_name, hire_date from employees
where emp_name like '_a%' and 
to_char(hire_date,'mm')=08 ;

-- 20070101 ���� �Ի��� ����̸� 2��°�� a�� �� �ִ� ���
select emp_name, hire_date from employees
where emp_name like '_a%' and
hire_date >= to_date(20070101);

select emp_name, hire_date from employees
where emp_name like '_a%' and 
to_char(hire_date,'mm')=08 or to_char(hire_date,'mm')=05 or to_char(hire_date,'mm')=01;

--01,05,08���� �Ի��� ���
select hire_date from employees
where to_char(hire_date,'mm') in ('01','05','08');
--�̸�
select emp_name from employees
where emp_name like '_a%';
--�Ի��ϰ� �̸� ��ġ��
select emp_name, hire_date from employees
where emp_name like '_a%' and to_char(hire_date,'mm') in ('01','05','08')
order by hire_date;

--���� Ÿ���� ��¥ Ÿ������ ����
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

-- �Է½� ��¥ Ÿ�Կ� ����(����-��¥����)�� �Է��ص� �����.
-- ���ڿ� ���ڸ� ����� �Ұ���, �׷��� ���ڸ� ��¥Ÿ������ �����ؾ���.
insert into eventdate values(
seq_mno.nextval, sysdate, '2024-04-01',sysdate - to_date('2024-04-01')
);

--����Ÿ���� ����Ÿ������ ����
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

--null �� 0���� ġȯ nvl()
select salary,commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;

--manager_id null ceo
select manager_id from employees
order by manager_id desc;

-- ����Ÿ���� ����Ÿ������ ����
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;
-- �׷��Լ� : sum, count(), count(*), min,max
-- count : ����
select count(emp_name) from employees;
--����� : 107��
select count(*) from employees;
--null���� ������ ���� - ����� : 106��
select count(manager_id) from employees;

select emp_name, manager_id from employees;

-- sum : �� ��
select sum(salary) from employees;

--avg :���
select avg(salary) avg_sal from employees;

--min : �ּҰ�, max : �ִ밪
select min(salary),max(salary) from employees;

-- 6461�޷����� ���� ����� ����Ͻÿ�, ��������
select emp_name, salary from employees
where salary > (select avg(salary) avg_sal from employees) ;

select min(salary) from employees;
select * from employees;

--�ִ������ �޴� ����� ��� �̸� ���
select employee_id,emp_name,salary from employees
where salary = (select max(salary) from employees);

--�μ���ȣ�� 50���� ����� ��ü ����
select department_id ,salary from employees;
select sum(salary) from employees
where department_id = 50;

select count(*) from stu_score;
select * from stu_score;
-- kor = 75�� �̻��� �л� ���
select kor, name from stu_score
where kor>=80;

select avg(kor) from stu_score;

--�������� ����̻�, ���� ���� ����̻��� �л� ���
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

--�������� �ְ����� �л�, �������� �ְ����� �л� ���� ���� �ְ����� �л��� ����ض�
select name, kor, eng, math, avg from stu_score
where kor= (select max(kor) from stu_score) 
or eng = (select max(eng) from stu_score)
or math =  (select max(math) from stu_score)
order by avg desc;

--������ �ִ�, �ּ� , ����� ��� ���
select emp_name, salary from employees
where salary = (select max(salary)  from employees)
or salary  = (select min(salary)  from employees)
or salary = (select avg(salary) from employees);

--�ִ밪
select emp_name, salary from employees
where salary = (select max(salary) from employees);

--��պ��� ���� ��� 
--56���� �����
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc;
--select max(salary) from (���̺�)
--56�� �� �ִ밪 : ��հ����� ���� ����߿� �ִ밪�� ����Ͻÿ�
-- 1. ��հ����� ���� ��� ���
select emp_name, salary from employees
where salary =6400;

select emp_name, salary from employees
where salary =(select max(salary) from(
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
)
) ;

-- 2. �� �߿� ���� ���� ��� ���
select max(salary) from(
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
);
--power(a,b): a��b����

--�����Լ�
--lpad: ����� ä��� 
--: �ڸ���, ���ʺ���� rpad : �ڸ���, ������ �����
select emp_name, lpad(emp_name,15,'#') from employees;
select emp_name, rpad(emp_name, 20,'@') from employees; 

--ltrim, rtim ������ ������ ����, ������ �ڸ���
select emp_name, ltrim(emp_name,'Do') from employees;

select 'ko20240001',ltrim('ko20240001','ko2024') from dual;
--substr(������,����, ����) ex)substr('abcdefg',3,3) -> cde 
select emp_name, substr(emp_name,3,4) from employees;

select job_id, employee_id from employees;
-- SH�� �����ȣ�� �����ؼ� ����Ͻÿ�
select job_id, substr(job_id,1,2) from employees;
select  substr(job_id,1,2)||employee_id from employees;

--length
select emp_name, length(emp_name) from employees
where length(emp_name)>15;
--��¥ �Լ�, +,- ���� ��¥�����ͳ���
--��¥�Լ� + 1 ����
select sysdate +1 from dual;
--��¥������ - ��¥�����ʹ� ����
select sysdate - hire_date from employees;

--��¥������+��¥�����ʹ� �Ұ���
select sysdate + hire_date from employees;

select round(sysdate,'month') from dual;

select trunc(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

select trunc(sysdate, 'year') from dual;

--���� �� �߰�
select sysdate, add_months(sysdate,-2) from dual;
--ceil �ø� floor ����  mod ������ power ����
select ceil(-4,2), floor(-4,2), mod(8,3), power(2,10) from dual;
select * from employees;
select emp_name||to_char(hire_date,'yyyy')||'��'||to_char(hire_date,'mm')||'��'||to_char(hire_date,'dd')||'��'||to_char(hire_date,' day') from employees; 

select emp_name||to_char(hire_date,'yyyy'"��" 'mm'"��" 'dd'"��" 'day') from employees;

--�����, �ڸ��� 9�ڸ������ 0���� ǥ��
--salary*1400�տ� ��ȭǥ�ÿ� ��ǥ �־ ���
select to_char(employee_id,'000000000') from employees;
select to_char(salary*1400,'L999,999,999') from employees;

--�ڽ��� ���ϰ� �ڽ��� ������ ���� ���� ��������¥
--2010 10 10
select '2010-10-10', last_day('2010-10-10') from dual;
select '2010-10-10',trunc(to_date('2010-10-10'),'month') from dual;

select * from member;

desc member;
--DDL(data definition language)column �߰�
--commit, rollback ����
alter table member add (gender varchar2(6) default 'Female' not null);
select * from member;
update member set gender = 'male';

--�÷� ���� : commit, rollback ����
alter table member drop column phone;
--�÷� ���� : �̸�, Ÿ��, ���氡��
alter table member rename column name to stu_name;
desc member;

--Ÿ�Ժ���
alter table member modify(stu_name varchar2(50));
--������ �����Ͱ� �����Ϸ��� ũ�⺸�� ���� ���� ����
update member set stu_name='ȫ';
alter table member modify (stu_name varchar2(3));
--varchar2->number�� �����Ͱ� ���ִ� ���� �Ұ���
--�÷��� Ÿ���� �����Ϸ��� �ȿ� �ִ� �÷� �����Ͱ� ������̰ų� null�� �� ����
alter table member modify (stu_name number(4));
alter table member modify(stu_name number(100));

desc member;

select * from member;

commit;