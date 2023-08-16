-- 7/26
-- Q1. 각 직위별로 총 월급을 출력하되 월급이 낮은 순으로 출력하라.
use my_emp;
select * from emp;

select job, sum(sal) 
from emp 
group by job 
order by sum(sal);

-- Q2. 직위별 월급을 출력하되, 직위가 MANAGER인 사원들은 제외하라. 
    -- 그리고 그 총 월급이 5000 보다 큰 직위와 총 월급만 출력하라
select job, sum(sal) 
from emp 
where job != 'MANAGER' 
group by job 
having sum(sal) > 5000;	#집계 함수 조건 문.

--  Q3. 직위별 최대월급을 출력하되, 직위가 CLERK인 사원들은 제외하라. 
     -- 그리고 그 최대월급이 2000이상인 직위와 최대직급을 최대 월급이 높은 순으로 정렬하여 출력하라.
select job, max(sal) 
from emp 
where job != 'CLERK' 
group by job 
having max(sal) >= 2000 
order by max(sal) desc;

-- Q4. 부서별 총 월급을 구하되 30번 부서를 제외하고 그 총월급이 8000 이상인 부서만 나오게 하고 
-- 총월급이 높은 순으로 출력하라.
select deptno, sum(sal) 
from emp 
where deptno != 30 
group by deptno 
having sum(sal) >= 8000 
order by 2 desc;

-- Q5. 부서별 평균월급을 구하되 커미션이 책정된 사원만 가져오고, 
 -- 그 평균월급이 1000달러 이상인 부서만 나오게 하고 , 평균월급이 높은 순으로 출력하라.
select deptno, avg(sal) 
from emp 
where comm is not null 
group by deptno 
having avg(sal) >= 1000 
order by 2 desc;

-- 문자열 관련 함수  
SELECT 
    CONCAT('Hello', ' ', 'World'), #문자열 결합 concat(ename,':',empno)
    UPPER('hello'), #전체 대문자
    LOWER('WORLD'), #전체 소문자
    LENGTH('Hello, World!'), #전체 문자열 길이 리턴
    SUBSTRING('Hello, World!', 1, 5),	#지정된 숫자만큼 잘라서 리턴
    LEFT('Hello, World!', 5),	#왼쪽에서 5개
    RIGHT('Hello, World!', 6),	#오른쪽에서 6개
    TRIM('   Hello, World!   '), # 공백제거
    REPLACE('Hello, World!', 'World', 'Universe'), #1번째 문자열에서 타겟 문자열을 universe로 대체
    LOCATE('World', 'Hello, World!');# world가 어디에 있나. 그 위치.

select SUBSTRING('Hello, World!' from -10 for 2);
#사원테이블에서 사원의 이름 중 첫글자만 대문자로 나머지는 소문자로
select * from emp;
select concat(substring(ename,1,1), lower(substring(ename,2))) as 사원이름 from emp;

#사원이름 : 사번 : 입사일 출력
select concat(ename,':',empno,':',hiredate)
from emp;

select concat_ws(':',ename,empno,hiredate)
from emp;

--  숫자 관련 함수 
SELECT 
    ABS(-15) , #절대값 
    CEILING(3.7) , #지정된 숫자보다 크거나 같은 가장 가까운 정수로 반올림
    FLOOR(7.2) , #지정된 숫자보다 작거나 같은 가장 가까운 정수로 내림.
    ROUND(5.67) , #가장 가까운 정수로 반올림
    SQRT(16) ,	#제곱근
    POWER(2, 3) , #거듭제곱
    MOD(10, 3) ,#나눗셈 나머지 리턴	
    RAND() ,#0~1사이의 부동소숫점 반환
    SIN(45) ,#라디언으로 지정된 각도의 사인 값을 리턴
    COS(60) ;#라디언으로 지정된 각도의 코사인 값을 리턴

