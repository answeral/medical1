--[1]사원정보 테이블에서
-- 사원번호, 이름, 급여, 부서, 입사일, 상사의 사원번호를 출력하라
--이름은 이름과 직급을 연결하여 name이라는 별칭으러 출력

select * from employees
;
select * from departments;

select a.employee_id, a.emp_name, a.salary, b.department_name, a.department_id, c.employee_id, c.emp_name as NAME, a.hire_date,
a.manager_id
from employees a, departments b, employees c
where a.department_id = b.department_id and a.employee_id = c.manager_id;

--[2]사원정보 테이블에서
-- 사원이 이름과 성은 NAME, 업무는 JOB, 급여는 SALARY, 연봉에 $100 보너스를 추가해서
--계산한 값은 INCRESE ANN_salary,
--급여에 $100 보너스를 추가하여 계산한 연봉은 Increase Salary라는 별칭을 붙여 출력

select emp_name as Name,job_id as Job, salary as Salary,
to_char((((salary+nvl(commission_pct,0))*12)+100),'$999,999,999') as "Increase Ann salary"
from employees;

--[3]H R 부서에서 예산 편성 문제로 급여 정보 보고서를 작성하려고 한다. 
--사원정보(Employees) 테이블에서 급여가 $7,000~$10,000 범위 이외인 사람의 이름과 성(Name으로 별칭) 및 급여를 급여가 적은 순서로 출력하시오
select emp_name Name ,to_char(salary,'$999,999,999') salary from employees
where salary<= 7000 or salary >=100000
order by salary ;

select emp_name, salary from employees
where not (salary between 7000 and 10000)
order by salary;

--[ 4 ] 사원의 성(last_name) 중에 ‘e’ 및 ‘o’ 글자가 포함된 사원을 출력하시오. 이때 머리글은 ‘e or o Name’이라고 출력하시오(8행).
select emp_name as "e or o Name" from employees
where emp_name like '%e%' or emp_name like '%E%' or emp_name like '%o%' or  emp_name like '%O%';

--소문자 대문자 모두 출력해야함
select emp_name from employees
where lower(emp_name) like '%o%' or lower(emp_name) like '%e%'
order by emp_name;

--[ 5 ] 이번 분기에 60번 IT 부서에서는 신규 프로그램을 개발하고 보급하여 회사에 공헌하였다. 
--이에 해당 부서의 사원 급여를 12.3% 인상하기로 하였다. 
--60번 IT 부서 사원의 급여를 12.3% 인상하여 정수만(반올림) 표시하는 보고서를 작성하시오. 
--보고서는 사원번호, 성과 이름(Name으로 별칭), 급여, 인상된 급여(Increase Salary로 별칭)순으로 출력하시오(5행).

select department_id,employee_id, emp_name Name, round(salary*(salary*0.123)) "Increase Salary" from employees 
where department_id =60 ;

--[ 6 ] 모든 사원의 연봉을 표시하는 보고서를 작성하려고 한다. 
--보고서에 사원의 이름과 성(Name으로 별칭), 급여, 수당여부에 따른 연봉을 포함하여 출력하시오. 
--수당여부는 수당이 있으면 “Salary + Commission”, 수당이 없으면 “Salary only”라고 표시하고, 별칭은 적절히 붙이시오. 
--또한 출력 시 연봉이 높은 순으로 정렬하시오(107행).

select emp_name Name, salary, salary+(salary*nvl(commission_pct,0)) as  Salary_Commission from employees
where commission_pct is not null
order by salary+(salary*nvl(commission_pct,0))desc;

select emp_name Name, salary, salary+(salary*nvl(commission_pct,0)) as Salary_only from employees
where commission_pct is null
order by salary+(salary*nvl(commission_pct,0))desc;

--case when then
select emp_name, salary,salary+(salary*nvl(commission_pct,0)) as comm_salary ,commission_pct ,
case when commission_pct is null then 'Salary only'
when commission_pct is not null then 'Salary Commission'
end as "commission_isNull"
from employees
order by salary desc
;

--decode : 딱 맞는 케이스만 진행
--decode(commission_pct,null,'Salary only','Salary+Commission')
--decode( salary,
--3000,'A'
--4000,'B'
--5000,'C')
--from employees
--order by salary desc

