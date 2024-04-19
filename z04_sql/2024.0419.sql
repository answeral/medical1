select * from employees;
--회원정보 테이블 생성

create table member(
--column ,varchar:문자열,사용자리개수(한글은 한글자에 3자리차지)
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

--데이터 입력 문자라서 ''넣어서 사용
insert into member(id,pw,name,phone) values(
'aaa','1111','홍길동','010-1111-1111'
);
insert into member values(
'bbb','1111','유관순','010-2222-2222'
);
insert into member(id,name,phone) values(
'ccc','이순신','010-3333-3333'
);
--컬럼 수 부족 에러
/*insert into member values(
'ddd','강감찬','010-4444-4444'
);*/
--null : 무한대값
select id,pw,name,phone from member;

commit;

rollback;
select * from member;

insert into member values(
'ddd','1111','강감찬','010-4444-4444'
);

commit;

select * from member;

update member set pw='2222' where id='ccc';

-- 모든 테이블 확인
select * from tab;

--테이블의 타입 확인
desc member;

--오라클 타입
--number-숫자, date-날짜, char-고정문자, varchar2-가변문자, clob-대용량 문자

--number : 정수, 실수
--number(4):-9999~9999 가능, 5자리 수 안됨
create table mem(
no number, -- 길이 지정하지 않음.무한대지만 21자리?
no2 number(4),
no3 number(4,2)
);

insert into mem (no) values (1234567890);

insert into mem (no2) values (9999);
insert into mem (no2) values (-9999);
insert into mem (no2) values (-99999);
insert into mem (no2) values (1.11); --1만 들어감. 소수점 자리 배정X

insert into mem (no3) values (11.11);
insert into mem (no3) values (111); --111.00 : 5자리 수

select * from mem;
commit;
create table mem2(
no number(4,2),
mdate date,
mdate2 timestamp --date : 년,월,일,시,분,초 저장 = timestamp : 밀리초까지 저장가능.
);

insert into mem2(mdate) values('2024-04-19'); --24/04/19라고 나오지만 00:00:00초로 저장
insert into mem2(mdate) values (sysdate); --sysdate:현재시간
insert into mem2(mdate2) values(sysdate);
insert into mem2(mdate,mdate2) values (sysdate,sysdate+30);


select * from mem2; 

select to_char(mdate,'yyyy/mm/dd hh:mi:ss') from mem2;
select to_char(mdate2,'yyyy/mm/dd hh:mi:ss:ff') from mem2;

select mdate,mdate2+30 from mem2; --select는 보여지는 것만

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
--char : 고정문자
insert into mem3 (tel) values ('11112222');
insert into mem3 (tel) values ('22223333');
insert into mem3 (tel) values ('111');
insert into mem3 (tel) values ('123456789');
insert into mem3 (tel) values ('홍');

--varchar2 : 가변문자
insert into mem3(name) values ('11112222');
insert into mem3(name) values ('홍길동'); --한글크기 :3
insert into mem3(name) values ('신사임당');-- 크기:12
INSERT INTO MEM3(NAME) VALUES ('AAA');
insert into mem3(name) values ('aaa');

commit;

select * from mem,mem2;

--select,from 2개의 키워드로 구성됨.
--모든 컬럼을 출력
-- 대소문자를 구분하지 않음.
select * from mem3;
SELECT * FROM MEM3;
--sql구문은 대소문자 구분없음, 데이터는 대소문자 구분됨
select name from mem3 where lower (name)='aaa'; --모두 소문자로 검색 1.AAA 2.aaa
select * from mem3 where name ='AAA'; -- AAA
select * from mem3 where name ='aaa'; -- aaa

select emp_name,department_id from employees;
--distinct : 같은 것은 1번만 출력
select distinct department_id from employees; --107개-> 12부서

select department_id, department_name from departments;
--리스트의 딕셔너리 형태로 보여줌
select * from departments; 
select * from employees;
select * from jobs;
select * from products; 
select job_id, min_salary from jobs;

select * from mem3;
select no, mdate2,name,mdate from mem3; --컬럼의 위치가 바뀌어서 나옴

select * from employees;

--사원번호, 사원이름, 급여, 입사일자
select employee_id,emp_name,salary, hire_date from employees;

desc employees; --컬럼명, 타입이 나옴

select * from stu_score;
--테이블 삭제
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
1,'홍길동',100,100,100,300,100,1
);

insert into stu_score values(
5,'김구',100,100,100,300,100,1
);

commit;

select * from stu_score;

--산술연산자 number타입인 경우만 가능

select * from stu_score;

insert into stu_score values(
6,'김유신',100,95,96,(100+95+96),(100+95+96)/3,1
);

select * from stu_score;

insert into stu_score values(
7,'홍길자',100,100,99,(100+99+100),(100+100+99)/3,1
);

--번호, 이름, 국어점수, 국어점수-20, 평균,국어-20을 한 평균
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select * from employees;
select commission_pct, salary from employees;

--salary 달러 -> 원화 환산
select employee_id, emp_name,salary from employees;
select employee_id,emp_name, salary*1381.79 from employees;

select * from employees;
--커미션, 실제 월급 =월급 +커미션
select employee_id, emp_name, (salary*12*1381.79)+(commission_pct*1381.79) from employees;

select employee_id, emp_name, salary+(salary*commission_pct) from employees;
--nvl(컬럼,0)
select employee_id, emp_name, nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;

-- 월급 *12 ->연봉
select employee_id, emp_name,(salary*12),(salary*12*1381.79),(commission_pct*1381.79) from employees;

commit;

