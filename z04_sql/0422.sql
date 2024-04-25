select * from employees;

select employee_id, emp_name from employees;

select salary from employees;

--Ÿ�� : number�� �� +,-,*,/����
select salary, salary*1400 k_sal, salary*1400*12 as y_sal from employees;

select * from stu_score;

select no,name, kor, eng, math, total, avg, rank from stu_score;

--���̽� 

select department_id from employees;

select nvl(department_id,0) from employees;

--��Ī as,  "":Ű���带 �ִ� �׷��� ���
select salary, salary +(salary* nvl(commission_pct,0)) as "Real_sal" from employees;

select salary as ���� from employees;

select * from departments;

--�μ��̸�, �μ���ȣ�� ���
select department_id, department_name from departments;

--�������� �����͸� 1���� ���ļ� �Ѱܾ� �� ��� concat
--ȫ�浿, ������, �̼���, �豸, ������, �豸 ->�и� :split(",") 

select * from stu_score;

select kor||','||eng||','||math stu from stu_score;

select kor+ eng+ math as total,(kor+eng+math)/3 from stu_score;

--�ߺ����� : distinct
--where : ������ not �����ϰ� �����Ϸ��� is not null
select distinct department_id from employees where department_id is not null;

--manager_id
select manager_id from employees;
select distinct manager_id from employees where manager_id is not null;

select * from employees;
select employee_id,salary from employees
where employee_id =200 or employee_id =201 or employee_id =202;

--201<=employee_id < 205�� �Ұ��� and ����� ��
select * from employees
where employee_id >=200 and employee_id <=206;

select * from employees
where employee_id <=150 or employee_id >= 200;

select employee_id,department_id from employees
where department_id =10 or department_id =30 or department_id = 50;

--���� 6000 �̻� 9000����
--����: order by �÷� asc:��������, desc:��������
select employee_id, salary from employees
where salary>=6000 and salary <=9000
order by salary asc;

--���� 6000,7000,8000�� ����� ����Ͻÿ�
select employee_id, salary from employees
where salary =6000 or salary=7000 or salary = 8000;

--�μ���ȣ�� 50�̸鼭 ������ 8000�̻��� ��� ���
select department_id,salary from employees
where department_id =50 and salary>=8000;

--stu_score���� ȫ�浿 ���
select * from stu_score
where name = 'ȫ�浿';

--��������
select hire_date from employees
order by hire_date asc;

--��������
select hire_date from employees
order by hire_date desc;

select emp_name,hire_date from employees
where hire_date <='02/01/01'
order by hire_date asc;

select hire_date,hire_date+100 from employees;

--�ݿø�:round
select round(sysdate-hire_date) from employees;
--���� ��ġ��: + ������ �Ұ���, concat : || ���
select emp_name || email from employees;

--�Ի����� 05�� �̻� 06�� �����̸鼭 ������ 6000�޷� �̻��� ����� ���� ���
select emp_name,hire_date,salary from employees
where hire_date>='05/01/01' and hire_date <= '06/12/31' and salary>=6000
order by hire_date desc;

--!=, <>, not, ^=
select department_id from employees
where department_id != 10 and not department_id =50
order by department_id asc;

--5000�̻� 9000����
select emp_name,salary from employees
where salary >=5000 and salary <=9000
order by salary asc;

--��� 99�̻��� ��� �˻�
select name,avg from stu_score
where avg>=99
order by avg desc;

select * from students;

update students set name='������'
where no=10;

select * from students;
commit;

--students���� ��� 80�̻�, ��� 85���̻��� �л� ���
select * from students
where kor>=70 and avg >=75;

--�������� 80��, ���� 70, ���� 90�� �� �л��� ���
select name, kor from students
where kor=70 or kor =80 or kor =90;

update students set kor =100
where no = 1;
rollback;
select * from students
where no =1;
--����
update students set kor=100,total = 100+ eng+ math,avg = (100+eng+math)/3
where no=1;

--���������� 70~90 �̻� �л��� ����Ͻÿ�
select name, kor from students
where kor > 70 and kor <= 90;
--100��
select * from students;
--between a and b : a �� b ����, a���� ũ�ų� ����, b���� �۰ų� ���� �� �˻�
--27��
select kor from students
where kor between 80 and 90;

--70���� �۰� 90���� ū��
--73�� not between a and b: a���� �۰ų�, b���� ū �� �˻�
select kor from students
where kor not between 70 and 90;

--��¥�� between a and b
select hire_date from employees
order by hire_date asc;

--���ڰ� 99�⺸�� ũ�ų� ����, 01�⺸�� �۰ų� ���� ��
select hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date asc; 

--in ������ : ������ �ʵ尡 �������� �� �߿� �ϳ��� �˻��� ���
--not in : �����ϰ�
select name, kor from students
where kor not in(80,70,90);

--�̸��˻�
select * from students
where name = 'ȫ�浿';

--like �˻� : Ư���ܾ ���ԵǾ� �ִ� ���� �˻�
--%ȫ: ȫ���� ������ �ܾ�, ȫ%:ȫ���� �����ϴ� ��, %��%:���ԵǾ� �ִ� �ܾ�
select * from students
where name like '%��';

-- _ : �� ĭ ������ ���, �� �տ� 1���� �� �����鼭 ���� ���ԵǾ� �ִ� �ܾ� �˻�
select * from students
where name like '_��%';

--�� ��° ���ڿ� t�� �� �ִ� �̸� ã��
select * from students
where name like'__t%';

--�̸��� 4�ڸ��� 3��°�� r�� �� �̸� �˻�
select * from students
where name like '__r_';
--�̸����̰� 4�ڸ��̰�, 3��°�� r�� �� �̸� �˻�
select * from students
where name like'__r%'
and length (name) = 4;

--�̸� ���̰� 4�ڸ�
select name from students
where length(name) = 4;

--�̸��� �빮�� A�� ���۵Ǵ� �� �˻�
select no,name from students
where name like 'A%';

--�̸��� a�� �� �ִ� �л� �˻�
select no,name from students
where name like '%a';

--��ҹ��� ���о��� a�� �� �ִ� �л� �˻�
--�ҹ��� ġȯ lower().�빮�� ġȯ upper(), ù���� �빮�� initcap()
select no,name from students
where lower(name) like '%a%';
--a�� ���ԵǾ� ���� ���� �̸� �˻�
select no,name from students
where lower(name) not like '%a%';

select employee_id, manager_id from employees
where manager_id =100;

select employee_id, emp_name, manager_id from employees
where manager_id = null;

select employee_id, emp_name, manager_id from employees
where manager_id is null;

select employee_id, emp_name, manager_id from employees
where manager_id is not null;

select * from stu_score;

--�ѱ۵� �������� ����
select * from stu_score
order by name asc;

--1�� ���������� �������� �� ����, ���� ������ ���, ���������� �������� ����
select * from students
order by kor desc, eng asc;

select * from students
order by total desc;

--�÷� �߰�
alter table students add rank number(3);

--�÷� Ÿ��
desc students;

select * from students;

update students set rank = 0;

commit;

-- ���
select no,rank() over(order by total desc) as rank from students
;
update students s1 set rank = (select ranks
from (select no no2, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no2 )
;
select * from students;

--����
update students set rank =13
where no=1;

select * from students;

update students s1 set rank = 13
where no =1;

--select * from(���̺�);
select * from (select * from students
where avg >= 70);