import sqlite3      #sqlite3 CRUD -> class로 변형

class EmployeeDB:
    def __init__(self,db_name):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.executescript(
            '''
            DROP TABLE IF EXISTS employees;
            CREATE TABLE employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                city TEXT NOT NULL
            )
            '''
        )
        self.conn.commit()

    def insert_employees(self, name, age, city):
        self.cursor.execute('insert into employees (name, age, city) values (?,?,?)',(name,age,city))
        self.conn.commit()

    def selectall_employees(self):
        self.cursor.execute('select * from employees')
        return self.cursor.fetchall()

    def update_employees(self, id, name, age, city):
        self.cursor.execute('update employees set name=?, age=?, city=? where id =? ',(name,age,city,id))
        self.conn.commit()

    def delete_employees(self, id):
        self.cursor.execute('delete from employees where id =?',(id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    db= EmployeeDB('emp.db')

    db.insert_employees('헤르미온느',25,'호그와트')
    db.insert_employees('해리포터',25,'그린고트')
    db.insert_employees('시리우스 블랙',40,'호그스미드')
    print('After insert : ')
    print(db.selectall_employees())

    print('After update : ')
    db.update_employees(1,'정길동',35,'인천')
    print(db.selectall_employees())

    print('After delete : ')
    db.delete_employees(1)
    print(db.selectall_employees())

    del db