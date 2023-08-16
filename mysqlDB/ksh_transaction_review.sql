use my_test;
DROP TABLE IF EXISTS PARENT_TABLE, CHILD_TABLE;
CREATE TABLE parent_table(
	id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE child_table(
	id INT PRIMARY KEY,
    parent_id INT,
    description VARCHAR(100),
    FOREIGN KEY (parent_id) REFERENCES parent_table(id) ON DELETE CASCADE
);
SELECT * FROM parent_table;
SELECT * FROM child_table;

INSERT INTO parent_table(id,name) VALUES (1,'Parent1'),(2,'Parent2'),(3,'Parent3');
INSERT INTO child_table (id, parent_id, description) VALUES
    (101, 1, 'Child 1 of Parent 1'),
    (102, 1, 'Child 2 of Parent 1'),
    (103, 2, 'Child 1 of Parent 2'),
    (104, 3, 'Child 1 of Parent 3');
    
DELETE FROM parent_table WHERE id=3;

DROP TABLE IF EXISTS accounts, transactions;
CREATE TABLE accounts(
	account_id INT PRIMARY KEY,
    account_name VARCHAR(50),
    balance DECIMAL(10,2)
);
INSERT INTO accounts(account_id, account_name, balance) VALUES (1, 'Account 1', 1000.00),
															   (2, 'Account 2', 500.00);

CREATE TABLE transactions(
	transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    from_account_id INT,
    to_account_id INT,
    amount DECIMAL(10,2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);        

START TRANSACTION;
                                                       
SELECT @from_balance := balance FROM accounts WHERE account_id = 2; # account_id가 1인 Account1의 잔액 값을 설정
-- 1200
SELECT @to_balance := balance FROM accounts WHERE account_id = 1;
-- 500


SET @transfer_amount := 200.00;
UPDATE accounts SET balance = balance - @transfer_amount WHERE account_id=2;
select * from accounts; -- 잔액 : 700, 1000

UPDATE accounts SET balance = balance + @transfer_amount WHERE account_id=1;
select * from accounts; -- 900,800


INSERT INTO transactions(from_account_id, to_account_id,amount) 
VALUES (1,2,@transfer_amount);
select * from transactions;
savepoint s1;
savepoint s2;
rollback to savepoint s1;

commit; -- 커밋하기 전에는 cmd에서 동시에 select * from 해도 기존의 값만 나왔다. 하지만 commit한 후에 select * 하면 변경된 값이 나온다.

SELECT * FROM accounts;
SELECT * FROM transactions;
SELECT @from_balance, @to_balance, @transfer_amount;
rollback;
