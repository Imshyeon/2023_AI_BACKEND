use my_emp;
-- CRUD를 할 수 있는 TEST 테이블을 생성하자
-- MYEMP, MYDEPT 이름으로 EMP, DEPT 테이블의 구조와 데이터로 생성하자.
CREATE TABLE MYEMP AS SELECT * FROM EMP; #제약조건 없이 가져옴
CREATE TABLE MYDEPT AS SELECT * FROM DEPT; 

SELECT * FROM MYEMP;
SELECT * FROM MYDEPT;

-- INSERT INTO table_name(,,,) VALUES(,,,);
-- UPDATE table_name SET = value,,,,
-- DELETE FROM table_name or WHERE conditional;
SET SQL_SAFE_UPDATES = 0; #오류 1175
-- Q1) 사원 테이블에 사원번호가 7499사원의 월급을 5000으로 변경하자. ***
UPDATE MYEMP SET SAL = 5000
WHERE EMPNO = 7499;
COMMIT; 

-- Q2) 부서번호가 20번인 사원의 월급을 2000으로 변경해보자.
UPDATE MYEMP SET SAL = 2000
WHERE DEPTNO=20;

-- Q3) 부서테이블에서 데이터를 입력해보자, 50,RESEARCH,BOSTON
INSERT INTO MYDEPT VALUES (50,'RESEARCH','BOSTON');

-- Q4) 방금 전 입력한 내용을 삭제해보자
DELETE FROM MYDEPT WHERE DEPTNO = 50;

-- Q5) FORD의 월급을 4000으로 변경하고 부서번호도 30으로 변경해보자
UPDATE MYEMP SET SAL=4000, DEPTNO=30
WHERE ENAME = 'FORD';

-- Q6) 사원번호가 7698인 사원의 부서번호(30)를 7934사원의 부서번호(10)로 변경하자.
-- 시험용 
UPDATE MYEMP SET DEPTNO = (SELECT DEPTNO FROM MYEMP WHERE EMPNO=7934) #FROM MYEMP 해버리면 스스로 참조할수없다고 함. BUT 이건 MYSQL만 이렇다...
WHERE EMPNO = 7698;
-- MYSQL용(시험에 FROM EMP 이렇게 나오면 틀림.) : 원본을 백업해놓고 참조 또는 수정하거나, VIEW 해라.
UPDATE MYEMP SET DEPTNO = (SELECT DEPTNO FROM EMP WHERE EMPNO=7934) #FROM MYEMP 해버리면 스스로 참조할수없다고 함. BUT 이건 MYSQL만 이렇다...
WHERE EMPNO = 7698;

-- Q7) 아래 데이터를 추가하자.
INSERT INTO MYEMP VALUES(0001,'홍길동','CLERK',7783,NOW(),9000,NULL,10);
INSERT INTO MYEMP VALUES(0001,'홍길동','CLERK',7784,NOW(),9000,NULL,10);
INSERT INTO MYEMP VALUES(0001,'홍길동','CLERK',7785,NOW(),9000,NULL,10);

-- Q7-1) 사원번호가 1이고 매니저가 7785인 사원을 삭제하자
DELETE FROM MYEMP WHERE EMPNO = 1 AND MGR = 7785;
-- Q1-2) 사원번호가 1이고 매니저가 7784의 월급을 8888을 변경하자
UPDATE MYEMP SET SAL = 8888
WHERE EMPNO = 1 AND MGR = 7784;
-- Q7-3) 사원테이블의 내용을 전체 삭제하자.
DELETE FROM MYEMP;

-- Q8) 서브쿼리를 사용해보자.
-- 테이블을 삭제하자 MYEMP;
DROP TABLE MYEMP;
DROP TABLE MY_EMP;
DESC MYEMP; #오류 : 없어!
CREATE TABLE MY_EMP AS SELECT * FROM EMP;
SELECT COUNT(*) FROM MY_EMP; #14개 온다.

