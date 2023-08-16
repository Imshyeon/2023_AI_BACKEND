USE MY_EMP;

/*---------- 조인 ---------*/
-- 테이블의 컬럼간에 공통 값(VALUE)추출하는 것   
--  USING(공통컬럼)    ON(컬럼명이 다를때  )
--  INNER JOIN = JOIN : 같은 값만 추출  / FALSE , NULL은 추출되지 않는다.  
 
--  OUTTER JOIN : 주종관계   / 주테이블은 전체를 출력 하고 종테이블이 같은 값만 출력 
               -- LEFT OUTER JOIN  / RIGHT OUTER JOIN 
               
--  CROSS JOIN   : 비교 컬럼이 속한 모든테이블을 출력

-- Q1) INNER JOIN을 이용해서 사원의 이름과 사원이 속해있는 부서이름을 출력
-- Ansi
select * from emp;
select ename, dname
from emp inner join dept using(deptno);

select ename, dname
from emp join dept using(deptno);

-- MYSQL
select ename, dname
from emp, dept
where emp.deptno=dept.deptno;

-- Q2) 전체 컬럼을 리턴 1번을..
select * from emp join dept using(deptno); #deptno를 기점으로 합집합

select * from emp,dept; #곱을 해버림 14*4 => cross join // row 단위로 교차

-- Q3) 간단한 테이블을 생성해서 조인을 연습해보자.
CREATE TABLE X(
X1 VARCHAR(5),
X2 VARCHAR(5));

CREATE TABLE Y(
Y1 VARCHAR(5),
Y2 VARCHAR(5));

DESC X;
DESC Y;

insert into x values('A','D');
insert into y values('A','1');
insert into y values('B','2');
insert into y values('C','3');
insert into y values(NULL,'1');

select * from x;
select * from y;

-- X,Y 조인을 해보자				 <리턴되는 레코드 확인, 각 컬럼명이 다를 때는 각 일치되는 데이터만 리턴.>
select * from x join y on x1=y1; #1 row// x1과 y1은 컬럼명이 다르기 때문에 합쳐지지 않음.
								 #같은 값만 추출  / FALSE , NULL은 추출되지 않는다.

/*
	X1  X2  Y1  Y2
	A   D   A   1
            B   2
            C   3
		  NULL  1
=> OUTER TABLE : 주테이블은 전체를 출력 하고 종테이블이 같은 값만 출력
*/

-- Q4) 주종관게 조인을 구현해보자
SELECT * FROM X RIGHT OUTER JOIN Y	#Y: 주테이블 / X: 종테이블
ON X1=Y1;

SELECT * FROM X LEFT OUTER JOIN Y	#X: 주테이블 / Y: 종테이블
ON X1=Y1;

-- Q5) RIGHT OUTER JOIN+LEFT OUTER JOIN = FULL OUTER JOIN 만들자
SELECT * FROM X FULL JOIN Y ON X1 = Y1; #MYSQL은 FULL OUTER JOIN 인식 못함

-- Q6) 급여등급에 해당하는 테이블을 생성하자.
CREATE TABLE SALGRADE(
    GRADE  INT , 
    LOSAL   INT,
    HISAL   INT
);

insert into salgrade values (1, 700, 1200);
insert into salgrade values (2, 1201, 1400);
insert into salgrade values (3, 1401, 2000);
insert into salgrade values (4, 2001, 3000);
insert into salgrade values (5, 3001, 9999);

select * from salgrade;
select * from emp;
-- Q6) NON-EQUI JOIN
-- 각 사원의 이름과 월급 그리고 그 사원의 급여등급을 출력해보자
select ename, sal, salgrade.grade from emp join salgrade on(sal between losal and hisal);
select ename, sal, grade from emp, salgrade where sal between losal and hisal;

-- Q7) 각 사원의 이름과 월급, 급여등급, 부서이름 출력
-- 테이블 제약 조건이 있는 것이 선, 나머지는 후 조인
select ename, sal, grade , dname from emp join dept using(deptno)
									 join salgrade on(sal between losal and hisal);
									
select ename, sal, grade, dname from emp, dept, salgrade where emp.deptno = emp.deptno and sal between losal and hisal;                                    
                                     
select * from emp join dept using(deptno) join salgrade on(sal between losal and hisal);

-- Q8) SELF JOIN : 테이블 하나에 같은 값을 가진 컬럼을 조인하는 것
-- 테이블에 별칭을 부여한 후 조인
-- 사원의 번호와 이름, 관리자의 번호와 이름을 출력해보자. emp 사원, emp 관리자
select 사원.empno as 사원번호, 사원.ename as 사원이름, 관리자.empno as 관리자번호, 관리자.ename as 관리자이름 
from emp 사원 left outer join emp 관리자 on(사원.mgr=관리자.empno);

