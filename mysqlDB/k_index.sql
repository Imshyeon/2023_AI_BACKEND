/*
인덱스(index)
 테이블 안의 데이터를 쉽고 빠르게 찾을 수 있도록 만든 데이터베이스 객체이다. 
 SQL을 실행할 때, 디스크 접근 횟수를 줄여 검색 속도를 높이기 위해 인덱스를 사용한다. 
 B-트리를 이용하면 모든 데이터에 대한 일정 수준의 검색 시간을 보장하는 장점이 있다. 테이블 행이 입력되거나 수정될 때마다 인덱스가 재구성되어 데이터를 검색할 때는 효율
적이지만 데이터를 추가하고 수정할 때는 인덱스 관리 때문에 시간이 더 걸린다. 


 【인덱스 생성이 바람직한 경우】
• 기본키와 외래키의 경우, 인덱스 생성이 바람직하다. 대부분의 DBMS는 기본키에 대
해서 자동으로 인덱스를 생성한다. 
• WHERE 절 조건식에 자주 사용되는 테이블 열의 경우, 인덱스 생성이 바람직하다. 
• 조인 조건식에 자주 사용되는 테이블 열도 인덱스 생성이 바람직하다. 
• 하나의 테이블에 3~5개 정도의 인덱스가 효과적이다. 
• 가변길이 문자형이나 실수형, 날짜형 열보다는 정수형, 고정길이 문자형 열에 인덱스를 생성하는 것이 바람직하다. 그 외에는 바람직하지 않다.
• ORDER BY절이나 GROUP BY절에 자주 사용되는 열의 경우, 인덱스 생성을 고려할 수 있다.

 【인덱스 생성이 바람직하지 않은 경우】
• 갱신이 빈번한 테이블 열의 경우, 인덱스가 바람직하지 않다. 
• 집계 함수, 내장 함수를 적용하여 열 값을 변형하는 경우, 인덱스가 효과적이지 않다. 
• 성별 같은 열처럼 도메인이 작아서 열의 선택도(selectivity)가 높을 경우, 인덱스가 바람직하지 않다. 
• 범위 검색을 하는 경우, 인덱스가 바람직하지 않다.(NON-EQUI JOIN)
 • 테이블의 행 개수가 별로 없는 경우, 인덱스가 바람직하지 않다
*/

-- ----------------------------------------

USE WORLD;
CREATE TABLE BUSINESS(NAME VARCHAR(255), ADDR VARCHAR(255),
                  TEL VARCHAR(255));

INSERT INTO BUSINESS VALUES ('1','1','1');
INSERT INTO BUSINESS VALUES ('2','1','1');
INSERT INTO BUSINESS VALUES ('3','1','1');

SHOW CREATE TABLE BUSINESS;
-- SELECT * FROM BUSINESS;

CREATE INDEX MY_INDEX ON BUSINESS(NAME);

ALTER TABLE BUSINESS DROP INDEX MY_INDEX; -- ALTER TABLE로 수정..!

-- HTTPS://LAUNCHPAD.NET/TEST-DB
USE EMPLOYEES;
DESC employees;

select count(*) from employees;
-- 인덱스  컬럼
select * from employees  where emp_no=20000;	-- 빠름
-- 인덱스 없는 컬럼 
select * from employees  where last_name ='Matzke' and first_name='Jenwei';	-- 인덱스보다 느림

-- 추가 
 create index emp_idx  on  employees(last_name , first_name); -- 추가 후, 위에 있는 쿼리를 실행하면 더 빨라짐을 알 수 있다
--  삭제  
alter table employees drop index emp_idx ;


/*
트리거
데이터 변경 등 명세된 이벤트 발생시 감지하여 자동 실행되는 사용자 정의 프로시저
INSERT, UPDATE, DELETE 명령문의 실행 직전 후 자동으로 호출되어 실행
보통 무결성 제약 조건을 유지하거나 업무 규칙 등을 적용하기 위해 사용
ex. 장바구니에 담아놓은 상품을 구매하면, 장바구니에 담아놨던 내용이 삭제..
*/

use my_emp;
CREATE TABLE emp_test (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    change_date DATETIME,
    PRIMARY KEY(id)
);
-- 새 행이 emp_test 테이블에 삽입될 때마다 새 행의 change_date 필드가 자동으로 현재 타임스탬프로 설정
/*
DELIMITER //cmd에서 procedure, function등을 하기 전에, ~~하겟다..

CREATE TRIGGER before_emp_test_insert 
BEFORE INSERT ON emp_test
FOR EACH ROW
BEGIN
   SET NEW.change_date = NOW();
END;
//

DELIMITER ;
*/
-- 트리거 확인: 설정한 트리거 때문에 change_date 필드는 삽입 시점의 현재 타임스탬프로 자동으로 설정
INSERT INTO emp_test (first_name, last_name) VALUES ('John', 'Doe');

SELECT * FROM emp_test;


