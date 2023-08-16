use my_emp;

SET @dbms_output_enabled := FALSE;	#cmd에서 내용을 보여주는지 아닌지를 설정하는 거임.
SELECT IF(@dbms_output_enabled, '1.HELLO WORLD.', '') AS Message;

SET @dbms_output_enabled := TRUE;
SELECT IF(@dbms_output_enabled, '2.HELLO WORLD.', '') AS Message;

####################################################
-- PROCEDURE
-- Q1. 임의의 문자열 출력을 구현하는 프로시저를 작성해보자
CALL my_test();
-- Q2. 생성된 프로시저 내용을 확인해보자.
show create procedure my_test;

-- Q3. 사칙연산을 구현하는 프로시저를 작성해보자.
CALL my_calc();

-- Q4. 사칙연산을 다음과 같이 호출해서 구현해보자.
CALL my_calc02(10,5,'+');
CALL my_calc02(10,5,'-');
CALL my_calc02(10,5,'*');
CALL my_calc02(10,5,'/');
/*
CREATE DEFINER=`root`@`localhost` PROCEDURE `my_calc02`(IN a FLOAT, IN b FLOAT, IN operator CHAR(1))
BEGIN
	DECLARE result FLOAT;
	CASE operator
		WHEN '+' THEN SET result = a+b;
        WHEN '-' THEN SET result = a-b;
        WHEN '*' THEN SET result = a*b;
        WHEN '/' THEN
			IF b <> 0 THEN
				SET result = a/b;
			ELSE
				SELECT '0으로 나눌 수 없다.' AS result;
			END IF;
		ELSE
			SELECT '알 수 없는 OPERATOR; AS result;
	END CASE;
	SELECT CONCAT('Result : ', a, operator, b, '=', result) AS output;
END
*/

-- Q5) 아래코드를 활용해서 구문을 만들어보자.
-- 부서번호가 10번인 사원의 이름과 부서 번호를 출력 하자 . 
CALL get_exam05(10);
CALL get_exam05(20);
CALL get_exam05(30);
/*
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam05`(IN dept_num INT)
BEGIN
	SELECT ENAME, DEPTNO FROM EMP WHERE DEPTNO=DEPT_NO;
END
*/

-- Q6) 아래코드를 활용해서 구문을 만들어보자.
-- 입력받은 봉급 이상인 사원의 이름과 봉급을 출력하자. 
CALL get_exam06(1000);
/*
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam06`(IN sal_in FLOAT)
BEGIN
	SELECT ENAME, SAL FROM EMP WHERE SAL >= sal_in;
END
*/

-- Q7) get_exam05부서 번호와 월급을 입력받아 해당 부서번호 및 월급 이상인 사원의 이름과 부서번호, 월급을 출력하자.
CALL get_exam07(10,1000); 
/*
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam07`(IN dept_num FLOAT, IN sal_in FLOAT)
BEGIN
	SELECT ENAME, DEPTNO, SAL FROM EMP WHERE SAL >= sal_in AND DEPTNO = dept_num;
END
*/
 
 -- Q8) 입력된 부서번호에 따른 사원의 이름과 부서번호를 출력하자. 
 CALL get_exam08(10,20); 
 /*
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam08`(IN dept_num1 FLOAT, IN dept_num2 FLOAT)
BEGIN
	SELECT ENAME, DEPTNO FROM EMP WHERE DEPTNO IN (dept_num1, dept_num2);
END
*/
 
-- Q9) 입력된 월에 입사한 사원의 이름과 입사년도 및 입사한 달, 일을 출력 해보자. 
 CALL get_exam09(2);
  /*
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam09`(IN h_month INT)
BEGIN
	SELECT ENAME, YEAR(HIREDATE) AS hire_year, 
		   DATE_FORMAT(HIREDATE,'%m') AS hire_month, 
		   DATE_FORMAT(HIREDATE,'%d') AS hire_day
    FROM EMP WHERE MONTH(HIREDATE) = h_month;
END
*/

-- Q10) 점수를 입력받아서 학점을 출력하는 프로시저를 만들ㅇ러보자.
CALL get_grade(100);
/*
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam10`(IN score INT)
BEGIN
	DECLARE grade VARCHAR(2);
	IF score >= 90 THEN
		SET grade = 'A';
    ELSEIF score >= 80 THEN
		SET grade = 'B';    
	ELSEIF score >= 70 THEN
		SET grade = 'C'; 
	ELSEIF score >= 60 THEN
		SET grade = 'D'; 
	ELSE
		SET grade = 'F';
	END IF;
    SELECT CONCAT('SCORE : ', score, 'GRADE : ', grade);
END
*/

-- Q11) 테이블을 만들어서 데이터를 1~10까지 입력하는 프로시저를 만들자.
CREATE TABLE TEST01(
	NO 		INT(3),
    MY_NAME VARCHAR(10)
);
DESC TEST01;
CALL INSERT_DATA_TEST01();
SELECT * FROM TEST01;
/*
CREATE DEFINER=`root`@`localhost` PROCEDURE `INSERT_DATA_TEST01`()
BEGIN
	DECLARE i INT(3) DEFAULT 1;
    
    WHILE i <= 10 DO
		INSERT INTO TEST01 VALUES(i , CONCAT('NO:',i));
		SET i = i+1;
	END WHILE;
END
*/