-- select 사원.empno as 사원번호, 사원.ename as 사원이름, 관리자.empno as 관리자번호, 관리자.ename as 관리자이름

select * from dept;
select * from emp;

##########
-- 1. 사원의 이름, 부서번호, 부서이름 출력
-- ansi
select ename, deptno, dname from emp left outer join dept using(deptno);
-- mysql
select ename, dept.deptno, dname from emp, dept where emp.deptno = dept.deptno;

-- 2. dallas에서 근무하는 사원의 이름, 직위, 부서번호, 부서이름 출력
-- ansi
select ename, job, deptno, dname from emp left outer join dept using(deptno)
where loc = 'DALLAS';
-- mysql
select ename, job, dept.deptno, dname from emp, dept 
where emp.deptno = dept.deptno and dept.loc = 'DALLAS';

-- 3. 이름에 'A'가 들어있는 사원의 이름과 부서이름 출력
-- ansi
select ename, dname from emp join dept using(deptno)
where ename like '%A%';
-- mysql
select ename, dname from emp, dept 
where emp.deptno = dept.deptno and ename like '%A%';

-- 4. 사원이름과 그 사원이 속한 부서의 부서명, 그리고 월급을 
-- 출력하는데 월급이 3000이상인 사원을 출력하라.
-- ansi
select ename, dname, sal from emp join dept using(deptno) where sal >=3000;
-- mysql
select ename, dname, sal from emp,dept where emp.deptno= dept.deptno and sal >=3000;

-- 5. 직위가 'SALESMAN'인 사원들의 직위와 그 사원이름, 그리고
-- 그 사원이 속한 부서 이름을 출력하라.
-- ansi
select ename, job, dname from emp join dept using(deptno)
where job = 'SALESMAN';
-- mysql
select ename, job, dname from emp, dept
where emp.deptno= dept.deptno and job = 'SALESMAN';

-- 6. 커미션이 책정된 사원들의 사원번호, 이름, 연봉, 연봉+커미션,
-- 급여등급을 출력하되, 각각의 컬럼명을 '사원번호', '사원이름',
-- '연봉','실급여', '급여등급'으로 하여 출력하라.
-- ansi
select  empno 사원번호, ename 사원이름, sal*12 as 연봉, (sal+comm)*12 as 실급여, grade 등급
from emp join salgrade on (sal between losal and hisal)
where comm is not null;
-- mysql
select  empno 사원번호, ename 사원이름, sal*12 as 연봉, (sal+comm)*12 as 실급여, grade 등급
from emp, salgrade
where (sal between losal and hisal) and comm is not null;

-- 7. 부서번호가 10번인 사원들의 부서번호, 부서이름, 사원이름,
-- 월급, 급여등급을 출력하라.
 -- ansi
 select deptno, dname, ename, sal, grade from emp 
	join dept using(deptno)
	join salgrade on (sal between losal and hisal)
 where deptno = 10;
-- mysql
 select dept.deptno, dept.dname, ename, sal, grade from emp, dept, salgrade
 where emp.detpno = dept.deptno and (sal between losal and hisal) and dept.deptno = 10;

-- 8. 부서번호가 10번, 20번인 사원들의 부서번호, 부서이름, 
-- 사원이름, 월급, 급여등급을 출력하라. 그리고 그 출력된 
-- 결과물을 부서번호가 낮은 순으로, 월급이 높은 순으로 
-- 정렬하라.
-- ansi
select deptno,dname,ename,sal,grade from emp 
	join dept using(deptno)
	join salgrade on (sal between losal and hisal)
	where deptno in (10,20) order by deptno, sal desc;


-- 10 -자신의 관리자보다 먼저 입사한 모든 사원의 이름 및 입사일을 해당
 -- 관리자의 이름 및입사일과 함게 표시하고 열 이름을 각각 
-- EMPLOYEE,EMPHIREDATE,MANAGER,MGRHIREDATE로 저장한다.
-- ansi
select E.ename as EMPLOYEE, E.hiredate as EMPHIREDATE, M.ename as MANAGER, M.hiredate as MGRHIREDATE
from emp E join emp M on (E.mgr = M.empno)
where M.hiredate > E.hiredate;


-- 11 해당 부서의 모든 사원에 대한 부서 이름, 위치, 사원 수 및 평균 급여를
 -- 표시하는 정의를 작성한다. 
