use my_emp;
-- schema : 외부 내부 구조 확인
show tables;
-- 스키마 이동
use world; 
-- 데이터 베이스 생성과 삭제
drop database my_test; 
create database my_test;
use my_test;

-- 데이터베이스 생성, 테이브 생성, 데이터 추가, DDL
create database multi;
use multi;

-- 테이블 생성
-- create table username(
-- column명 데이터타입(사이즈) ,,,,);
create table students(
	id int,
    name varchar(100),
    phone char(13),
    address varchar(1000)
);
-- 테이블 구조를 확인
desc students;
-- 테이블 레코드 확인 -> select 컬럼,,, from 테이블명
-- 테이블의 전체 레코드 확인 
SELECT * FROM STUDENTS;

-- INSERT INTO 테이블명('컬럼명' 을 주면 거기에 맞춰서 values를 줌) values(,,,);
INSERT INTO STUDENTS VALUES(1,'홍길동','010-1111-1111','서울시');
-- 컬럼 추가 
alter table students
add subjects varchar(200);
select * from students;

-- 컬럼 수정 : 추가된 subjects의 컬럼을 100으로 수정해서 desc로 확인해보자
alter table students modify subjects varchar(100);
desc students;
-- 컬럼 수정 : subjects의 칼럼을 삭제해보자.
alter table students drop subjects;
desc students;

-- 테이블 삭제, 데이터베이스 삭제, 데이터베이스 전체 확인
drop table students;
drop database multi;
show databases;

-- -------------------------------

use my_emp;
show tables;
desc emp;
desc dept;

-- 사원 테이블
select * from emp;
-- SMITH의 사원번호 7369, SMITH의 상사(MANAGER):7902 = FORD, FORD의 상사 = JONES => 자기가 자기 스스로를 참조(SELF JOIN)
-- EMPNO : 사원의 번호이면서, 상사의 번호이다.

-- 부서 테이블
select * from dept;
-- SMITH가 근무하는 지역은 DALLAS, 부서 이름은 RESEARCH (DEPTNO)
-- 두 개의 ENTITY가 RELATION관계
-- COMMISSION을 받는 사람은 총 4명. 0도 받는 걸로 생각한다.
-- 명령은 대소문자를 가리지만 value는 대소문자를 가린다.


DESC EMP;

USE MY_EMP
-- Q1) 오늘의 날짜를 출력해보자.
SELECT NOW();
-- SELECT 100 + 200;

-- Q2) 사원테이블의 전체 목록을 출력
SELECT * FROM EMP;
-- Q2) 부서 테이블의 전체 내용을 출력
SELECT * FROM DEPT;
-- Q4) 사원테이블에서 사원의 이름,봉급,커미션을 출력하자.
SELECT ename, sal, comm FROM EMP;
-- Q5) 사원테이블에서 사원의 이름, 입사일, 부서번호출력alter
SELECT ENAME,HIREDATE,DEPTNO FROM EMP;
-- Q6) 사원테이블에서 사원의 이름, 봉급, 상사 출력
SELECT ENAME,SAL,MGR FROM EMP;
-- Q7) 사원의 이름, 봉급, 근무지역 출력
SELECT ENAME, SAL, LOC FROM EMP, DEPT;

-- 테이블의 별칭
-- Q8) 사원의 이름, 봉급, 근무지역 출력
SELECT E.ENAME, E.SAL, D.LOC FROM EMP E, DEPT D;
-- 테이블의 객체
-- Q9) 사원의 이름, 봉급, 근무지역 출력
SELECT EMP.ENAME, EMP.SAL, DEPT.LOC FROM EMP, DEPT;

-- Q10) 부서테이블에서 부서번호, 근무지역을 출력
SELECT DEPTNO, LOC FROM DEPT;
-- Q11) 사원의 이름, 봉급, 부서번호, 근무지역 출력
-- 테이블 별칭을 반드시 명시!! 왜냐면 양쪽 다 있거든요 DEPTNO가..
SELECT ENAME, SAL, DEPT.DEPTNO, LOC FROM EMP, DEPT;

