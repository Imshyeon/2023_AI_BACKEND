use my_emp;
drop table my_emp;
create table my_emp as select * from emp;
create table my_dept as select * from dept;
select * from my_emp;
select * from my_dept;

-- 
create view empview  
as 
select  * from my_emp;	#실제 데이터는 없고 망원경으로 보는 것처럼. 실제 데이터는 my_emp에 있다.
-- Q1. empview를 통해서 데이터를 삭제 한 후 원본과 비교  
 delete from empview
 where empno =7369;
 select  * from my_emp;
 select * from empview;
-- Q2. my_emp를 통해서 데이터 삭제 한 후  view 비교 
 delete from my_emp
 where empno =7499;
 
 -- Q3. 조인된 view 만들어서 인서트 한 후 각 테이블의 업데이트를 확인 하자.  
 --  
  create view my_view
  as 
  select ename, empno, deptno, dname
  from my_emp join my_dept using(deptno);
 
  select  * from  my_view; 
  insert into my_view(ename,empno,deptno,dname) 
  values('홍길동',1111, 50, '서울');  -- 안들어감  
  
-- Q4. 참조형으로 되어 있는 테이블을 사용해서 view를 만들고 값을 입력해보자. 
  create view my_view02
  as 
  select ename, empno, deptno, dname
  from emp join dept using(deptno);
 
  select  count(*) from  my_view02; 
  
  insert into my_view02(ename,empno,deptno,dname) 
  values('홍길동',1111, 50, '서울');  -- 안들어감  
  