SELECT 
    EXP(2),	#지수값 리턴
    LOG(10),#숫자의 자연로그(밑 e)를 리턴
    LOG10(100),#숫자의 e가 10인 로크
    PI(),   #파이 리턴
    TAN(45),#라디언 지정된 각도의 탄젠트 값을 리턴
    ACOS(0.5),#함수 arcc를 리턴
    ASIN(0.7),#호를 리턴
    ATAN(1);#아크 탄젠트를 리턴		[sinh(), cosh() -> 하이퍼볼릭 함수		mysql에 없음]

 #하이퍼볼릭 쌍곡선 : 쌍곡선 삼각법, 변과 변 사이의 관계도를 설명
 #tanh : 기울기와 관련이 있다.
 #sinh(x) = (e^x - e^(-x)) / 2
 #cosh(x) = (e^x + e^(-x)) / 2
 #tanh(x) = sinh(x) / cosh(x) = (e^x - e^(-x)) / (e^x + e^(-x))

#기울기란? 선 또는 곡선의 가파른 정도. 
#	한 변수가 다른 변수와 관련하여 변경되는 비율로 측정.
#	기울기는 수직(y) 좌표의 변화를 선 또는 곡선의 두 점 사이의 수평(x) 좌표의 변화로 나눈 값.
# 	slope = (y2-y1)/(x2-x1)
#	기울기가 양수이면 선이 왼쪽에서 오른쪽으로 상승한다.(오름차순)
#	기울기가 음수이면 선이 왼쪽에서 오른쪽으로 떨어진다.(내림차순)
#	기울기가 0이면 수평선을 나타내고 기울이가 정의되지 않으면 수직선을 나타낸다.

#	곡선의 경우 기울기는 일정하지 않으면 곡선의 여러 지점에서 다를 수 있다.
#	이런 경우 기울기에 대한 개념은 변수에 대한 곡선의 도함수로 표시되는 순간 변화율로 확장된다.

-- --------------------------------------------------------------
-- 서브 쿼리
-- Q1. 'Jones'의 월급보다 많은 월급을 받는 사원의 이름과 월급을 출력하자.
#step01. : 'Jones'의 월급
select sal
from emp
where ename = 'JONES';	#2975
#step02. 많은 월급을 받는 사원의 이름과 월급을 출력
select ename, sal
from emp
where sal > 2975;

#서브쿼리 변환 메인쿼리가 서브쿼리를 참조한다. => 서브쿼리 - 메인쿼리 순서로 실행
select ename, sal
from emp
where sal > (select sal
			 from emp
			 where ename = 'JONES');
-- 1. Single Row Subquery : 서브쿼리의 결과가 한 개의 row를 리턴할 경우
	-- > , < , >= , <= , != , <> 같은 단일 값 비교 연산자 이용

-- 2. Multi Row Subquery : 서브쿼리의 결과가 여러 개의 row를 리턴할 경우
	-- in, not, not in, >any, <any, >all, <all

-- Q1) 직업이 'salesman'인 사원들과 같은 월급을 / 받는 사원의 이름과 월급
select ename, sal 
from emp
where sal in (select sal 
			 from emp
			 where job = 'SALESMAN');
#아래와 같은 결과값             
select ename, sal 
from emp
where sal in (1600, 1250, 1250, 1500); # data or data or null,,,,

-- primary indexing 된 애들은 single row. 그렇지 않은 애들은 multi row.
-- Q2) 부서번호가 10번인 사원들과 같은 월급을 받는 사원의 이름과 월급
select ename, sal 
from emp
where sal in (select sal from emp
			  where deptno = 10);
# where안에 변수 = 서브쿼리 안 select-list

-- Q3) 직업이 clerk 인 사원과 같은 부서에서 근무하는 사원의 이름과 월급, 부서 출력
select ename, sal, deptno from emp
where deptno in (select deptno from emp
				 where job = 'CLERK');
select deptno from emp
where job = 'CLERK'
                 
