
drop database employees;
CREATE DATABASE employees;
USE employees;
show tables;
select * from employees;

-- 부서
select * from departments;
-- 사원의 부서
select * from dept_emp;
-- 부서 매니저
select * from dept_manager;
-- 사원
select * from employees;
-- 사원 월급
select * from salaries;
-- 사원 직업
select * from titles;

-- 1.  emp_no 10007을 사용하여 직원의 채용 날짜 이전에 채용된 직원의 직원 번호와 채용 날짜를 출력하자 
select emp_no,hire_date from employees where emp_no = 10007; #1989-02-10

select emp_no, hire_date from employees
where hire_date <any(select hire_date from employees
					  where emp_no=10007);
 
-- 2  급여테이블의  평균 급여보다  급여가 높은 직원의 이름과 성을 출력하자.  
select avg(salary) from salaries; #63810.7448

select first_name, last_name from employees
where emp_no >all (select avg(salary) from salaries);

-- 3 . emp_no가 10006인 직원과 동일한 성별을 가진 모든 직원의 emp_no 및 성별을 출력하자.  
select gender from employees where emp_no = 10006; #F

select emp_no, gender from employees
where gender = (select gender from employees where emp_no = 10006);

-- 4. emp_no가 10003인 직원과 동일한 생년월일을 공유하는 모든 직원의 emp_no 및 birth_date를 출력하자 
select emp_no, birth_date from employees where emp_no = 10003;	#1959-12-03

select emp_no, birth_date from employees
where birth_date = (select birth_date from employees where emp_no = 10003);

-- 5. emp_no 10002 직원의 고용 날짜 이후에 고용된 모든 직원의 이름first_name과 고용 날짜를 출력하자. 
select emp_no, hire_date from employees where emp_no = 10002;	#1985-11-21

select first_name, hire_date from employees
where hire_date >all (select hire_date from employees where emp_no = 10002);

-- 6.'Smith'라는 성을 가진 직원이 현재 고용되어 있는 모든 부서의 dept_no 및 dept_name을 출력 하자 ***
select * from employees where last_name = 'Smith';

select dept_no, dept_name from departments
where dept_no in (select dept_no from dept_emp
				  where emp_no in (select emp_no from employees where last_name = 'Smith'));

-- 7. dept_no가 'd002'인 부서와 같은 모든 직원의 emp_no 및 last_name을 출력하자 
select emp_no, last_name from employees
where emp_no in (select emp_no from dept_emp
				 where dept_no = 'd002');

-- 8.'Salaries' 테이블에서 가장 높은 월급을 받는 직원의 이름first_name을 출력하자.***
select max(salary) from salaries;#158220
select emp_no from salaries where salary = 158220;
select first_name from employees where emp_no = 43624;

select first_name from employees
where emp_no =any (select emp_no from salaries
					where salary =(select max(salary) from salaries));

-- 9. 성이 'Johnson'인 직원이 근무하는 부서 번호와 부서이름을 출력하자. ***
select last_name,emp_no from employees where last_name = 'Johnson';

select dept_no, dept_name from departments
where dept_no in (select dept_no from dept_emp 
				  where emp_no in (select emp_no from employees
								   where last_name = 'Johnson'));
                                   
-- 10.  emp_no 10015와 같은 날에 고용된 직원의 성과 이름을 출력하자.  
select first_name, last_name, hire_date from employees where emp_no = 10015;#1987-07-02

select first_name, last_name from employees
where hire_date in (select hire_date from employees where emp_no = 10015);

