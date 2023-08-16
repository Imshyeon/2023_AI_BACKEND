/*
-group by
1. group by 문 다음에는 데이터를 구분 짓기위한 표현식으로  해당 테이블의 컬럼 명이나 변수 값 등이 올수 있으며 
        그룹 함수를 사용한 형태는 올 수 없다< group by avg(sal) 안됨>

2. select-list에는 group by문에는 명시된 표현식과  그외 그룹합수를 사용한 표현식만이 올 수있다
     (*는 안됨 )
3. 출력된 결과를 정렬하기 위해 order by 문을 사용하면 된다
  단 order by 문 다음에는 select-list에서 명시된 컬럼 또는 표현식과 컬럼의 별칭(alias), 컬럼 번호 등만 사용
-- SELECT-LIST = SELECT

[GROUP BY {col_name | expr | position}, ... [WITH ROLLUP]]
    [HAVING where_condition]	-- GROUP BY의 조건문

*/

-- Q1) 부서별 평균 월급을 구해라.
USE MY_EMP;
SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO;
SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO ORDER BY DEPTNO DESC;
SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO ORDER BY 1 DESC;
SELECT DEPTNO AS NO, AVG(SAL) AS 별칭 FROM EMP GROUP BY DEPTNO ORDER BY 별칭 DESC;
SELECT DEPTNO AS NO, AVG(SAL) AS 별칭 FROM EMP GROUP BY DEPTNO ORDER BY 별칭;

-- Q2) 직업별 평균 월급을 구하자.
SELECT JOB, AVG(SAL) FROM EMP GROUP BY JOB ORDER BY 1;

-- Q3) 부서별 평균 월급을 구하되, 10번 부서의 평균 월급만 구하자.
SELECT DEPTNO, AVG(SAL) FROM EMP WHERE DEPTNO=10 GROUP BY DEPTNO;

-- Q4) 직업별 월급의 합을 구하라.
SELECT JOB, SUM(SAL) FROM EMP GROUP BY JOB;

-- Q5) 직업이 SALESMAN인 사원의 월급의 합
SELECT JOB, SUM(SAL) FROM EMP WHERE JOB='SALESMAN';

-- Q5-1) 직업별 사원의 월급의 합을 구하되, 직업이 SALESMAN인 사원을 출력
SELECT JOB, SUM(SAL) FROM EMP WHERE JOB='SALESMAN' GROUP BY JOB;

-- Q6) 사원테이블에서 사원의 최대 월급
SELECT MAX(SAL) FROM EMP;

-- Q7) 각 부서별 사원의 최대월급을 구해라
SELECT DEPTNO, MAX(SAL) FROM EMP GROUP BY DEPTNO;

/*
	IS [NOT] NULL
*/
-- Q1) 사원테이블에서 커미션이 책정되어있는 사원의 이름과 커미션을 출력
SELECT ENAME, COMM FROM EMP WHERE COMM IS NOT NULL;
-- Q2) 사원테이블에서 커미션이 책정되지 않는 사원의 이름과 커미션을 출력
SELECT ENAME, COMM FROM EMP WHERE COMM IS NULL;

/*
수행순서
SELECT-------5
FROM---------1
WHERE--------2
GROUP BY-----3
HAVING-------4
ORDER BY-----6
*/

/*
HAVING : GROUP BY 함수로 집계된 데이터에 조건을 줄 때 사용하는 키워드
SELECT-LIST 에서 사용한 컬럼과 그룹함수를 사용한 컬럼에 대해서만 조건을 줄 수 잇다.
[HAVEING where_condition]
*/
-- Q1) 직업별 전체 월급을 구하고, 그 월급이 5000 이상인 것만 출력
SELECT JOB, SUM(SAL) FROM EMP GROUP BY JOB HAVING SUM(SAL) >= 5000;
-- Q2) 부서별 월급의 합을 구하고 합이 1000 이상인 것만 출력 
SELECT DEPTNO, SUM(SAL) FROM EMP GROUP BY DEPTNO HAVING SUM(SAL)>=1000;

/*
[[WITH ROLLUP]] : 그룹 총합, 세부 소계(부분합), ROLLUP 연산자는 GROUP BY 문과 함께 사용,
	GROUP BY 문에서 사용된 명시 컬럼 순서대로 추가적인 요약 정보를 단계적으로 만들어 준다.
*/
-- Q1) 부서 별 총합 뿐만 아니라 전체 총합 및 세부 내역을 보고 싶을 때
SELECT DEPTNO, ENAME, SUM(SAL) 
FROM EMP 
GROUP BY DEPTNO, ENAME WITH ROLLUP;

