-- 11 해당 부서의 모든 사원에 대한 부서 이름, 위치, 사원 수 및 평균 급여를
-- 표시하는 정의를 작성한다. 
-- 열 이름을 각각 DNAME,LOC,NUMBER OF PEOPLE,SALARY로 한다.
SELECT DNAME, LOC, COUNT(EMPNO) AS 'NUMBER OF PEOPLE', ROUND(AVG(SAL),1) AS SALARY
							  FROM EMP RIGHT JOIN DEPT USING(DEPTNO)
                              GROUP BY DNAME, LOC;
/*
결과)
+------------+----------+------------------+--------+
| DNAME      | LOC      | NUMBER OF PEOPLE | SALARY |
+------------+----------+------------------+--------+
| ACCOUNTING | NEW YORK |                3 | 2916.7 |
| RESEARCH   | DALLAS   |                5 | 2175.0 |
| SALES      | CHICAGO  |                6 | 2133.3 |
| OPERATIONS | BOSTON   |                0 |   NULL |
+------------+----------+------------------+--------+
OPERATIONS를 FETCH할 때 SALARY에 NULL값이 들어감을 주의
*/
                              
CALL GET_EXAM11(); -- => SELESCT * FROM EXAM11; 임시 테이블 결과 출력
SELECT * FROM EXAM11;

/*
SOL)
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
END
*/