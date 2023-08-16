-- 1) CREATE TABLE로 새 테이블 만들기
-- 2) CREATE TABLE에서 기본 키 (PRIMARY KEY, not null) 제약 조건 지정
-- 		고유한 식별자이면서 null값을 포함할 수  없다.
-- 		컬럼 뒤에 선언, 복합 키로 primary key를 줄 수 있다.

-- 3) CREATE TABLE에서 고유 키(UNIQUE KEY, null 허용) 제약 조건 지정
-- 		지정된 열의 값이 테이블 전체에서 고유하도록 보장해라. null 허용, 중복키 없이 사용한다.

-- 4) CREATE TABLE에서 검사 (CHECK) 제약 조건 지정
-- 5) CREATE TABLE에서 열에 기본값 지정
-- 6) CREATE TABLE에서 외래 키 (FOREIGN KEY) 제약 조건 지정
-- 		두 테이블 간의 링크(참조)를 설정해서 한 테이블의 열의 값이 다른 테이블의 열의 값과 일치하도록 한다.

-- 7) Not NULL : 열에 Null값 포함하지 말자, default
-- 8) 제약 조건 삭제  
ALTER TABLE table_name DROP PRIMARY KEY;	#이름, 조건과 상관없음.
ALTER TABLE table_name DROP INDEX index_name;	#unique 삭제
ALTER TABLE table_name DROP FOREIGN KEY constraint_name;
ALTER TABLE table_name DROP CHECK constraint_name;	#check 제약조건 삭제
ALTER TABLE table_name DROP CONSTRAINT constraint_name;	#check 제약조건 삭제,(전체 제약조건 삭제)

-- 9) 제약 조건 추가 
ALTER TABLE table_name ADD PRIMARY KEY (column_name);
ALTER TABLE table_name ADD UNIQUE (column_name);

ALTER TABLE table_name ADD CONSTRAINT constraint_name
FOREIGN KEY (column_name) REFERENCES referenced_table_name (referenced_column);
ALTER TABLE table_name ADD CONSTRAINT constraint_name CHECK (condition);

-- 10) TYPE : BTREE -> 쿼리 최적화 인덱스 유형 [스키마 - student_my - indexes - MY_FK]
	-- 1. 인덱싱된 열을 기반으로 데이터를 빠르게 탐색할 수 있다.
    -- 2. 균형을 이진으로 잡고 쿼리를 탐색하는 구조.
    -- 3. 데이터를 정렬하고 쿼리, 조건 등의 구문(where, join, order by, group by)으로 데이터를 찾는다.
    -- 4. 기본으로 인덱싱을 BTREE로 하게 됨. CREATE INDEX idx_column ON tablename (column_name);
	create table test(
		name varchar(10),
        primary key (name) using btree 	#name은 btree로 명시해서 쓰겠구나..
										#사실, mysql 5.5 이후에는 기본
    ) engine = InnoDB;
###########################################################################

CREATE DATABASE  STUDENTS;
USE STUDENTS;

--  << 학생 정보를 유지하기 위한 students 테이블 생성 >>- 
/*
student_id: 레코드 ID(정수 유형)  --INT 
student_number: 학생 번호(최대 10자리 문자열 유형) VARCHAR
first_name: 아래 이름(최대 50자리 문자열 유형)  VARCHAR
last_name: 이름(최대 50자리 문자열 유형)VARCHAR 
middle_name: 중간 이름(최대 50자리 문자열 유형) VARCHAR
birthday: 생일(날짜형)   DATE
gender: 성별(문자열 형식으로 M: 남성, F: 여성)  ENUM  
paid_flag : 수업료를 지불했는지 여부 플래그 (BOOL 형식으로 FALSE (0) : 미결제, TRUE (1) : 지불됨) - BOOL  

*/

-- 1) CREATE TABLE로 새 테이블 만들기
DROP TABLE STUDENTS;