-- Q12) 컬럼명 별칭 AS, "" 명시
-- 사원이름 봉급 매니저로 출력하자.
-- CASE01. 공백으로 별칭 구분
SELECT ENAME 사원이름, SAL 봉급, MGR 매니저 FROM EMP;

-- 사원이름 봉급 매니저로 출력하자.
-- CASE02. AS로 별칭 구분(MS사에서.. ORACLE은 AS 안줘도 됨.)
SELECT ENAME AS 사원이름, SAL AS 봉급, MGR AS 매니저 FROM EMP;

-- 사원 이름 봉급 매니저로 출력하자.
-- CASE03. " "으로 별칭 구분 -- MYSQL에서는 보통 '', ORACLE ""
SELECT ENAME AS "사 원 이 름", SAL AS "봉 급", MGR AS "매 니 저" FROM EMP;
-- ORACLE은 오류남, ORACLE은 VALUE만 SINGLE. MYSQL은 ''해도 됨.
SELECT ENAME "사 원 이 름", SAL "봉 급", MGR '매 니 저' FROM EMP;

SELECT ENAME, SAL, 부서.DNAME FROM EMP, DEPT AS 부서; -- MYSQL만 TABLE에 별칭 시 AS 줄 수 있다.
SELECT ENAME, SAL, 부서.DNAME FROM EMP, DEPT 부서; 
-- SELECT ENAME, SAL, 부서.DNAME FROM EMP, DEPT "부 서"; -- " " 안됨!

/*
	SELECT 컬럼리스트,,, --- 여기만 * 가능
    FROM 테이블명,,,
    WHERE 조건문, 숫자비교, 문자비교, 대소문자비교, NULL 비교, 날짜값 비교
    HAVING   GROUP BY 연산
    GROUP BY  집계연산 _SUM, MAX, MIN, AVG, VAT(분산), COUNT,, 윈도우함수,분석함수, 기타함수
    ORDER BY 정렬, 서브쿼리;
*/

-- Q13) 사원의 이름, 매니저 출력
SELECT ENAME AS "사원님", MGR AS '매 니 저' FROM EMP;

-- Q14) 사원의 이름과 연봉을 출력해보자
SELECT ENAME, SAL*12 AS '연 봉' FROM EMP;

-- Q15) 사원의 이름과 급여를 출력하되, 급여 = 봉급 + 커미션
-- 커미션이 NULL인 애들은 연산이 안된다.
SELECT ENAME, SAL+COMM AS '급 여' FROM EMP; 
-- NULL을 0으로 변환 후 연산, IFNULL(컬럼, 대체할 값) : MYSQL // NVL(컬럼, 대체할 값) : ORACLE
SELECT ENAME, SAL+IFNULL(COMM,0) FROM EMP;
SELECT ENAME, SAL+IFNULL(COMM,'값없음') FROM EMP; -- '값없음'을 0으로 생각하고 통과시킴

-- Q16) 커미션이 책정되지 않은 사원의 커미션을 300으로 지정한 후 
-- 사원의 이름, 봉급, 커미션을 출력
SELECT ENAME, SAL, IFNULL(COMM,300) FROM EMP;

SELECT ENAME, SAL, IFNULL(COMM,SAL) FROM EMP;
SELECT ENAME, SAL, IFNULL(COMM,NULL) FROM EMP;
-- SELECT ENAME, SAL, IFNULL(COMM,) FROM EMP; -- PARAMETER COUNT 오류// ,만 줘도 안됨
SELECT ENAME, SAL, IFNULL(COMM,"~") FROM EMP;

-- << SELECT, FROM 절 뒤에 별칭, NULL 연산처리(산술 연산)>> --

