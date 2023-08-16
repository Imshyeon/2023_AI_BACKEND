import mysql.connector
from dataclasses import dataclass
@dataclass
class Lang:
    name : str
    year : int

class DBManager:
    def __init__(self,config):
        self.con = mysql.connector.connect(**config)
        self.cur= self.con.cursor()
        self.cur.execute("DROP TABLE IF EXISTS lang")
        self.cur.execute("CREATE TABLE lang(name VARCHAR(255), year INT)")

    def insert_data(self,data):
        self.cur.executemany("INSERT INTO lang(name,year) VALUES(%s, %s)",[(lang.name, lang.year) for lang in data])
        self.con.commit()

    def select_all(self):
        self.cur.execute('SELECT * FROM lang')
        result = [Lang(*row) for row in self.cur.fetchall()]
        return result

    def update_data(self,name, year):
        #year = int(year)
        self.cur.execute("update lang set name=%s, first_appeared=%s where name='C'", (name, year))
        self.con.commit()

    def __del__(self):  #소멸자 추가
        self.con.close()

if __name__ == '__main__':
    config = {
        'user': 'root',
        'password': '^Kimjml5v2!',
        'host': '127.0.0.1',
        'database': 'my_emp',
        'raise_on_warnings': True
    }
    db_manager = DBManager(config)
    data = [
        Lang("C",year=1972),
        Lang(name="Fortran", year = 1957),
        Lang(name="Python", year = 1991),
        Lang("Go",year=2009),
    ]
    db_manager.insert_data(data)
    all=db_manager.select_all()
    for row in all:
        print(row)
    # print('------------')
    # db_manager.update_data('Java', 2008)   #name C를 찾아서 각각 변경해본다.
    # all = db_manager.select_all()
    # for row in all:
    #     print(row)