CREATE TABLE STUDENTS(
	student_id 		INT 				NOT NULL,
	student_number VARCHAR(10)  		NOT NULL,
	first_name 	   VARCHAR(50)  		NOT NULL,
	last_name 	   VARCHAR(50) 			NOT NULL,
	middle_name    VARCHAR(50)					,
	birthday 		DATE 				NOT NULL,
	gender 			ENUM ('M','F') 		NOT NULL,
	paid_flag 		BOOL 				NOT NULL
);
desc students;
INSERT INTO STUDENTS VALUES(1,1,1,1,1,NOW(),'F',TRUE);
INSERT INTO STUDENTS VALUES(1,1,1,1,1,NOW(),'M',0);
SELECT * FROM STUDENTS;


-- 2) CREATE TABLE에서 기본 키 (PRIMARY KEY, not null) 제약 조건 지정
-- 	 식별키, 테이블 당 하나의 컬럼만 지정할 수 있다(복합키 포함). _컬럼 라벨, 테이블 라벨 가능
#테이블라벨
CREATE TABLE STUDENTS02(
	student_id 		INT 				NOT NULL,
	student_number VARCHAR(10)  		NOT NULL,
	first_name 	   VARCHAR(50)  		NOT NULL,
	last_name 	   VARCHAR(50) 			NOT NULL,
	middle_name    VARCHAR(50)					,
	birthday 		DATE 				NOT NULL,
	gender 			ENUM ('M','F') 		NOT NULL,
	paid_flag 		BOOL 				NOT NULL,
    PRIMARY KEY (student_id)
);
DESC STUDENTS02;
-- 데이터 입력
INSERT INTO STUDENTS02 VALUES(1,1,1,1,1,NOW(),'F',TRUE);
INSERT INTO STUDENTS02 VALUES(2,1,1,1,1,NOW(),'M',0);	#중복 값 X 확인 -> 2로 변경
INSERT INTO STUDENTS02 VALUES(NULL,1,1,1,1,NOW(),'M',0);	#NULL값 X 확인
SELECT * FROM STUDENTS02;

-- 테이블 컬럼 레벨에 STUDENT_ID의 NOT NULL 없이 PRIMARY KEY 선언
CREATE TABLE STUDENTS03(
	student_id 		INT 		,
	student_number VARCHAR(10) 	,
    PRIMARY KEY (student_id)
);#PRIMARY KEY인 애들은 NOT NULL을 명시하던 아니던 어쨌든 NOT NULL이다.
DESC STUDENTS03;

-- 자동 증가를 PRIMARY KEY와 함께 지정
drop table students04;
CREATE TABLE STUDENTS04(
	student_id 		INT 		AUTO_INCREMENT,
	student_number VARCHAR(10) 				  ,
    PRIMARY KEY (student_id)
)AUTO_INCREMENT=404;	#자동증가를 특정값으로 재설정. 2번째 방법
DESC STUDENTS04;
INSERT INTO STUDENTS04 VALUES(1,1);
INSERT INTO STUDENTS04(student_number) VALUES(2);
INSERT INTO STUDENTS04 VALUES (10,1);
INSERT INTO STUDENTS04(student_number) VALUES(2);
INSERT INTO STUDENTS04 VALUES (20,1);
INSERT INTO STUDENTS04(student_number) VALUES(1);# 21   1
INSERT INTO STUDENTS04 VALUES (-20,1);			 #-20   1
INSERT INTO STUDENTS04(student_number) VALUES(1);# 22   1
INSERT INTO STUDENTS04(student_number) VALUES(-1);#23  -1
INSERT INTO STUDENTS04 VALUES (-21,-1);			  #-21 -1
INSERT INTO STUDENTS04(student_number) VALUES(-1);#24  -1
SELECT * FROM STUDENTS04;

-- 자동 증가를 특정 값으로 재설정 하고싶다. 1번째 방법
ALTER TABLE STUDENTS04 AUTO_INCREMENT=404;
INSERT INTO STUDENTS04(student_number) VALUES(2);#404   2
INSERT INTO STUDENTS04(student_number) VALUES(1);#405   1
SELECT * FROM STUDENTS04; 

