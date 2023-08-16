import sqlite3
from dataclasses import dataclass

@dataclass
class Lang: #생성자, 소멸자, 연산자 재정의 메소드, __repr__ 지가 알아서 해줬음.
    name : str
    year : int

#Register adapter for Lang class
#1.
# sqlite3.register_adapter(Lang, lambda lang:(lang.name, str(lang.year)))
#2.
def adapt_lang(lang):
    return lang.name, lang.year
sqlite3.register_adapter(Lang, adapt_lang)  #여기서 한대로 타입을 해줬으면 좋겠다.


con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")    #타입 지정 안함

def insert_data(data):
    for lang in data:
        cur.execute("INSERT INTO lang VALUES(?, ?)",(lang.name,lang.year))
    con.commit()
def select_all():
    cur.execute('SELECT * FROM lang')
    # result = [Lang(*row) for row in cur.fetchall()] 이렇게 줘도 되긴한다..
    result = cur.fetchall()
    return result

def update_data(name, year):
    cur.execute("update lang set name=?, first_appeared=? where name='C'", (name, year))
    con.commit()

if __name__ == '__main__':
    data = [
        Lang("C",1972),
        Lang(name="Fortran", year = 1957),
        Lang(name="Python", year = 1991),
        Lang("Go",2009),
    ]   #객체라서 이렇게..

    insert_data(data)
    all=select_all()
    for row in all:
        print(row)
    print('------')
    update_data('Java', 2008)   #name C를 찾아서 각각 변경해본다.
    all = select_all()
    for row in all:
        print(row)