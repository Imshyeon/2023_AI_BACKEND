import sqlite3
from dataclasses import dataclass
@dataclass
class Lang: #생성자, 소멸자, 연산자 재정의 메소드, __repr__ 지가 알아서 해줬음.
    name : str
    first_appeared : int

class LangDB:
    def __init__(self):
        self.con = sqlite3.connect(":memory:")
        self.cur = self.con.execute("CREATE TABLE lang(name text, first_appeared integer)")

    def insert_data(self,data):
        self.cur.executemany("INSERT INTO lang VALUES(?, ?)",[(lang.name, lang.first_appeared) for lang in data])
        self.con.commit()

    def select_all(self):
        self.cur.execute('SELECT * FROM lang')
        result = [Lang(*row) for row in self.cur.fetchall()]
        return result

    def update_data(self,name, year):
        #year = int(year)
        self.cur.execute("update lang set name=?, first_appeared=? where name='C'", (name, year))
        self.con.commit()

    def __del__(self):  #소멸자 추가
        self.con.close()

if __name__ == '__main__':
    data = [
        Lang("C",1972),
        Lang(name="Fortran", first_appeared = 1957),
        Lang(name="Python", first_appeared = 1991),
        Lang("Go",2009),
    ]   #객체라서 이렇게.. Lang 클래스에 넣어야되니까 이렇게 넣는것이 맞다!
    lang_db = LangDB()
    lang_db.insert_data(data)
    all=lang_db.select_all()
    for row in all:
        print(row)
    print('------------')
    lang_db.update_data('Java', 2008)   #name C를 찾아서 각각 변경해본다.
    all = lang_db.select_all()
    for row in all:
        print(row)

    # del lang_db