/* Q3) 시카고에서 근무하는 사원들과 같은 부서에서 근무하는 사원의 이름과 월급*/

select ename, sal 
from emp
where deptno in (select deptno from dept
				 where LOC = 'CHICAGO');
                 
select ename, sal
from emp
where deptno in (select deptno from DEPT
				where LOC = 'CHICAGO');
                
select ename, sal 
from emp
where deptno in (select deptno from dept
				 where LOC = 'CHICAGO');

/*
 ANY	(DATA OR DATA OR... NULL)
 = ANY 	 하나라도 만족하는 값이 있으면 결과를 리턴하며 IN과 동일함
 > ANY 	 값들 중 최소값 보다 크면 결과를 리턴
 >= ANY 	 값들 중 최소값 보다 크거나 같으면 결과를 리턴
 < ANY 	 값들 중 최대값 보다 작으면 결과를 리턴
 <= ANY 	 값들 중 최대값 보다 작거나 같으면 결과를 리턴
 <> ANY 	 모든 값들 중 다른 값만 리턴 ,값이 하나일 때만 가능함

ALL		(DATA AND DATA AND DATA....NULL)
 > ALL 	 값들 중 최대값 보다 크면 결과를 리턴
 >= ALL 	 값들 중 최대값 보다 크거나 같으면 결과를 리턴
 < ALL 	 값들 중 최소값 보다 작으면 결과를 리턴
 <= ALL 	 값들 중 최소값 보다 작거나 같으면 결과를 리턴
 = ALL 	 모든 값들과 같아야 결과를 리턴, 값이 하나일 때만 가능함
 <> ALL 	 모든 값들과 다르면 결과를 리턴
 */

-- 서브쿼리, 조인으로도 나옴 = self join 테이블에서 null 처리 구문 때문에 나옴
-- Q5) 부하 직원이 있는 사원의 사원번호와 이름을 출력 <나의 사원번호가 mgr이면 된다.>
select empno, ename from emp
where empno in (select mgr from emp); # DATA OR DATO OR .... NULL 	=ANY

select empno, ename from emp
where empno =any (select mgr from emp);

select empno, ename from emp
where mgr =any (select empno from emp); #상사가 있는 직원의 이름과 사번.

-- Q6) 부하 직원이 없는 사원의 사원번호와 이름을 출력
select empno, ename from emp
where empno not in (select ifnull(mgr,0) from emp);	#not in : DATA AND DATA AND... NULL  =? !=ALL과 같음.
select mgr from emp;	#중간에 null이 있음

-- Q7) 직속상관(mgr)이 King인 사원의 이름과 월급을 출력
-- mgr = 사원번호 = king
select ename, sal from emp
where mgr = (select empno from emp
			 where ename = 'KING');

-- Q8) 20번 부서의 사원 중 가장 많은 월급을 받는 사원들보다 더 많은 월급ㅇ르 받는 사원들의 이름과 월급을 출력하라.
-- ALL 연산자 변형
select ename, sal from emp
where sal > (select max(sal) from emp
			 where deptno = 20);

#서브쿼리
select sal from emp where deptno = 20;

select ename, sal from emp
where sal >all (select sal from emp
				where deptno = 20);

-- Q9) 20번 부서의 사원 중 가장 적은 월급을 ㅇ받는 사원들 보다 더 많은 월급ㅇ르 받는 사원들의 이름과 월급출력
select ename, sal
from emp
where sal > (select min(sal) from emp
				where deptno=20);
                
select sal from emp where deptno=20;

select ename, sal
from emp
where sal >any (select sal from emp
				where deptno=20);

###############################################################
use my_emp;
-- Q11) 직업이 SALESMAN인 사원 중 가장 많은 월급을 받는 사원보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력. (MIN(), MAX() 사용하지말고 연산자만 사용)
select ename, sal from emp
where SAL >all (select sal from emp
				where job = 'SALESMAN');