-- Q2) ROLLUP을 이용해서 직위별 사원의 이름과 월급을 출력
SELECT JOB, ENAME, SUM(SAL) FROM EMP
GROUP BY JOB, ENAME WITH ROLLUP 
ORDER BY JOB;

/*
CUBE = 소계, 총계 GROUP BY 문과 함께 사용하게 되면 GROUP BY 문에서 선언된 
전체 컬럼에 대해서 추가적인 요약 정보를 단계적으로 만들어줌. ms_sql, oracle에선 가능. 하지만  mysql에서는 IF(GROUPING()) 이렇게 한다.
GROUPING : 그룹 기준에서 고려하지 않은 부분 총계인 경우에 1을 리턴하고 그렇지 않을 경우 0을 리턴한다.

-- SELECT JOB, ENAME, SUM(SAL) FROM EMP GROUP BY CUBE(JOB,ENAME); => ERROR : MYSQL에서는 IF(GROUPPING())을 사용

*/
-- Q1) 
SELECT ENAME, COMM, SUM(COMM) AS SUM, GROUPING(ENAME), GROUPING(COMM)
FROM EMP
GROUP BY ENAME, COMM WITH ROLLUP;

/*
 기준이 되는 컬럼값으로 그룹핑 분할하고 그중에서 해당 컬럼 값의 차순을 일련번호로 리턴한다.
SELECT ROW_NUMBER() [OVER PARTITION BY,
							ORDER BY ]
	   RANK() [OVER PARTITION BY,
							ORDER BY ]   -> 1등, 2,2,2등,5등,6,6,8등
	   DENSE_RANK() [OVER PARTITION BY,
							ORDER BY ] -> 1등,2,2,2,3등,4,4,5등
                            
EX) 열 A값의 내림차순으로 일련번호를 리턴 SELECT ROW_NUMBER() OVER (ORDER BY A DESC);
 기준이 되는 X 컬럼 값으로 그룹핑 분할하고 그중에서 해당 컬럼 A 값의 차순을 일련번호로 리턴한다.
SELECT ROW_NUMBER() OVER (PARTITION BY X ORDER BY A DESC);

*/
-- 예시
SELECT ROW_NUMBER() OVER (ORDER BY ENAME), ENAME FROM EMP;
SELECT ROW_NUMBER() OVER (PARTITION BY JOB ORDER BY ENAME DESC), JOB, ENAME FROM EMP;

-- DAY(), YEAR(), MONTH(), DATE(), WEEKDAY() : 월화수..
SELECT DAY(HIREDATE), YEAR(HIREDATE), MONTH(HIREDATE), DATE(HIREDATE), WEEKDAY(HIREDATE)
FROM EMP;

SELECT 
	RANK() OVER (ORDER BY DAY(HIREDATE)) AS RANK_NO,
	EMPNO, 
    ENAME, 
    HIREDATE 
FROM EMP;

SELECT
	DENSE_RANK() OVER(ORDER BY DAY(HIREDATE)) AS DENSE_NO,
    EMPNO,
    ENAME,
    HIREDATE
FROM EMP;

SELECT
	DENSE_RANK() OVER(ORDER BY YEAR(HIREDATE)) AS DENSE_NO,
    EMPNO,
    ENAME,
    HIREDATE
FROM EMP;

SELECT
	DENSE_RANK() OVER(ORDER BY MONTH(HIREDATE)) AS DENSE_NO,
    EMPNO,
    ENAME,
    HIREDATE
FROM EMP;

SELECT
	DENSE_RANK() OVER(ORDER BY DATE(HIREDATE)) AS DENSE_NO,
    EMPNO,
    ENAME,
    HIREDATE
FROM EMP;

SELECT
	DENSE_RANK() OVER(ORDER BY WEEKDAY(HIREDATE)) AS DENSE_NO,
    EMPNO,
    ENAME,
    HIREDATE,
    WEEKDAY(HIREDATE) AS 요일
FROM EMP;