/*
TRIGGER: 테이블에서 특정 유형의 작업(예: INSERT, UPDATE 또는 DELETE)에 의해 실행되거나 트리거되는 일련의 명령 => 유동값
DEFAULT:  키워드를 사용하면 테이블을 생성하거나 변경할 때 열에 대한 기본값을 설정(단순고정값) =>단순 고정값
*/


-- Q1)  employees 테이블에 새 행이 삽입될 때마다 departments 테이블의 해당 부서에 대한 
 -- num_employees 필드가 자동으로 1씩 증가 시키자. 
USE MY_EMP;
CREATE TABLE Test_departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50),
    num_employees INT DEFAULT 0
);

CREATE TABLE Test_employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Test_departments(id) on delete cascade
);
drop table test_employees;
/*
DELIMITER //

CREATE TRIGGER after_employee_insert 
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
   UPDATE Test_departments SET num_employees = num_employees + 1 WHERE id = NEW.dept_id;
END;
//

DELIMITER ;
*/
insert into Test_departments(dept_name) values ('hr'), ('sales'),('develop');
select * from Test_departments;

insert into Test_employees(first_name, last_name, dept_id) values ('길동','홍',1);
insert into Test_employees(first_name, last_name, dept_id) values ('길동','정',2);
insert into Test_employees(first_name, last_name, dept_id) values ('수현','강',3),('jones','potter',3);
insert into Test_employees(first_name, last_name, dept_id) values ('수현','강',null); -- employees에서 null로 들어가긴 하지만 departments에서 count되진 않는다.
select * from Test_employees;

delete from test_employees;
delete from test_departments;

-- Q2)  . Test_employees 테이블에서 직원이 삭제될 때마다 Test_departments 테이블의 
   -- num_employees 필드를 업데이트하는 트리거를 생성해보자.
  /*
  DELIMITER //

CREATE TRIGGER after_employee_delete  
AFTER DELETE ON Test_employees #Test_employees 테이블에 대한 각 삭제 작업 후 트리거가 활성화
FOR EACH ROW  #삭제되는 각 행에 대해 트리거가 활성화 
BEGIN
   UPDATE Test_departments SET num_employees = num_employees - 1 WHERE id = OLD.dept_id;
   # OLD 키워드는 삭제할 행에 액세스하는 데 사용
END;
//

DELIMITER ;
*/
-- 1번 3명, 2번 2명, 3번 4명
delete from test_employees where id=2;
select * from test_departments; # 1번 3명, 2번 1명, 3번 4명으로 변경됨.
select * from test_employees;	#id = 2인 직원이 삭제됐다.
   
/*
OLD 및 NEW 키워드는 INSERT, UPDATE 또는 DELETE 작업과 같은 데이터 수정 이벤트
     전후의 열 값을 참조하기 위해 트리거 내에서 사용
OLD: OLD 키워드를 사용하면 행이 업데이트되거나 삭제되기 전에 행의 원래 값에 액세스할 수 있다. 
      참조할 기존 행이 필요하므로 UPDATE 및 DELETE 트리거에서만 사용된다.
       UPDATE 트리거에서 OLD.column_name을 사용하면 업데이트되기 전에 
      column_name의 값을 참조할 수 있다.
NEW: NEW 키워드를 사용하면 업데이트되거나 삽입된 행의 새 값에 액세스할 수 있다.
     'INSERT' 및 'UPDATE' 트리거에서 사용할 수 있다. 
      INSERT 트리거에서 NEW.column_name은 방금 삽입된 column_name의 값을 제공하며
      UPDATE 트리거에서 업데이트 후 column_name의 새 값을 제공한다. 
*/

--  Q3) 직원의 이름은 항상 대문자로 저장해야 한다는 규칙을 적용해보자. 
-- 'BEFORE INSERT' 트리거를 생성하여 새 이름을 테이블에 삽입하기 전에 자동으로 대문자로 변환할 수 있다.
/*
DELIMITER //

CREATE TRIGGER before_employee_insert
BEFORE INSERT ON Test_employees  # Test_employees 테이블에 대한 각 삽입 작업 전에 트리거가 활성화
FOR EACH ROW  #삽입되는 각 행에 대해 트리거가 활성화
BEGIN
   SET NEW.first_name = UPPER(NEW.first_name);  # NEW 키워드는 삽입되는 행에 액세스하고 수정하는 데 사용
END;
//

DELIMITER ;
*/
# 1번 - 3명, 2번 - 1명, 3번 - 4명
insert into Test_employees(first_name, last_name, dept_id) values ('harry','potter',2),
																  ('hermione','park',1),
                                                                  ('zoe','kang',3);
select * from Test_employees;
select * from test_departments;

-- Q4) Test_employees 테이블에서 update트리거를 생성하여 직원의 부서가 변경될 때마다
-- 	 Test_departments 테이블의 num_employees 필드를 자동으로 업데이트 해보자
# 10번이 부서번호가 3->1로 변경
#1번 - 4명, 2번 - 2명, 3번 - 5명
update test_employees set dept_id = 1 where id = 10;
select * from Test_employees;#10번 부서번호가 1번으로 변경됨
select * from test_departments; #1번 - 5명, 2번 - 2명, 3번 - 4명으로 변경
update test_employees set dept_id = 1 where id = 8; # 8번(부서번호 null)의 부서번호를 1번으로 변경 



