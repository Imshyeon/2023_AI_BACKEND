CREATE DATABASE  IF NOT EXISTS `my_emp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `my_emp`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: my_emp
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping events for database 'my_emp'
--

--
-- Dumping routines for database 'my_emp'
--
/*!50003 DROP FUNCTION IF EXISTS `GET_DEPT` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_DEPT`(V_EMPNO INT) RETURNS varchar(50) CHARSET utf8mb4
    DETERMINISTIC
BEGIN
	DECLARE V_DNAME VARCHAR(50);
    #DECLARE V_ID INT;
    SELECT DNAME INTO V_DNAME FROM MY_EMP 
    JOIN MY_DEPT USING(DEPTNO) WHERE EMPNO = V_EMPNO; 
RETURN V_DNAME;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `GET_SAL` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_SAL`(V_ID INT) RETURNS int
    DETERMINISTIC
BEGIN
	-- 연봉 = (봉급 * 12) + 커미션
	DECLARE V_SAL DECIMAL(10,2) DEFAULT 0;
    DECLARE VTOT DECIMAL(10,2) DEFAULT 0;
    DECLARE VCOMM DECIMAL(10,2);
    SELECT SAL, COMM INTO V_SAL, VCOMM FROM EMP WHERE EMPNO = V_ID;
    
    SET VTOT := V_SAL * 12 + IFNULL(VCOMM,0);
RETURN VTOT;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `hello` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `hello`(s CHAR(20)) RETURNS char(50) CHARSET utf8mb4
    DETERMINISTIC
RETURN CONCAT('Hello, ',s,'!') ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `Hello2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `Hello2`(s CHAR(20)) RETURNS char(50) CHARSET utf8mb4
    DETERMINISTIC
BEGIN

RETURN CONCAT('Hello, ',s,'!');
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `UPDATE_SAL` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `UPDATE_SAL`(V_EMPNO INT) RETURNS decimal(10,2)
    DETERMINISTIC
BEGIN
	DECLARE V_SAL DECIMAL(10,2); -- 리턴할 값을 담은 변수
    SELECT SAL + 100 INTO V_SAL	-- INTO는 1:1 대입
    FROM MY_EMP
    WHERE EMPNO = V_EMPNO;
RETURN  V_SAL;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_emp_data` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_emp_data`()
BEGIN
	DECLARE done INT DEFAULT FALSE;
    DECLARE V_EMPNO INT;
    DECLARE V_ENAME VARCHAR(50);
    DECLARE V_SAL DECIMAL(10,2);
	DECLARE CUR_EMP CURSOR FOR SELECT EMPNO,ENAME,SAL FROM MY_EMP.MY_EMP;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET DONE = TRUE; -- 못찾았을 때! 변수에 TRUE 초기화
    -- continue 할 동안 not found면 SET done = True;해라.
    DROP TEMPORARY TABLE IF EXISTS EMP_DATA;
    CREATE TEMPORARY TABLE EMP_DATA(EMPNO INT, ENAME VARCHAR(50), SAL DECIMAL(10,2));
    
    OPEN CUR_EMP;
    READ_LOOP: LOOP
		FETCH CUR_EMP INTO V_EMPNO,V_ENAME,V_SAL;
        IF DONE THEN	-- 더이상 행을 찾을 수 없는 경우
			LEAVE READ_LOOP;
		END IF;
        INSERT INTO EMP_DATA(EMPNO, ENAME, SAL) VALUES(V_EMPNO,V_ENAME,V_SAL);
	END LOOP;
    CLOSE CUR_EMP;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_exam05` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam05`(IN dept_num INT)
BEGIN
	SELECT ENAME, DEPTNO 
	FROM EMP
	WHERE DEPTNO = dept_num ;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_exam06` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam06`(IN sal_input decimal(10,2))
BEGIN
	SELECT ENAME, SAL  
	FROM EMP 
	WHERE  SAL  >= sal_input; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_exam07` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam07`(IN dept_num INT, IN sal_input decimal(10,2))
BEGIN
	 SELECT ENAME, DEPTNO, SAL
	 FROM EMP
	 WHERE DEPTNO = dept_num  AND SAL  >= sal_input;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_exam08` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam08`(in dept_num int, in dept_num2 int)
BEGIN
	 SELECT ENAME, DEPTNO
	 FROM EMP
	 WHERE DEPTNO IN (dept_num,dept_num2);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_exam09` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam09`(IN month_input int)
