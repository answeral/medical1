select * from stu_score;

select a.*,b.name from board a, member b
where a.id = b.id;

select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile
from board a, member b
where a.id = b.id ;

select * from stu_score; 
select num, name, total, avg,
case 
when avg >= 90 then  'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score ;

--alter table stu_score rename column num to no;

select round(avg(salary),-2) from employees;

select * from employees;
select * from departments;

select employee_id, emp_name, salary, (salary+(salary*nvl(commission_pct,0))),
to_char(salary*1410,'L999,999,999') from employees;


select department_id,round(avg(salary),2), max(salary), min(salary) from employees
where department_id is not null
group by department_id
order by department_id
;
select * from stu_score
order by no;

--홍이라고 검색하면 홍에 관련된 학생이 모두 출력되도록
select * from stu_score
where name like '%홍%';

select * from stu_score;

select * from stu_score
where avg >= 60
order by no
;

--equi join / 다른 테이블이 같은 컬럼을 가지고 있을 때
--사원번호, 사원명, 부서번호, 부서명을 출력하시오
select employee_id, emp_name, a.department_id, department_name
from employees a,departments b
where a.department_id = b.department_id and emp_name like '_a%'
and  salary>=(select avg(salary) from employees);

--두번째 자리에 a가 들어가는 사원을 검색하시오
select emp_name from employees
where emp_name like '_a%';

--월급이 평균 이상인 사람만 검색
select salary from employees
where salary>=(select avg(salary) from employees);
select * from departments;
select * from employees;
-- jobs 직급
select * from jobs;

-- 사원명e, 사원번호e, 부서번호e, 부서명d, 직급번호e, 직급명j
select employee_id,emp_name,b.department_id,department_name, a.job_id, job_title
from employees a, departments b , jobs c
where a.department_id = b.department_id and a.job_id = c.job_id ;
-- 사원번호, 사원명, 월급, 최소 월급분, 직급, 직급 타이틀 , 최소 월급에 몇 %이상을 받고 있는지...?
--최소 월급의 몇 % 이상 받고 있는지 출력 (최소월급 / 현재월급) *100

select employee_id, emp_name, salary, min_salary, max_salary, job_title, j.job_id , to_char(round((((salary-min_salary)/salary)*100),2))||'%' up
from employees a, jobs j
where a.job_id = j.job_id;

select job_id, job_title from jobs;