###############################################################################
#partition

USE WORLD;

#1. city_partitioned 이란 테이블을 생성해서 분할 작업을 하기 위해 원본테이블에 있는 기본키를 변경한다. | 기본키 삭제, primary key를 다른 곳으로 이관한다.
# 분할을 하게 되면 모든 열에 고유키의 일부가 되어야하는 이유이다.
ALTER TABLE city DROP PRIMARY KEY, ADD PRIMARY KEY(ID, Population);
desc city;
select count(*) from city;

#2. 동일한 구조를 가진 새로운 테이블을 생성한다.
CREATE TABLE city_partitioned LIKE city;
desc city_partitioned;
select * from city_partitioned;

#3. 분할 행을 각 객체에 포함시킨다.
ALTER TABLE city_partitioned PARTITION BY RANGE(Population) (
    PARTITION p0 VALUES LESS THAN (1000000),
    PARTITION p1 VALUES LESS THAN (2000000),
    PARTITION p2 VALUES LESS THAN MAXVALUE
);
select * from information_schema.partitions where table_name = 'city'
					and table_schema = 'world';
select * from information_schema.partitions where table_name = 'city_partitioned'
					and table_schema = 'world';

#4. 모든 행의 테이블을 복사한겠다.
INSERT INTO city_partitioned SELECT * FROM city;
select count(*) from city_partitioned;

#5. 파티션 전 후에 쿼리를 실행하여 실행 시간을 비교해보자.
# 비교하기 전 캐시를 지운다.
select SQL_NO_CACHE * FROM city WHERE Population < 1000000;
explain SELECT * FROM city WHERE Population < 1000000; -- PARTITION에 대한 분포를 볼 수 있다.
select * from information_schema.partitions where table_name = 'city'
					and table_schema = 'world';
SELECT SYSDATE();SELECT COUNT(*) FROM city WHERE Population < 1000000;SELECT SYSDATE();                   
                    
DROP TABLE city;
RENAME TABLE city_partitioned TO city;


#######################################################
-- example
use my_emp;
CREATE TABLE t1 (
    id INT,
    year_col INT
)
PARTITION BY RANGE (year_col) (
    PARTITION p0 VALUES LESS THAN (1991),
    PARTITION p1 VALUES LESS THAN (1995),
    PARTITION p2 VALUES LESS THAN (1999),
    PARTITION p3 VALUES LESS THAN (2003),
    PARTITION p4 VALUES LESS THAN (2007)
);
desc t1;
-- schema 구조 확인
select * from information_schema.partitions where table_name = 't1' and table_schema = 'my_emp';

ALTER TABLE t1 ADD PARTITION (PARTITION p5 VALUES LESS THAN (2012)); #-> 스키마 구조 재확인, p5 생성 (2012로 자름)

select * from t1;

INSERT INTO T1 VALUES (1,1990);
INSERT INTO T1 VALUES (2,1993);
INSERT INTO T1 VALUES (3,1996);
INSERT INTO T1 VALUES (4,2000);
INSERT INTO T1 VALUES (5,2005);

EXPLAIN SELECT * FROM T1;

-- 실제 데이터 실행시간과 함께 확인
EXPLAIN SELECT * FROM T1 WHERE YEAR_COL<1990;
EXPLAIN SELECT * FROM T1 WHERE YEAR_COL<2004;

-- 파티션 객체 이름으로 데이터 추출
SELECT * FROM T1 PARTITION (P0);
SELECT * FROM T1 PARTITION (P1);
SELECT * FROM T1 PARTITION (P4);

-- 각 파티션 객체와 데이터 수 체크
select PARTITION_NAME, TABLE_ROWS from information_schema.partitions where table_name = 't1' and table_schema = 'my_emp';

ALTER TABLE t1 TRUNCATE PARTITION p1;	-- P1에 해당하는 값만 삭제
DELETE FROM t1 WHERE year_col < 1991;

ALTER TABLE t1 TRUNCATE PARTITION p1, p3; -- P1, P3에 해당하는 값만 삭제
DELETE FROM t1 WHERE
    (year_col >= 1991 AND year_col < 1995)
    OR
    (year_col >= 2003 AND year_col < 2007);

SELECT * FROM T1;
SELECT PARTITION_NAME, TABLE_ROWS
    FROM INFORMATION_SCHEMA.PARTITIONS
    WHERE TABLE_NAME = 't1';

/*
-- dump / import

mysqldump -u root -p  my_emp > my_emp_dump.sql

mysqldump -u root -p --no-data my_emp > my_emp_structure.sql

mysql -u root  -p my_emp < my_emp_dump.sql

<mysql manual>
mysqldump [options] db_name [tbl_name ...]
mysqldump [options] --databases db_name ...
mysqldump [options] --all-databases
*/

use my_test;
show tables; 