/*
SELECT WEEKDAY(NOW()); # 0  ~  6 // 월: 0, 화: 1
/*(DATETIME OR DATE)
  YEAR(): 1000 ~  9999  4자리 표시  
  MONTH() : 1 ~ 12
  DAY ()  : 1~  31
  DAYOFMONTH()  = DAY()  
  HOUR() / MINUTE() / SECOND() 
  DATE_ADD( INTERVAL ) , DATE_SUB() 

*/

-- 변수를 활용해서 날짜 함수를 사용해보자.
-- Q1) 변수를 통해서 날짜 함수를 활용해보자
SET @date = NOW();
SELECT @date, year(@date), month(@date), day(@date);

SELECT HOUR(@date), MINUTE(@date), SECOND(@date); 

-- 제어문 if, while, loop, repeat, case ~ when ~ then 문 (case ~ end문)
-- Q2) 변수를 통해서 날짜함수 WEEKDAY()를 활용해보자.
SET @data= NOW();
SELECT @data,
		case weekday(@date)
			when 0 then '월'
			when 1 then '화'
			when 2 then '수'
			when 3 then '목'
			when 4 then '금'
			when 5 then '토'
			when 6 then '일'
            end as 요일;
        
-- BETWEEN ~ AND
-- 사원의 봉급 1000에서 2000 사이의 사원의 이름과 봉급을 출력
SELECT ENAME, SAL FROM EMP WHERE SAL BETWEEN 1000 AND 2000;
SELECT ENAME, SAL FROM EMP WHERE SAL>=1000 AND SAL<=2000; -- 위와 같은 결과
-- Q1) 사원테이블의 내용을 출력하되, EMPNO순으로 내림차순 5줄만 출력해보자
-- [LIMIT {[offset,] row_count | row_count OFFSET offset}]
SELECT * FROM EMP ORDER BY EMPNO DESC LIMIT 5;
SELECT * FROM EMP ORDER BY EMPNO DESC LIMIT 5 OFFSET 10;
SELECT * FROM EMP ORDER BY EMPNO DESC LIMIT 1 OFFSET 14; -- 15번째부터 1행을 검색
SELECT * FROM EMP ORDER BY EMPNO DESC LIMIT 5,10; -- 5~15행 가져옴 -> 실질적으로 14행까지
SELECT * FROM EMP ORDER BY EMPNO DESC LIMIT 10, 5;
SELECT * FROM EMP ORDER BY EMPNO DESC LIMIT 5, 1;
	
-- ------------------------------
-- Q1) 다음 쿼리를 통해 테이블을 생성해보자.
use my_emp;
DROP TABLE My_REPORT;
CREATE TABLE My_REPORT(
name varchar(10),
color varchar(10),
sales int);

select * from My_REPORT;

-- Q2) 데이터를 다음과 같이 입력해본다.
insert into My_REPORT
values ('shoes', 'Red', 5200),
	   ('Wallet', 'White', 3800),
       ('shoes', 'Red', 5100),
	   ('shoes', 'Black', 4600),
       ('Wallet', 'Black', 3900),
	   ('Wallet', 'White', 4000),
       ('shoes', 'Red', 5200);
commit;


-- Q3) 다음과 같이 그룹핑하자.
select name, sum(sales) from My_REPORT group by name;
-- Q4) 
select name, color, sum(sales) from My_REPORT group by name, color;
-- Q5)
select name, sum(sales) from My_REPORT group by name with rollup;
-- Q6)
select name, color, sum(sales) from My_REPORT group by name, color;
-- Q7)
select name, color, sum(sales) from My_REPORT group by name, color with rollup;
-- Q8) sales 값이 150 이상의 데이터만을 대상으로 그룹화하고, 그룹별로 sales 평균을 리턴하되 200 이상만 출력하자.
select name as NAME, avg(sales) as average from My_REPORT group by name;
select name as NAME, avg(sales) as average from My_REPORT where sales >= 150 group by name having avg(sales) >= 200;


-- 09.제품 이름이 '신발'이고 판매량이 5000보다 크거나 같은 각 색상의 총 판매량을 검색하는 쿼리를 작성하자.  
select color, SUM(sales) AS total 
from My_REPORT 
where name = 'shoes' and sales >= 5000 
group by color;

-- 10.판매량이 4000보다 큰 각 제품 이름에 대한 판매량을 출력하자.  
select name, sum(sales) 
from My_REPORT 
where sales > 4000 
group by name;

