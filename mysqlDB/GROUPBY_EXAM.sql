USE MY_EMP;
create table  My_REPORT(
name varchar(10), 
color varchar(10), 
sales int);
 

insert into My_REPORT values ('shoes', 'Black', 4500);
insert into My_REPORT values ('Wallet', 'White', 3800);
insert into My_REPORT values ('shoes', 'Red', 5100);
insert into My_REPORT values ('shoes', 'Black', 4600);
insert into My_REPORT values ('Wallet', 'Black', 3900);
insert into My_REPORT values ('Wallet', 'White', 4000);
insert into My_REPORT values ('shoes', 'Red', 5200);

SELECT * FROM MY_REPORT;


-- Q3. 다음과 같이 그룹핑하자.
select name, sum(sales)
from My_REPORT group by name;
 
 -- Q4. 다음과 같이 그룹핑하자.
select name, color, sum(sales) 
from My_REPORT group by name, color;

-- Q5. 다음과 같이 출력 해보자.  
select name, sum(sales) 
from My_REPORT group by name with rollup;


-- Q6. 다음과 같이 출력 해보자.  
select name, color, sum(sales) 
from My_REPORT group by name, color;

-- Q7. 다음과 같이 출력 해보자
select name, color, sum(sales) 
from My_REPORT group by name, color with rollup;

-- 08. sales 값이 150 이상의 데이터만을 대상으로 그룹화하고, 그룹별로 sale  평균를 리턴하되  200 이상 만 출력하자. 
select NAME, avg(sales) as average 
from My_REPORT 
where sales >= 150 
group by NAME 
having average >= 200;

-- 09.제품 이름이 '신발'이고 판매량이 5000보다 크거나 같은 각 색상의 총 판매량을 검색하는 쿼리를 작성하자.  
SELECT color, SUM(sales) AS total_sales
FROM My_REPORT
WHERE name = 'shoes' AND sales >= 5000
GROUP BY color;

-- 10.판매량이 4000보다 큰 각 제품 이름에 대한 판매량을 출력하자.  
SELECT name, SUM(sales) AS total_sales
FROM My_REPORT
WHERE sales > 4000
GROUP BY name;
-- 11  '검은색' 및 제품 이름이 '신발' 또는 '지갑'인 판매량을 출력하자.  
SELECT name, SUM(sales) AS total_sales
FROM My_REPORT
WHERE color = 'Black' AND (name = 'shoes' OR name = 'Wallet')
GROUP BY name;
-- 12  판매량이 3800에서 5000 사이인 각 색상 및 제품 이름에 대한 총 판매량을 검색하자
   -- between and 
   SELECT color, name, SUM(sales) AS total_sales
FROM My_REPORT
WHERE sales BETWEEN 3800 AND 5000
GROUP BY color, name;

-- 13. 판매량이 4000개 이상이고 제품 이름이 'Wallet'이 아닌 제품 이름 및 색상을 출력하자. 
SELECT name, color
FROM My_REPORT
WHERE sales > 4000 AND name != 'Wallet';



