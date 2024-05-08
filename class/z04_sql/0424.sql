--trunc: 버림 round:반올림 
select sysdate,hire_date, trunc(sysdate-hire_date,2) from employee;

-- 어제 날짜 sysdate-1, 내일 날짜 sysdate+1
select sysdate-1 어제, sysdate 오늘 ,sysdate+1 내일 ,sysdate+100 from dual;
--m_no -시퀀스 1-9999 1씩 증가, 5번 반복해서 저장
--yesterday,m_no m_today, m_tomorrow, m_year 날짜 컬럼을 가진 테이블 m_date 만들기
--어제, 오늘, 내일 1년 후 날짜를 저장하기
create sequence seq_m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;
--테이블 생성 date, timestamp
--drop table m_date;

create table m_date(
m_no number(4),
m_yesterday date,
m_today date,
m_tomorrow date,
m_year date
);
insert into m_date(m_no, m_yesterday, m_today, m_tomorrow, m_year) values
(seq_m_no.nextval, sysdate-1, sysdate, sysdate+1, sysdate+365);
select * from m_date;
--abs 절대값, ceil 올림  floor 버림 round 자리수 지정 반올림, trunc- 자리수 지정 버림
select abs(hire_date-sysdate) from employees;
--날짜의 월을 기준으로 반올림
select hire_date, round(hire_date,'month') from employees;

--날짜의 월을 기준으로 버림
select hire_date, trunc(hire_date,'month'),round(hire_date,'month') from employees;

select trunc(hire_date,'month') 기준일 ,hire_date from employees
order by hire_date ;

select * from channels;

select period,count(period) from kor_loan_status
group by period
order by period;

select period from kor_loan_status
where period='201111';

select trunc(kor,-1) t_kor, count(trunc(kor,-1)) from students
group by trunc(kor,-1)
order by t_kor;

--날짜의 '월'기준으로 버림
select trunc(hire_date,'month'),count(trunc(hire_date, 'month'))from employees
group by trunc(hire_date,'month')
order by m_hire date;

--drop table stu_score;
--drop table emp01;
--drop table board;

select * from stu_score
order by num;

update stu_score set name='관순스'
where num=10;

update stu_score set avg=round(total/3);

--2개의 날짜에서 월 간격을 확인
select hire_date,floor(months_between(sysdate,hire_date)),trunc(sysdate-hire_date,2) from employees;

--개월 추가
select hire_date, add_months(hire_date,6) from employees;

--last day
select hire_date,last_day(hire_date),round(hire_date,'d') from employees;
--일주일 기준으로 반올림, 현재는 12시가 안넘어서 24/04/21 넘으면 24/04/27
select sysdate, round(sysdate,'d') from employees;
--날짜를 기준으로 현재일, 처음일, 마지막일
select sysdate 현재일, trunc(sysdate,'month') 처음일,last_day(sysdate) 마지막일 from dual;

--특정 요일의 날짜 확인
select sysdate, next_day(sysdate,'토요일')from dual;

--요일의 처음일, 다음 '요일'
select sysdate, trunc(sysdate,'d'), next_day(sysdate, '토요일') from dual;

--board 테이블 default는 입력이 없을 시 지정한 데이터 자동 입력됨
create table board(
bno number(4) primary key, --중복이 안됨, null허용하지 않음. 기본키로 사용됨.
id varchar2(30),
btitle varchar2(1000),
bcontent clob, --varchar2(3000)까지 사용가능, crob은 무제한, varchar2의 타입
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'aaa','제목입니다.','내용입니다.',sysdate,0,board_seq.currval,0,0,'1.jpg'
);
insert into board(board,id,btitle,bcontent,bgroup,bfile) values(
board_seq.nextval,'bbb','이벤트 신청','이벤트를 신청합니다.',board_seq.currval,'2.jpg'
);

select * from board;

--형변환, number, character, date 세 개가 서로 형변환 가능 (1->일, 가->는 안됨.)
select sysdate from dual;
select sysdate, to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'yy/mm/dd') from dual;
select to_char(sysdate,'yyyy') from dual;

--문자열은 +가 안됨 // ko+2024+0001
select 'ko'||to_char(sysdate,'yyyy')||to_char(seq_mno.nextval,'0000') from dual;

select to_char(sysdate, 'dy'),to_char(sysdate,'day') from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon day') from dual;

