import mysql.connector     #sqlite3 CRUD -> class로 변형 / 입출력 객체를 생성해서 사용한다.
from dataclasses import dataclass

@dataclass
class Employee:
    id : int
    name : str
    age : int
    city : str
    #init, repr 자동생성, get과 set 할 수 있다.

class EmployeeDB:
    def __init__(self):
        config= {
            'user': 'root',
            'password': '^Kimjml5v2!',
            'host': '127.0.0.1',
            'database': 'my_emp',
            'raise_on_warnings': True
            }
        self.conn=mysql.connector.connect(**config)
        self.cursor=self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS my_employees")
        self.cursor.execute(
            '''
            CREATE TABLE my_employees(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(50) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(50) NOT NULL
            )
            '''
        )
        self.conn.commit()

    def insert_employees(self, employee : Employee):
        self.cursor.execute('insert into my_employees (name, age, city) values (%s,%s,%s)'
                            ,(employee.name, employee.age, employee.city))
        self.conn.commit()

    def selectall_employees(self):  #def test(a,b,*tupletype, **dicttype) ... test(1,2,3,4)
        self.cursor.execute('select * from my_employees')
        rows = self.cursor.fetchall()   #[여러 개의 행을 튜플로 리턴]
        return [Employee(*row) for row in rows] #한 줄씩 리턴. => rows[('헤르미온느',25,'호그와트'),(),()]
                                                #Employee(*row) : row 각 튜플에서 값을 압축 해제하고 클래스 생성자에게 인수로 전달한다.
                                                #데이터베이스에서 리턴된 튜플의 목록(list)에서 Employee 객체 목록으로 변환해서 리턴한다.

    def update_employees(self, employee : Employee):
        self.cursor.execute('update my_employees set name=%s, age=%s, city=%s where id =%s '
                            ,(employee.name, employee.age, employee.city, employee.id))
        self.conn.commit()

    def delete_employees(self, id):
        self.cursor.execute('delete from my_employees where id =%s',(id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    db= EmployeeDB()
    db.insert_employees(Employee(None,'헤르미온느',25,'호그와트'))
    db.insert_employees(Employee(None,'해리포터',25,'그린고트'))
    db.insert_employees(Employee(None,'시리우스 블랙',40,'호그스미드'))
    print('After insert : ')
    print(db.selectall_employees())

    print('After update : ')
    db.update_employees(Employee(1,'정길동',35,'인천'))
    print(db.selectall_employees())

    print('After delete : ')
    db.delete_employees(1)
    print(db.selectall_employees())