-- Q17) 급여 = 봉급 + 커미션 - 세금 , 세금 = 봉금의 15%
-- 사원의 이름, 봉급, 커미션, 세금, 급여
SELECT ENAME "사원의 이름", SAL 봉급, 
		COMM 커미션,
        SAL*0.15 세금,
        SAL+IFNULL(COMM,0)-(SAL*0.15) 급여  
FROM EMP;

-- Q18) 중복 값 제거 후 직업을 출력해보자
SELECT DISTINCT JOB FROM EMP; -- GROUPING했다고 생각함. 
SELECT DISTINCT DEPTNO FROM EMP;

/*
비교연산 > >= < <= = != 
SELECT-->3
FROM -->1
WHERE-->2 결과가 TRUE
*/

-- Q1) 사원의 봉급이 1000 이상인 사원의 이름과 봉급을 출력
SELECT ENAME, SAL FROM EMP WHERE SAL >= 1000;

-- Q2) 부서번호가 10번인 사원의 이름과 부서번호를 출력
SELECT ENAME, DEPTNO FROM EMP WHERE DEPTNO=10;

-- Q3) 부서번호가 10번이고 월급이 1000 이상인 사원의 이름과 부서번호,월급
SELECT ENAME, DEPTNO, SAL FROM EMP WHERE DEPTNO=10 AND SAL >= 1000;

-- Q4) 부서번호가 10, 20인 사원의 이름과 부서번호 출력
SELECT ENAME, DEPTNO FROM EMP WHERE DEPTNO=10 OR DEPTNO=20;
SELECT ENAME, DEPTNO FROM EMP WHERE DEPTNO IN (10,20);

-- Q5) 사원의 입사년도가 80년 이후 사원의 이름과 입사년도 출력
SELECT ENAME, HIREDATE FROM EMP WHERE HIREDATE >='1980/01/01';
SELECT ENAME, HIREDATE FROM EMP WHERE HIREDATE >='1980-01-01';
SELECT ENAME, HIREDATE FROM EMP WHERE HIREDATE >='80-01-01';
SELECT ENAME, HIREDATE FROM EMP WHERE HIREDATE >='80/01/01';

/*
	문자열 비교 LIKE %[모든]  _[한 글자]
	'ABCD' LIKE 'A%' => A로 시작하는 모든 글자를 찾아라 => ABCD
*/
-- Q1) 사원테이블에서 사원의 이름이 A로 시작하는 사원의 이름을 출력
SELECT ENAME FROM EMP WHERE ENAME LIKE 'A%';
-- Q2) 사원테이블에서 사원의 이름이 T가 2개 들어간 사원의 이름을 출력
SELECT ENAME FROM EMP WHERE ENAME LIKE '%T%T%' ;
-- Q3) 사원테이블에서 사원의 이름이 L가 2개 들어간 사원의 이름을 출력
SELECT ENAME FROM EMP WHERE ENAME LIKE '%L%L%' ;
-- Q4) 사원테이블에서 사원의 이름이 S로 끝나는 사원의 이름을 출력
SELECT ENAME FROM EMP WHERE ENAME LIKE '%S' ;
-- Q5) 사원테이블에서 사원의 이름이 T로 끝나는 사원의 이름을 출력
SELECT ENAME FROM EMP WHERE ENAME LIKE '%T' ;
-- Q6) 사원이름 중 두번쨰 M인 사원의 이름을 출력하자.
SELECT ENAME FROM EMP WHERE ENAME LIKE '_M%' ;
-- Q7) 사원이름 중 세번쨰 R인 사원의 이름을 출력하자.
SELECT ENAME FROM EMP WHERE ENAME LIKE '__R%' ; -- '%\%%' : 문자열에 %가 들어간 경우 