-- 11  '검은색' 및 제품 이름이 '신발' 또는 '지갑'인 판매량을 출력하자.  
select name, color, sum(sales) 
from My_REPORT 
where name in ('shoes','Wallet') and color = 'Black' 
group by name, color;

-- 12  판매량이 3800에서 5000 사이인 각 색상 및 제품 이름에 대한 총 판매량을 검색하자
   -- between and 사용
select name, color, sum(sales)
from My_REPORT
where sales between 3000 and 5000
group by name, color;   

-- 13. 판매량이 4000개 이상이고 제품 이름이 'Wallet'이 아닌 제품 이름 및 색상을 출력하자.
select name, color, sum(sales) as total_sale
from My_REPORT
where sales >= 4000 and name <> 'Wallet'
group by name, color;

-- 14. 물건 종류별 색상수와 평균 가격을 출력하시오
select name, count(color), avg(sales)
from My_REPORT
group by name;

-- 15. 색상이 같은 물건들의 평균 값을 출력하시오
select color, avg(sales) as average
from My_REPORT
group by color;

-- 16. 신발,지갑 상관없이 금액따라 오름차순 정리하고 색깔별로 개수 표기 하기
select name, sales, count(color) 
from My_REPORT
group by name, sales
order by 2 asc; 

-- myQ1. 이름이 신발이고 색상이 Red인 제품의 판매량을 출력. where를 사용하지 않고.
select name, color, sum(sales)
from My_REPORT 
group by name, color
having name = 'shoes' and color = 'Red';

-- myQ2. 판매량이 3000 이상인 제품들 중에 색깔의 수가 2개 이상인 제품을 출력
select name, color, sum(sales)
from My_REPORT
where sales > 3000
group by name,color
having count(color) >= 2;

-- ------------------------------------------------------------------

USE MY_EMP;
CREATE TABLE orders(
	order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    order_status VARCHAR(50)
);
INSERT INTO orders(customer_id, order_date, total_amount, order_status)
VALUES
	(101,'2023-07-23',250.00,'Shipped'),
    (102,'2023-07-24',1200.00,'Processing'),
    (103,'2023-07-25',350.00,'Delivered');
    
COMMIT; -- 저장(INSERT,DELETE,UPDATE)
SELECT * FROM orders;

-- 주문의 개별 항목을 볼 수 있는 테이블을 생성 _order_items
-- order_id 컬럼으로 orders 테이블의 해당 order_id에 연결되어 "주문과 해당 항목간의 관계"를 나타낸다.
-- => FOREIGN KEY (order_id) REFERENCES orders(order_id)
 
CREATE TABLE order_items(
	item_id INT AUTO_INCREMENT PRIMARY KEY, -- 컬럼 레벨 (NOT NULL)
    order_id INT,
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    total_price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) -- 테이블 레벨 (NOT NULL 안됨)
);
-- FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE 
-- => ORDERS 테이블에서 행을 삭제하게 되면 일치하는 ORDER_ID가 있는 ORDER_ITEMS 테이블에 해당되는 모든 행이
-- 자동으로 삭제 된다. (강한 종속 관계)


INSERT INTO order_items(order_id,product_name,quantity,price,total_price)
VALUES
	(1,'BOOK',1,30.0,35.0),
    (2,'PENCIL',2,15.0,20.0),
    (3,'PEN',3,20.0,30.0),
    (2,'PEN',3,20.0,30.0),
    (1,'지우개',3,20.0,30.0);
INSERT INTO order_items(order_id,product_name,quantity,price,total_price)
VALUES (NULL,'지우개',3,20.0,30.0);
    
-- 제약조건 거는 이유 : 데이터 유실하지 말자. 
desc order_items;
commit;
SELECT * FROM order_items;

-- 제약조건 확인하는 테이블
SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE TABLE_SCHEMA='MY_EMP' AND TABLE_NAME='order_items';
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE TABLE_SCHEMA = 'MY_EMP' AND TABLE_NAME='ORDERS';
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE TABLE_SCHEMA = 'MY_EMP' AND TABLE_NAME='ORDER_ITEM';
desc order_items;
DESC INFORMATION_SCHEMA.TABLE_CONSTRAINTS;
commit;

-- 테이블의 구조는 그대로 나두고 데이터의 내용만 전체 삭제하고 싶다.
-- DELETE FROM TABLE_NAME; -- 참조관계가 있음!
