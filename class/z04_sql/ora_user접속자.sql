--������ �ִ� ���̺� �˻�
select * from tab;
--f5�� ��ü ����, f9�� �κи� ����
--f5�� �κи� ���� �ϰ� ���� ���� �巡���ؼ� ����
--�����ϸ� f9���
select * from employees;

-- ���̺� ����Ȯ��
desc employees;

--�������� :number(���ڸ���, �Ҽ�)

--table ����
 --avg number(5,2) �� �ټ��ڸ�, 2�ڸ��� �Ҽ��κ�
create table stu_score (
    no number(2),
    kor number(3),
    eng number(3),
    avg number(5,2)
);

insert into stu_score(no,kor, eng, avg) values(
1,100,99,(100+99)/2);

insert into stu_score values(
1,95,98,(95+98)/2);

insert into stu_score values(
1,80,70.223,(80+70.223)/2) ;

select * from stu_score;

commit;


create table num (
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);

--�������� : date(����,��,��,��,��,��,��,����),timestamp(�и���������� ����)
--dual ���� ���̺�

--24/04/18 ��¥ �⺻����
select sysdate from dual;

--2024-04-18 ��¥ ���� ���� : to_char ����ȯ -> ������ ����
select to_char(sysdate,'yyyy-mm-dd') from dual;

--2024-04-18 01:07:57
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

--01:09:20
select to_char(sysdate,'hh:mi:ss') from dual;

select sysdate+1000 from dual;

select sysdate - to_date('24/01/01') from dual;