-- 열 이름을 각각 DNAME,LOC,NUMBER OF PEOPLE,SALARY로 한다.
select * from dept;

select dname, loc, count(empno) as 'NUMBER OF PEOPLE', round(avg(sal),1) as SALARY
from emp e right outer join dept d on e.deptno = d.deptno
group by dname, loc;

select dname, loc, count(empno) as 'NUMBER OF PEOPLE', round(avg(sal),1) as SALARY
from emp right outer join dept using(deptno)
group by dname, loc;

-- 12. 해당 부서 직원의 평균 봉급보다 많은 봉급를 받는 모든 직원의 이름, 부서 이름 및 직업을 출력 해보자. ***
select ename, dname, job from emp
inner join dept using(deptno)
where sal > (select avg(sal) from emp where deptno = emp.deptno);	#EX. DEPTNO = 10
#inner join = join

 -- 13. 급여가 해당 부서의 최대 봉급의 10% 이내인 모든 사원의 사원 이름과 봉급를 출력 해보자.
select ename, sal
from emp
join dept using(deptno)
where sal >= (select max(sal)*0.9 from emp where deptno = emp.deptno)
 and sal <= (select max(sal) from emp where deptno= emp.deptno);




explain	#쿼리 실행 계획
select ename, dname, job from emp
inner join dept using(deptno)
where sal > (select avg(sal) from emp where deptno = emp.deptno);

/*
EXPLAIN	#쿼리 실행 계획 // 데이터 처리의 기본단위는 block이다.

Extra
Using where; Using join buffer(flat, BNL join)  ==> 기본. BNL : Block Nested Loop

Extra
Using where; Using join buffer(hash join) ==> hash 알고리즘을 사용해서 join을 했다. 
											  대용량 데이터 테이블 조인 시 사용. 최적화프로그램에서 hash join 하고있다.
*/

/*
1. CROSS JOIN: 
두 테이블의 데카르트 곱, 즉 두 테이블의 가능한 모든 행이 반환(조인 조건이 필요하지 않다.)
SELECT * FROM table1 CROSS JOIN table2;
SELECT * FROM table1, table2;

2. INNER JOIN:
조인 조건에 따라 두 테이블에서 (조인 조건 : 일치하는 값이 있는 행만) 반환 -> USING(칼럼명 같을 때), ON(칼럼명 다를 때) 사용
SELECT * FROM table1 INNER JOIN table2 ON condition;

3. OUTER JOIN
3-1) LEFT JOIN(또는 LEFT OUTER JOIN):
조인 조건에 따라 왼쪽 테이블의 모든 행과 오른쪽 테이블의 일치하는 행을 반환
오른쪽 테이블에서 일치하는 항목이 없으면 오른쪽 테이블의 열에 대해 NULL 값이 반환
SELECT * FROM table1 LEFT JOIN table2 ON condition;

3-2) RIGHT JOIN(또는 RIGHT OUTER JOIN):
조인 조건에 따라 오른쪽 테이블의 모든 행과 왼쪽 테이블의 일치하는 행을 반환
왼쪽 테이블에서 일치하는 항목이 없으면 왼쪽 테이블의 열에 대해 NULL 값이 반환
SELECT * FROM table1 RIGHT JOIN table2 ON condition;

3-3) FULL JOIN(또는 FULL OUTER JOIN):
왼쪽 테이블 또는 오른쪽 테이블에 해당 항목이 있는 경우 모든 행을 반환
일치하는 항목이 정확하지 않은 테이블의 열에 대해 NULL 값이 반환
SELECT * FROM table1 FULL JOIN table2 ON condition;

4.SELE JOIN:
관련 열을 기반으로 행을 결합하기 위해 테이블을 자체적으로 조인
동일한 테이블 내의 레코드를 비교할 때 사용한다.
SELECT * FROM table1 t1 INNER JOIN table1 t2 ON condition;

5. NATURAL JOIN  = JOIN = USING(column)
이름과 일치하는 모든 열을 기반으로 두 테이블을 조인
이름과 데이터 유형이 같은 열은 자동으로 일치한다. USING, ON 키워드 사용하지 않는다.
SELECT * FROM table1 NATURAL JOIN table2;

================================================
JOIN 알고리즘의 선택 기준 : 데이터, 테이블의 크기, 인덱스 및 쿼리의 특정 요구사항(리소스와 쿼리의 복잡성)
중첩루프 조인, 해시조인, 인덱스 중첩 루프, 정렬 병합조인 등등
*/






