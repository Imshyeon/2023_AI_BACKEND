USE MY_EMP;
CREATE TABLE parent_table (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE child_table (
    id INT PRIMARY KEY,
    parent_id INT,
    description VARCHAR(100),
    FOREIGN KEY (parent_id) REFERENCES parent_table(id) ON DELETE CASCADE	#[ON DELETE reference_option] [ON UPDATE reference_option]
);

/*
Cascade : Delete or update the row from the parent table and automatically delete or update the matching rows in the child table. 
Both ON DELETE CASCADE and ON UPDATE CASCADE are supported. 
Between two tables, do not define several ON UPDATE CASCADE clauses that act on the same column in the parent table or in the child table.
*/

INSERT INTO parent_table (id, name) VALUES
    (1, 'Parent 1'),
    (2, 'Parent 2');

INSERT INTO child_table (id, parent_id, description) VALUES
    (101, 1, 'Child 1 of Parent 1'),
    (102, 1, 'Child 2 of Parent 1'),
    (103, 2, 'Child 1 of Parent 2');
    
SELECT * FROM parent_table;
SELECT * FROM child_table;

DELETE FROM parent_table WHERE id = 1;
-- id = 1에서 삭제되고 ON DELETE CASCADE 제약 조건으로 인해 with parent_table의 관련 행도 삭제
-- 두 테이블의 내용 확인 : PARENT2와 관련된 내용만 남았다.

################################################################
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    account_name VARCHAR(50),
    balance DECIMAL(10, 2)
);
INSERT INTO accounts (account_id, account_name, balance) VALUES
    (1, 'Account 1', 1000.00),
    (2, 'Account 2', 500.00);

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    from_account_id INT,
    to_account_id INT,
    amount DECIMAL(10, 2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- 송금 작업 수행 
START TRANSACTION;

-- @는 사용자 변수임
SELECT @from_balance := balance FROM accounts WHERE account_id = 1;
SELECT @to_balance := balance FROM accounts WHERE account_id = 2;


SET @transfer_amount := 200.00; #변수선언 := 값대입
UPDATE accounts SET balance = balance - @transfer_amount WHERE account_id = 1;
UPDATE accounts SET balance = balance + @transfer_amount WHERE account_id = 2;


INSERT INTO transactions (from_account_id, to_account_id, amount)
VALUES (1, 2, @transfer_amount);

-- 커밋 성공 
COMMIT;
-- 업데이트된 잔액과 트랜잭션 로그 확인  
SELECT * FROM accounts;
SELECT * FROM transactions;
SELECT @from_balance, @to_balance,@transfer_amount;

-- 금액 200.00이 에서 Account 1(으)로 이체되었으며 Account 2이에 따라 잔액이 업데이트되었다
-- ROLLBACK 명령을 사용하여 변경 사항을 실행 취소하고 데이터 일관성을 유지