-- 테이블의 상태 값(기본정보)을 확인하자.
SHOW TABLE STATUS LIKE 'STUDENTS04';	#SHOW는 ROOT 접속하자마자 전역으로 볼 수 있는거.

SELECT * FROM information_schema.TABLES 
WHERE TABLE_NAME = 'STUDENTS04' AND TABLE_SCHEMA = 'STUDENTS';	#어떤 스키마 안으로 들어왔을 때. 어떤 USE로 들어왔을 때.


-- 기본값을 설정해보자.
DROP TABLE STUDENTS05;
CREATE TABLE STUDENTS05(
	student_id 		INT 		   AUTO_INCREMENT,
	student_number VARCHAR(10) 		DEFAULT 'ABC', #DEFAULT와 NOT NULL은 컬럼라벨만 가능 
												   #NULL은 데이터라고 생각해서 입력을 받는다.
    PRIMARY KEY (student_id)
)AUTO_INCREMENT=1000;
#DEFAULT를 했는데 NOT NULL을 굳이..? 하지만 이런 문법 되긴 한다.
#DEFAULT를 했다고 NULL이 안들어가는 건 아님.. NULL 들어간다!

DESC STUDENTS05;
INSERT INTO STUDENTS05(student_id) VALUES(1);#값을 입력하지 않은 경우 기본값으로 대처
INSERT INTO STUDENTS05(student_number) VALUES(NULL);#NULL은 입력이 된다. NULL 입력 확인
INSERT INTO STUDENTS05(student_id) VALUES(2);#값을 입력하지 않은 경우 기본값으로 대처
SELECT * FROM STUDENTS05; 

-- 3) CREATE TABLE에서 고유 키(UNIQUE KEY, null 허용) 제약 조건 지정
-- 4) CREATE TABLE에서 검사 (CHECK) 제약 조건 지정
CREATE TABLE STUDENTS06(
	student_id 		INT,
	student_number VARCHAR(10),	
    birthday		DATE,
    UNIQUE KEY(student_id),
    CHECK(birthday >= '2000-01-01')
);
DESC STUDENTS06;
-- 제약조건 확인
SELECT * FROM information_schema.table_constraints
WHERE table_name='STUDENTS06';

INSERT INTO STUDENTS06 VALUES (1,1,'2000-05-29');
INSERT INTO STUDENTS06(student_id) VALUES (NULL);
INSERT INTO STUDENTS06(student_id, birthday) VALUES (2,NOW());
INSERT INTO STUDENTS06(student_id, birthday) VALUES (3,NOW());
SELECT * FROM STUDENTS06;
INSERT INTO STUDENTS06(student_id, birthday) VALUES (4,'1996-07-15');

-- 체크 제약조건 확인
SELECT * FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS;


-- 6) CREATE TABLE에서 외래 키 (FOREIGN KEY) 제약 조건 지정
-- FOREIGN KEY(자신의 테이블 컬럼명) REFERENCES 다른 테이블 명 (다른 테이블의 컬럼명)
DROP TABLE STUDENTS05;
#DEPT 테이블 같은 느낌
CREATE TABLE STUDENTS05(
	student_id 		INT 		   AUTO_INCREMENT,
	student_number VARCHAR(10) 		DEFAULT 'ABC', 
    PRIMARY KEY (student_id)
);
INSERT INTO STUDENTS05 VALUES(1,1);
INSERT INTO STUDENTS05 VALUES(2,2);
SELECT * FROM STUDENTS05;

-- 현재 student_my 테이블의 student_id를 STUDENTS05 테이블의 student_id로 참조
#EMP 테이블 같은 느낌
CREATE TABLE STUDENT_MY(
	student_id 		INT		NOT NULL,
    FOREIGN KEY(student_id) REFERENCES STUDENTS05(student_id)
);
INSERT INTO STUDENT_MY VALUES(1);
INSERT INTO STUDENT_MY VALUES(2);
INSERT INTO STUDENT_MY VALUES(7);	#Error Code : 1452
SELECT * FROM STUDENT_MY;