--hire_date, yyyy-mm-dd hh:mi:ss mon day
select hire_date, to_char(hire_date, 'yyyy-mm-dd hh:mi:ss mon day') from employees; 
-- am,pm 오전,오후 hh24는 24시간으로 표시
select to_char(sysdate,'am hh24:mi:ss') from dual;

select* from stu_score;
select to_char(create_date,'yyyy/mm/dd hh24:mi:ss day') from stu_score
order by create_date;

--날짜별로 몇개의 데이터가 들어가 있는지 출력하기
select create_date,count(create_date) from stu_score
group by create_date
order by create_date;

-- 문자형 사칙연산(+,-,*,/) 불가능, 자리수 표시, 쉼표표시, 날짜형태 표시 가능 
-- 숫자형 사칙연산, 컬럼별 사칙연산 가능, 자리수 표시, 쉼표 표시 불가능
-- 날짜형 +,- 연산기능 가능,months_between 2개 날짜 달 계산, 날짜 유형을 지정해서 출력이 안됨.

-- 문자형 안에 있는 데이터가 숫자이면 자동으로 형변환해서 계산해줌.
-- 문자형 안에 문자가 있으면 자동형변환 불가능
--가능
select 10 a, 100 b, (10+100) ab,to_char(100),10 + '100' from dual;
--불가능
select 10 a, 100 b, (10+100) ab,to_char(100),10 + '100원' from dual;

select 12340000,to_char(12340000),to_char(12340000,'999,999,999') from dual;
--'0000' 빈자리는 0으로 채움, '9999'는 빈자리를 그냥 둠.
select length(12340000),to_char(12340000), length(to_char(12340000,'999,999,999')) from dual;
select length(to_char(12340000,'999,999,999')) from dual;
-- L은 원화 표시
select 12340000,to_char(12340000,'L999,999') from dual;
--$는 $ 표시
select 12340000,to_char(12340000,'$999,999') from dual;
--소수점 자리 표시
select 1234.1234, to_char(1234.1234,'000,999.99') from dual;
--10개자리수 표시
-- 공백제거해서 자리수 확인 trim
select length(trim(to_char(12345,'0000000000'))),length(trim(to_char(12345,'999,999'))) from dual;

--123,456,789  100,000
--123,456,789 +100,000 값을 출력하시오. 천단위 표시할 것
select 123456789+100000 from dual;

-- 123,456,789 쉼표를 제거 ->replace('123,456,789,',','')
-- 타입을 number로 바꾸기
-- 더하기를 함.
-- 문자형 타입으로 변경해서 원화,쉼표 표시
-- total = '123,456,789'
-- wire = '100,000'
select (123,456,789)+(100,000) from dual;
select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')), 'L999,999,999'  )
from dual;

select to_number('0000123') from dual; -- 123만 나타남
select to_char('0000123') from dual; --0000123으로 나타남

--데이터 길이 함수
select length('안녕하세요') from dual;
select length(12340000) from dual;

--날짜형
--문자형
select '2024-04-24'-'2024-04-23' from dual;
select to_date('2024-04-24')-to_date('2024-04-01 ') from dual;
select to_date('24-04-24')-to_date('24-04-01 ') from dual;

select to_date('20240404') from dual;
-- 2024-04-01 타입으로 변경해서 출력하라
select to_char(to_date('20240401'),'yyyy-mm-dd hh:mi:ss') from dual;

select hire_date from employees
where hire_date >= '20080101';

select * from stu_score;

select create_date from stu_score
where create_date = '2024/04/15';

select sysdate-hire_date from employees;
select sysdate-to_date('2024/04/01') from dual;

--20,000 -10,000 해서 10,000을 출력
--1.number로 형변환
select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'99,999') from dual;
-- 실제 월급 = 월급+ (월급*커미션) 출력
select commission_pct, salary from employees;
select * from employees;
--nvl(데이터,0)
select salary,salary+(nvl(commission_pct,0)*salary)),commission_pct from employees;
--commission_pct null값만 출력
select commission_pct from employees
where commission_pct is null;


select manager_id from employees
order by manager_id desc;

--manager_id null이면 0이라고 입력 nvl(데이터,0)
select nvl(manager_id,0) from employees;

--maneger_id null->ceo number타입을 문자로 변경해야함
select nvl(to_char(manager_id),'ceo')from employees;