/*
	SELECT 컬럼리스트,,, --- 여기만 * 가능
    FROM 테이블명,,,
    WHERE 조건문, 숫자비교, 문자비교, 대소문자비교, NULL 비교, 날짜값 비교
    ORDER BY {col_name | expr | position}
		[ASC | DESC], ... => ASC : 오름차순/ DESC : 내림차순
*/
-- Q1) 사원의 이름을 오름차순으로 출력해보자
SELECT ENAME FROM EMP ORDER BY 1 ASC;
SELECT ENAME FROM EMP ORDER BY ENAME;
-- Q1) 사원의 이름을 내림차순으로 출력해보자
SELECT ENAME FROM EMP ORDER BY 1 DESC;
SELECT ENAME FROM EMP ORDER BY ENAME DESC;
-- Q3) 사원테이블에서 사원의 이름은 오름차순으로 봉급은 내림차순으로해라. -> 말이 이상하지만..
SELECT ENAME, SAL FROM EMP order by ENAME, SAL DESC;
SELECT ENAME, SAL FROM EMP order by 1 ASC, 2 DESC;
SELECT ENAME, SAL FROM EMP order by 1, SAL DESC;
SELECT ENAME, SAL FROM EMP order by 1, 2 DESC;
-- SELECT ENAME, SAL FROM EMP order by ENAME, 1 DESC; -- 오류는 안나지만 틀린문장. 

-- 사원의 이름은 내림차순
SELECT ENAME, SAL FROM EMP ORDER BY ENAME DESC, SAL;

/*
	집계 함수 : NULL은 처리 안됨 
    <>,!= : NOT EQUAL
    %,MOD :
    expr BETWEEN min AND max :
    expr IN (value,...) :
    IN NOT : 
    IS NOT NULL:
    IS NULL : 
    LIKE : 
    ... SQL 페이지 가서 찾아보기
*/
-- Q1) 봉급을 집계함수를 통해서 출력해보자.
SELECT SUM(SAL), AVG(SAL), MAX(SAL), MIN(SAL), STD(SAL) FROM EMP;
-- Q2) COUNT(*) : COUNT는 * 가능
SELECT COUNT(ENAME), COUNT(*), COUNT(COMM), COUNT(IFNULL(COMM,0)) FROM EMP; -- * 가장 긴 COLUMN을 대상으로 함
-- Q3) COUNT() 함수만 NULL 연산하지 않는다. / 
-- 프로그램은 기본적으로 집계함수(윈도우 내장함수) , 집계함수는 기본적으로(산술연산함수) NULL값을 허용하지 않는다.
SELECT SUM(COMM), SUM(IFNULL(COMM,0)) FROM EMP;
SELECT AVG(COMM), AVG(IFNULL(COMM,0)) FROM EMP; -- SUM/COUNT. COUNT는 NULL을 처리하지 않음.. 그걸 생각해라.
SELECT MAX(COMM), MAX(IFNULL(COMM,0)) FROM EMP;
SELECT MIN(COMM), MIN(IFNULL(COMM,0)) FROM EMP;

-- 집계를 적용해서 구문을 활용해보자
-- Q1) 사원테이블에서 부서번호가 10번인 평균월급을 구하자
SELECT AVG(SAL) FROM EMP WHERE DEPTNO=10;
-- Q2) 사원테이블에서 부서번호가 10, 20번인 사원의 평균 월급을 구하자
SELECT AVG(SAL) FROM EMP WHERE DEPTNO IN (10,20); -- DATA OR DATA OR NULL OR,,,

-- -------------------------
USE EMPLOYEES;
SHOW TABLES;
SELECT * FROM DEPT_EMP;
SELECT * FROM TITLES;
-- -------------------------
-- DAY22 7/25

USE MY_EMP;
-- Q1) 사원테이블에서 직업이 SALESMAN인 사원의 평균 월급을 구해보자
SELECT AVG(SAL) FROM EMP WHERE JOB = 'SALESMAN'; -- 대소문자를 구분해줘야함(SALESMAN)



select * from emp;
select * from dept;
