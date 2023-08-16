import sqlite3      #sqlite3 CRUD
#1. 연결 : database 생성
conn=sqlite3.connect('employee.db')
#2. 커서 생성
cursor=conn.cursor()
#3. 테이블 생성  employees   id(pk,autoincrement) 정수 ,name 문자열 nn,age 정수 nn ,city 문자열 nn
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL
    )
    '''
)

#4. insert_t, select, delete_t, update_t (_t : transaction)
def insert_employees(name, age, city):
    cursor.execute('insert into employees (name, age, city) values (?,?,?)',(name,age,city))
    conn.commit()

def selectall_employees():
    cursor.execute('select * from employees')
    return cursor.fetchall()
#수정 : 번호로 이름, 나이, 주소를 변경해보자
#1번 친구를 정길동 35 인천으로 변경해보자
def update_employees(id, name, age, city):
    cursor.execute('update employees set name=?, age=?, city=? where id =? ',(name,age,city,id))
    conn.commit()

def delete_employees(id):
    cursor.execute('delete from employees where id =?',(id,))
    conn.commit()

#5. 실행 결과
############insert

insert_employees('zoe',26,'london1')
insert_employees('hermione',23,'london2')
insert_employees('harry',23,'london3')

print(selectall_employees())
update_employees(1,'정길동',35,'인천')
print(selectall_employees())
delete_employees(1)
print(selectall_employees())
#6. conn close : 매우매우매우 중요!!
conn.close()