BEGIN
	SELECT ENAME, YEAR(HIREDATE) AS hire_year,
				  DATE_FORMAT(HIREDATE,'%m') AS hire_month,
				  DATE_FORMAT(HIREDATE,'%d') AS hire_day
	FROM EMP
	WHERE month(HIREDATE) = month_input;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_exam10` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam10`()
BEGIN
DECLARE sql_statement VARCHAR(1000);
    SET sql_statement = '
        CREATE OR REPLACE VIEW EXAM10 AS
        SELECT
            EM.ENAME AS EMPLOYEE,
            EM.HIREDATE AS EMPHIREDATE,
            MG.ENAME AS MANAGER,
            MG.HIREDATE AS MGRHIREDATE
        FROM
            EMP EM
        LEFT OUTER JOIN EMP MG ON (EM.MGR = MG.EMPNO) 
        WHERE
            MG.HIREDATE > EM.HIREDATE;
     ';

    SET @sql_statement = sql_statement;  
   	PREPARE stmt FROM @sql_statement; -- SQl구문 동적 구문 선언 
   	EXECUTE stmt;     -- 실행  
    DEALLOCATE PREPARE stmt;   -- 해제
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GET_EXAM11` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_EXAM11`()
BEGIN
   DECLARE done INT DEFAULT FALSE;
   DECLARE V_DNAME, V_LOC VARCHAR(50);
    DECLARE V_NOP INT;
    DECLARE V_SAL DECIMAL(10,2);
    DECLARE OUTPUT VARCHAR(1000) DEFAULT '';
    DECLARE n INT DEFAULT 1;
    DECLARE CUR_11 CURSOR FOR SELECT DNAME, LOC, COUNT(EMPNO) AS 'NUMBER OF PEOPLE', ROUND(AVG(SAL),1) AS SALARY
                     FROM MY_EMP RIGHT JOIN MY_DEPT USING (DEPTNO)
                            GROUP BY DNAME, LOC;
   DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- CUR OPEN -> LOOP -> 각각의 값을 fetch ~ into v_~ -> set v_prn -> 출력 -> end loop -> close cur
    OPEN CUR_11;
    SET OUTPUT = 'DNAME\t\tV_LOC\t\tV_NOP\t\tV_SAL\n';
    
    READ_LOOP: LOOP
      FETCH CUR_11 INTO V_DNAME,V_LOC,V_NOP,V_SAL;
      IF done THEN
         LEAVE READ_LOOP;
      END IF;
	  
      IF V_DNAME = 'OPERATIONS' THEN
		SET OUTPUT := CONCAT(OUTPUT,V_DNAME,' \t',V_LOC,' \t',V_NOP,' \t','NULL\n');
		SELECT OUTPUT;
	  ELSE
		SET OUTPUT := CONCAT(OUTPUT,V_DNAME,' \t',V_LOC,' \t',V_NOP,' \t',V_SAL,'\n');
      END IF;
      
    END LOOP;
    CLOSE CUR_11;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_exam12` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_exam12`()