-- Q12) 구구단 3,5,7,9를 출력해보자
CALL multi_tables();
/*
CREATE DEFINER=`root`@`localhost` PROCEDURE `MULTI_TABLES`()
BEGIN
	DECLARE i INT DEFAULT 2;
    DECLARE j INT;
    DECLARE result INT;
    DECLARE output_text  VARCHAR(600) DEFAULT '';
    
    WHILE i <= 9 DO
		IF mod(i,2) <> 0 THEN
			SET output_text := CONCAT(output_text, i, '단\n');
            SET output_text := CONCAT(output_text, '====\n');
            
            set j=2;
			WHILE j <= 9 DO
				SET result = i*j;
                SET output_text := CONCAT(output_text,i,'*',j,'=',result,'\t');
                SET j = j+2;
			END WHILE;
            SET output_text := CONCAT(output_text,'\n');
		END IF;
        SET i=i+1;
    END WHILE;
    SELECT output_text AS output;
END
*/

-- CALL 값을 줄 때 니가 알아서 결과를 출력해라~
-- FUNCTION 내가 받아서 결과를 주겠다.
#######################################################
-- FUNCTION
CREATE FUNCTION hello(s CHAR(20))
RETURNS CHAR(50) DETERMINISTIC
RETURN CONCAT('Hello, ',s,'!');
SELECT hello('world');
-- => Functions 자동으로 만들어보기.
SELECT HELLO2('world');

-- Q13) 사원번호를 입력하면 월급에 100을 더한 값으로 출력하는 함수
SELECT MY_EMP.UPDATE_SAL(7788);
/*
CREATE DEFINER=`root`@`localhost` FUNCTION `UPDATE_SAL`(V_EMPNO INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
	DECLARE V_SAL DECIMAL(10,2);
	SELECT SAL+100 INTO V_SAL 
    FROM MT_EMP WHERE EMPNO=V_EMPNO;
	RETURN V_SAL;
END
*/

-- Q14) 사번을 입력받아서 연봉을 되돌리는 함수를 만들자.
SELECT EMPNO, GET_SAL(EMPNO) FROM MY_EMP;
/*
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_SAL`(V_EMPNO INT)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE V_SAL DECIMAL(10,2) DEFAULT 0;
    DECLARE V_TOT DECIMAL(10,2) DEFAULT 0;
    DECLARE V_COMM DECIMAL(10,2);
    SELECT SAL,COMM INTO V_SAL, V_COMM FROM MY_EMP WHERE EMPNO = V_EMPNO;
    
    SET V_TOT := V_SAL*12 + IFNULL(COMM,0);
    RETURN V_TOT;
END
*/

-- Q15) 사번을 입력받아서 부서명을 리턴하는 함수
SELECT * FROM MY_EMP;
SELECT ENAME, EMPNO, GET_DEPT(EMPNO) FROM MY_EMP;
/*
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_DEPT`(V_EMPNO INT)
RETURNS VARCHAR(50)
BEGIN
    DECLARE V_DNAME VARCHAR(50);
    SELECT DNAME INTO V_DNAME FROM MY_EMP JOIN MY_DEPT USING(DEPTNO) WHERE EMPNO=V_EMPNO;
    RETURN V_DNAME;
END
*/

-- Q16) 
-- 프로시저를 호출하게 되면 사원테이블의 empno, ename, sal의 전체내용을 emp_data라는 테이블에 저장하고
-- 출력하는 로직을 구현하자.
-- 결과SELECT -> 프로시저 -> 임시테이블
CALL my_emp.get_emp_data(); 
SELECT * FROM emp_data;
/*
CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_EMP_DATA`()
BEGIN
	DECLARE drop INT DEFAULT FALSE;
	DECLARE V_EMPNO INT;
    DECLARE V_ENAME VARCHAR(50);
    DECLARE V_SAL DECIMAL(10,2);
    DECLARE CUR_EMP CURSOR FOR SELECT EMPNO, ENAME, SAL FROM MY_EMP;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done TRUE;
    
    DROP TEMPORARY TABLE IF EXISTS EMP_DATA;
    CREATE TEMPORARY TABLE EMP_DATA(
	EMPNO INT,
    ENAME VARCHAR(50),
    SAL DECIMAL(10,2)
    );
    
    OPEN CUR_EMP
	READ_LOOP: LOOP
		FETCH CUR_EMP INTO V_EMPNO, V_ENAME, V_SAL;
        IF done THEN
			LEAVE READ_LOOP; 
		END IF;
        INSERT INTO EMP_DATA(EMPNO, ENAME, SAL) VALUES (V_EMPNO, V_ENAME, V_SAL); 
    END LOOP;
    CLOSE CUR_EMP;
END
*/
