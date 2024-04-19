--가지고 있는 테이블 검색
select * from tab;
--f5는 전체 실행, f9는 부분만 실행
--f5로 부분만 실행 하고 싶을 때는 드래그해서 진행
--웬만하면 f9사용
select * from employees;

-- 테이블 구조확인
desc employees;

--데이터형 :number(총자리수, 소수)

--table 생성
 --avg number(5,2) 총 다섯자리, 2자리는 소수부분
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

--데이터형 : date(세기,년,월,일,시,분,초,요일),timestamp(밀리세컨드까지 존재)
--dual 가상 테이블

--24/04/18 날짜 기본형태
select sysdate from dual;

--2024-04-18 날짜 포맷 형태 : to_char 형변환 -> 포맷을 지정
select to_char(sysdate,'yyyy-mm-dd') from dual;

--2024-04-18 01:07:57
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

--01:09:20
select to_char(sysdate,'hh:mi:ss') from dual;

select sysdate+1000 from dual;

select sysdate - to_date('24/01/01') from dual;