BEGIN
/*
    SELECT ENAME, DNAME, JOB
	FROM Emp
	INNER JOIN DEPT USING(DEPTNO)
	WHERE sal > (SELECT AVG(sal) FROM Emp WHERE  deptno = Emp.deptno); 
*/

	DECLARE v_name VARCHAR(100);
    DECLARE v_dname VARCHAR(100);
    DECLARE v_job VARCHAR(100);
    
    DECLARE done INT DEFAULT FALSE;
  
    DECLARE cur_exam12 CURSOR FOR
    SELECT ENAME, DNAME, JOB
    FROM Emp
    INNER JOIN DEPT USING (DEPTNO)
    WHERE  sal > (SELECT AVG(sal) FROM Emp WHERE  DEPT.deptno = Emp.deptno);

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
   


    OPEN cur_exam12;
    SET @output = '';

    fetch_loop: LOOP
        FETCH cur_exam12 INTO v_name, v_dname, v_job;
        IF done THEN
            LEAVE fetch_loop;
        END IF;
        SET @output = CONCAT(@output, v_name, '\t', v_dname, '\t', v_job, '\n');
    END LOOP;

    CLOSE cur_exam12;
    SET @output = CONCAT('ENAME\t\tDNAME\t\tJOB\n', @output);
    SELECT @output;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GET_EXAM12_2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_EXAM12_2`()
BEGIN
	DECLARE done INT DEFAULT FALSE;
    DECLARE V_ENAME, V_DNAME, V_JOB VARCHAR(100);
    DECLARE OUTPUT VARCHAR(1000) DEFAULT '';
    DECLARE CUR_12 CURSOR FOR SELECT ENAME, DNAME, JOB FROM Emp
							  INNER JOIN DEPT USING(DEPTNO)
							  WHERE sal > (SELECT AVG(sal) FROM Emp WHERE  dept.deptno = Emp.deptno); 
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- 커서 오픈 -> 루프 -> FETCH INTO -> IF DONE~ -> SET 이용해서 데이터 입력 -> LOOP 종료 -> 출력 -> CLOSE CURSOR 
    OPEN CUR_12;
    SET OUTPUT = 'ENAME\t\tDNAME\t\tJOB\n';
	READ_LOOP : LOOP
		FETCH CUR_12 INTO V_ENAME, V_DNAME, V_JOB;
		IF done THEN
			LEAVE READ_LOOP;
		END IF;
		SET OUTPUT := CONCAT(OUTPUT, V_ENAME, '\t\t', V_DNAME, '\t\t', V_JOB,'\n');
	END LOOP;
		SELECT OUTPUT;
    CLOSE CUR_12;
                              
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_grade` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_grade`(IN score01 int)
BEGIN
	DECLARE grade01 varchar(2);
    -- IF THEN ELSEIF END IF
	IF score01 >= 90 THEN
		SET grade01='A';
	ELSEIF score01 >= 80 then
		set grade01 = 'B';
	elseif score01 >=70 then
		set grade01 = 'C';
	elseif score01 >=60 then
		set grade01 = 'D';
	ELSE
		set grade01 = 'F';
	END IF;
	select CONCAT('SCORE : ',score01,'  GRADE : ', grade01);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `INSERT_DATA_TEST01` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `INSERT_DATA_TEST01`()
BEGIN
	DECLARE I INT(3) DEFAULT 1;
    -- WHILE 조건문 DO 명령 END WHILE;
    WHILE I <= 10 DO
		INSERT INTO TEST01(NO, MY_NAME) VALUES(I, CONCAT('NO:',I));
        SET I=I+1;
	END WHILE;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `multi_tables` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `multi_tables`()
BEGIN
	DECLARE i INT default 2;
    DECLARE j INT;
    DECLARE total INT;
    DECLARE output_text VARCHAR(600) default '';
    while i <= 9 DO
		IF MOD(i,2) <> 0 THEN
			set output_text := concat(output_text,i,'단\n');
            set output_text := concat(output_text,'=====\n');
            
            set j=2;
            while j <=9 do
				set total = j*i;
                set output_text := concat(output_text,i,'*',j,'=',total,'	');
                set j=j+1;
			end while;
            set output_text := concat(output_text,'\n');
		end if;
		SET i = i+1;
	end while;
SELECT output_text AS output;    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `my_calc` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `my_calc`()
BEGIN
	-- 변수선언
   DECLARE a float;
   DECLARE b float;
   DECLARE op char(1);
   DECLARE result float;
    
   -- 값 대입
   SET a=100;
   SET b=0;
   
   -- 연산
   SET op = '+';
   SET result = a+b;
   -- 출력
   select concat('hap : ',a,' ',op,' ',b,' = ',result) as output;
	
   SET op = '-';
   SET result = a-b;
   select concat('sub : ',a,' ',op,' ',b,' = ',result) as output;
    
   SET op = '*';
   SET result = a*b;
   select concat('mul : ',a,' ',op,' ',b,' = ',result) as output;
   
   
   SET op = '/';
   if b <> 0 then
		SET result = a/b;
		select concat('div : ',a,' ',op,' ',b,' = ',result) as output;
   else
		select 'Division by zero is not allowed' as output;
   end if;
 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `my_calc02` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `my_calc02`(IN a float, 
														IN b float, 
                                                        IN operator char(1))
BEGIN
	DECLARE result float;
    
    CASE operator
		WHEN '+' THEN SET result=a+b;
        WHEN '-' THEN SET result=a-b;
        WHEN '*' THEN SET result=a*b;
        WHEN '/' THEN
			if b <> 0 then
				SET result = a/b;
			else
				select 'Division by zero is not allowed' AS result;
			end if;
		ELSE
			SELECT 'invalid operator.[+,-,*,/]' AS result;
	END CASE;
    
    SELECT CONCAT('Result: ',a,' ',operator,' ',b,' = ',result) AS output;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `my_test` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `my_test`()
BEGIN
	
    DECLARE i int default 20; -- 변수를 선언
	SELECT CONCAT('처음 출력하는 프로시저 값 : ', i);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-31 16:19:39