-- Q8-1) WARD와 같은 직업ㅇ르 가진 사원을 모두 삭제하자.
-- 서브쿼리를 사용해서 수정, 삭제를 할 경우 가상의 테이블을 생성해서 참조시킨다.
DELETE FROM MY_EMP WHERE JOB = (SELECT M_NEW.JOB FROM (SELECT JOB FROM MY_EMP WHERE ENAME='WARD')
												 M_NEW);
SELECT  ROW_COUNT() AS DeletedRows FROM MY_EMP;
SELECT COUNT(*) FROM MY_EMP;
-- Q8-2) WARD월급을 SMITH의 월급과 같게 지정하자.
UPDATE MY_EMP SET SAL = (SELECT M_NEW.SAL FROM(SELECT SAL FROM MY_EMP WHERE ENAME= 'SMITH') M_NEW)
WHERE ENAME = 'WARD';
-- Q8-3) ALLEN의 직업을 WARD와 같게 수정하자.
UPDATE MY_EMP SET JOB = (SELECT M_NEW.JOB FROM (SELECT JOB FROM MY_EMP WHERE ENAME='WARD') M_NEW)
WHERE ENAME = 'ALLEN'; 
-- Q8-4) 사원번호 7499번인 사원과 같은 직업ㅇ르 가진 사원들의 입사일을 오늘 날짜로 변경하자.
UPDATE MY_EMP SET HIREDATE=NOW()
WHERE JOB = (SELECT MY.JOB FROM(SELECT JOB FROM MY_EMP WHERE EMPNO=7499) MY);


SELECT * FROM MY_EMP;
ROLLBACK;	#INSERT DELETE UPDATE가 취소, COMMIT을 해버리면 ROLLBACK이 안됨
COMMIT;		#저장
SELECT * FROM MYDEPT;

-- Q9. 트랜잭션을 연동해보자. ROLLBACK, COMMIT => cmd로 보자!
SET autocommit = false;
START TRANSACTION; # ROLLBACK, COMMIT을 명시 명령어로 시작하겠다. => COMMIT을 줘야 저장
	SELECT COUNT(*) FROM MY_EMP;
    
	-- DELETE하고 COUNT() -> COMMIT하고 COUNT() -> 
    DELETE FROM MY_EMP WHERE DEPTNO=10;
    SELECT COUNT(*) FROM MY_EMP;
    COMMIT;#원본 업데이트 ->  cmd에서 count가 11로 보임
    
SET autocommit = false;
START TRANSACTION;

DELETE FROM MY_EMP WHERE DEPTNO=20; #5개 삭제
SELECT COUNT(*) FROM MY_EMP;
ROLLBACK; #데이터 되돌아옴
DELETE FROM MY_EMP WHERE DEPTNO=30;	#6개 삭제
COMMIT;	#나머지 데이터 5개로 저장
SELECT * FROM MY_EMP;


/*
start transaction; 
update table set column1 ='v1' where id =1 ;

#완벽한 ROLLBACK 아닌 분할..
SAVEPOINT savepoint1;
update table set column1 ='v2' where id =2 ;
ROLLBACK TO SAVEPOINT savepoint1;	==> update table set column1 ='v2' where id =2 ; 취소

update table set column1 ='v3' where id =3 ;

COMMIT;



1. START TRANSACTION: 새로운 트랜잭션을 시작
2. COMMIT: 트랜잭션 중에 변경된 사항을 영구저장
3. ROLLBACK: 트랜잭션 중에 변경된 사항을 취소하고 
          데이터베이스를 트랜잭션이 시작되기 전 상태로 되돌림
4. SAVEPOINT: 트랜잭션 내에서 저장점을 설정하여 나중에 해당 특정 지점으로 롤백
*/
# rollback : 명령을 실행하게 되면 현재 트랜잭션변경사항을 실행 취고하고
# 데이터베이스가 트랜잭션 [시작 전 상태]로 돌아감.
DELETE FROM MY_EMP;