-- 제약조건 확인 추가, 삭제
SELECT * FROM information_schema.table_constraints
WHERE table_name='STUDENTS06';

SELECT * FROM information_schema.table_constraints
WHERE table_name='STUDENTS05';

SELECT * FROM information_schema.table_constraints
WHERE table_name='STUDENT_MY';


-- 8) 테이블 생성 후 제약조건 추가, 삭제를 해보자. 
CREATE TABLE emp(
	emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(30),
    salary DECIMAL(10,2)
);
DESC EMP;

-- 8-1) EMP_NAME에 고유키를 추가하자.
ALTER TABLE EMP ADD UNIQUE (emp_name);

-- 8-2) 급여를 0보다 크거나 같도록 제한하는 CHECK 제약조건 추가
ALTER TABLE EMP ADD CONSTRAINT MYSAL CHECK (salary >= 0); #조건을 변경하고 싶다면 기존의 조건을 삭제 후 다시 ADD..
-- 체크 제약 조건 확인
SELECT * FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS;

-- 8-3) 체크제약조건 삭제해보자.
ALTER TABLE EMP DROP CHECK MYSAL;
#ALTER TABLE EMP DROP CONSTRAINT MYSAL;

-- 8-4) EMP 테이블의 고유키를 삭제하자.
ALTER TABLE EMP DROP INDEX emp_name;

-- 8-5) student_my가 가진 참조키를 확인 후 삭제한다.
SELECT * FROM information_schema.table_constraints
WHERE table_name='student_my' AND TABLE_SCHEMA = 'STUDENTS';
ALTER TABLE STUDENT_MY DROP FOREIGN KEY student_my_ibfk_1;

-- 8-6) student_my를 emp를 참조하는 제약조건을 추가하자.
ALTER TABLE STUDENT_MY ADD CONSTRAINT MY_FK 
FOREIGN KEY (student_id) REFERENCES EMP(emp_id);	#출력하는 오류 메시지 : 테이블에 없는 값을 참조하려고 한다.

#일치하는 값 확인
SELECT student_id FROM student_my
WHERE student_id NOT IN(SELECT EMP_ID FROM EMP);

#FOREIGN KEY 제약조건은 참조 무결성을 적용한다. : 한쪽은 null이라서 참조를 하지 못한다.

-- 8-7) 참조 추가할 테이블의 데이터가 존재하지 않아 8-6에서 무결성 에러가 발생.	
-- 해결책 : 참조될 테이블에 참조될 열의 값이 존재해야 한다.
# INSERT INTO EMP(emp_id, emp_name) VALUES(1,1); --> emp_id,emp_name은 반드시 값을 줘야함. 왜냐하면 not null 이니까.
INSERT INTO EMP VALUES(1,'홍길동','영업',500);
INSERT INTO EMP VALUES(2,'정길동','연구',700);

SELECT * FROM information_schema.table_constraints
WHERE table_name='STUDENT_MY' AND TABLE_SCHEMA = 'STUDENTS';

/*
<추가>
ALTER TABLE table_name ADD PRIMARY KEY (column_name);
ALTER TABLE table_name ADD UNIQUE (column_name);

ALTER TABLE table_name ADD CONSTRAINT constraint_name
FOREIGN KEY (column_name) REFERENCES referenced_table_name (referenced_column);
ALTER TABLE table_name ADD CONSTRAINT constraint_name CHECK (condition);
*/

/*
<삭제>
ALTER TABLE table_name DROP PRIMARY KEY;	#이름, 조건과 상관없음.
ALTER TABLE table_name DROP INDEX index_name;	#unique 삭제
ALTER TABLE table_name DROP FOREIGN KEY constraint_name;
ALTER TABLE table_name DROP CHECK constraint_name;	#check 제약조건 삭제 
ALTER TABLE table_name DROP CONSTRAINT constraint_name;	#check 제약조건 삭제,(전체 제약조건 삭제) -- MYSQL 80.16버전
*/-- MYSQL 8버전 이전





