--nvl2

--nvl2(commission_pct,'Salary+Commission','Salary only')
--from employees
--order by salary desc;

--[ 7 ] 각 사원이 소속된 부서별로 급여 합계, 급여 평균, 급여 최댓값, 급여 최솟값을 집계하고자 한다. 
--계산된 출력값은 여섯 자리와 세 자리 구분기호, $ 표시와 함께 아래와 같이 출력하시오. 
--단, 부서에 소속되지 않은 사원에 대한 정보는 제외하고, 출력 시 머리글은 다음 그림처럼 별칭(alias) 처리하시오(11행).

select department_id, 
to_char(sum(salary),'$999,999,999')as Sum, 
to_char(round(avg(salary),2),'$999,999,999') as Avg, 
to_char(max(salary),'$999,999,999') MAX_SAL, 
to_char(min(salary),'$999,999,999') MIN_SAL
from employees
where department_id is not null
group by department_id;

--[ 8 ] 사원들의 업무별 전체 급여 평균이 $10,000보다 큰 경우를 조회하여 업무별 급여 평균을 출력하시오. 
--단 업무에 사원(CLERK)이 포함된 경우는 제외하고 전체 급여 평균이 높은 순서대로 출력하시오(7행).
select * from employees;

--where 일반컬럼의 조건, having 그룸 컬럼의 조건
select department_id,job_id,avg(salary) from employees
where not (job_id like '%CLERK') 
group by department_id, job_id
having avg(salary)> 10000
order by avg(salary) desc;
--[ 9 ] 각 사원과 직속 상사와의 관계를 이용하여 다음과 같은 형식의 보고서를 작성하고자 한다.
--(예) 홍길동은 허균에게 보고한다 → Eleni Zlotkey report to Steven King
--어떤 사원이 누구에게 보고하는지 위 예를 참고하여 출력하시오. 
--단, 보고할 상사가 없는 사원이 있다면 그 정보도 포함하여 출력하고, 상사의 이름과 성은 대문자로 출력하시오(107행)

select a.employee_id, a.manager_id, to_char(a.emp_name||'report'||'to'||b.emp_name)as report  
from employees a, employees b
where a.employee_id(+) = b.manager_id
;


--[ 10 ] Employees, Departments 테이블의 구조를 파악한 후 사원 수가 다섯 명 이상인 부서의 부서이름과 사원 수를 출력하시오.
--이때 사원 수가 많은 순으로 정렬하시오(5행).
select * from employees;
select * from departments;

select  b.department_name, count(*) as dep_cnt
from employees a, departments b
where a.department_id = b.department_id
group by b.department_name  
having count(*) >=5 
order by count(*) desc
;
-- [ 추가 ] HR 부서의 어떤 사원은 급여정보를 조회하는 업무를 맡고 있다.
-- Tucker가 포함된 사원보다 급여를 많이 받고 있는 사원의 이름, 업무, 급여를 출력하시오(15행).

select emp_name, salary, job_id from employees
where  salary>(select salary from employees
where emp_name like '%Tucker%');

-- [ 추가 ] 모든 사원의 소속부서 평균연봉을 계산하여 
-- 사원별로 이름, 업무, 급여, 부서번호, 부서평균연봉(Department Avg Salary로 별칭)을 출력하시오(107행).
select emp_name, job_id, salary, e.department_id,
(select round(avg(salary),2) from employees a
where a.department_id = e.department_id) 
as "Department Avg Salary"
from employees e;

-- 소속 부서 평균연봉
select round(avg(salary)) from employees
where department_id =50

;
-- 단일 컬럼 대신 select 구절을 사용 할 수 있음
--join 
select salary,a.department_id,avg_salary
from employees a, (select department_id,round(avg(salary),2) avg_salary from employees group by department_id ) b
where a.department_id = b.department_id
;
-- equi join
select salary, a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id
;

select emp_name, salary 
from (select *from employees
where salary>= (select avg(salary)
from employees))
where emp_name like '%a%';

select *
from employees
where salary>= (select avg(salary)
from employees);

create table daum_movie(
dno number,
title varchar2(100),
img varchar2(100),
audience number(10),
ddate date default sysdate
);

commit;