-- Q12) 직업이 SALESMAN인 사원 중 가장 적은 월급을 받는 사원보다 더 적은 월급을 받는 사원들의 이름과 월급을 출력. (MIN(), MAX() 사용하지말고 연산자만 사용)
select ename, sal from emp
where sal <all (select sal from emp
				where job = 'SALESMAN');

# multi row
-- Q1) 직업이 SALESMAN인 사원과 같은 부서에서 근무하고 
-- 		같은 월급을 받는 사원들의 이름, 월급, 부서번호 출력
select ename, sal, deptno from emp
where deptno in (select deptno from emp where job = 'SALESMAN')
and sal in (select sal from emp where job = 'SALESMAN');

-- Q2) 30번 부서 사원들과 같은 월급과 같은 커미션을 받는 사원들의 이름,월급,커미션을 출력
select ename, sal, comm from emp
where sal in (select sal from emp where deptno = 30)
and comm in (select comm from emp where deptno = 30);

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


####################################지현님 풀이#############################################
-- 1.  emp_no 10007을 사용하여 직원의 채용 날짜 이전에 채용된 직원의 직원 번호와 채용 날짜를 출력하자
 SELECT emp_no, hire_date
FROM employees
WHERE hire_date < (SELECT hire_date FROM employees WHERE emp_no = 10007);
-- 2  급여테이블의  평균 급여보다  급여가 높은 직원의 이름과 성을 출력하자.
select avg(salary) from salaries; #63810.7448
select first_name, last_name from employees
where emp_no >all (select avg(salary) from salaries);
-- 3 . emp_no가 10006인 직원과 동일한 성별을 가진 모든 직원의 emp_no 및 성별을 출력하자.
SELECT emp_no, gender
FROM employees
WHERE gender = (SELECT gender FROM employees WHERE emp_no = 10006);
-- 4. emp_no가 10003인 직원과 동일한 생년월일을 공유하는 모든 직원의 emp_no 및 birth_date를 출력하자
SELECT emp_no, birth_date
FROM employees
WHERE birth_date = (SELECT birth_date FROM employees WHERE emp_no = 10003);
-- 5. emp_no 10002 직원의 고용 날짜 이후에 고용된 모든 직원의 이름first_name과 고용 날짜를 출력하자.
SELECT first_name, hire_date
FROM employees
WHERE hire_date > (SELECT hire_date FROM employees WHERE emp_no = 10002);
-- 6.'Smith'라는 성을 가진 직원이 현재 고용되어 있는 모든 부서의 dept_no 및 dept_name을 출력 하자
SELECT dept_no, dept_name
FROM departments
WHERE dept_no IN (
    SELECT dept_no
    FROM dept_emp
    WHERE emp_no IN (
        SELECT emp_no
        FROM employees
        WHERE last_name = 'Smith'
    )
);
-- 7. dept_no가 'd002'인 부서와 같은 모든 직원의 emp_no 및 last_name을 출력하자
SELECT emp_no, last_name
FROM employees
WHERE emp_no IN (
    SELECT emp_no
    FROM dept_emp
    WHERE dept_no = 'd002'
);
-- 8.'Salaries' 테이블에서 가장 높은 월급을 받는 직원의 이름first_name을 출력하자.
SELECT first_name
FROM employees
WHERE emp_no = (
    SELECT emp_no
    FROM salaries
    ORDER BY salary DESC
    LIMIT 1
);
-- 9. 성이 'Johnson'인 직원이 근무하는 부서 번호와 부서이름을 출력하자.
SELECT dept_no, dept_name
FROM departments
WHERE dept_no = (SELECT dept_no FROM employees WHERE first_name = 'Johnson');
-- 10.  emp_no 10015와 같은 날에 고용된 직원의 성과 이름을 출력하자.
SELECT last_name, first_name, hire_date
FROM employees
WHERE hire_date = (SELECT hire_date FROM employees WHERE emp_no = 10015);
