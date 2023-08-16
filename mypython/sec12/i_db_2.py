import sqlite3
from dataclasses import dataclass

@dataclass
class Lang:
    name : str
    year : int

def adapt_lang(lang):
    return lang.name, lang.year
def convert_lang(value):
    return Lang(*value)

con = sqlite3.connect(":memory:",detect_types=sqlite3.PARSE_DECLTYPES| sqlite3.PARSE_COLNAMES)
sqlite3.register_adapter(Lang, adapt_lang)
sqlite3.register_converter("lang",convert_lang)
cur=con.cursor()
cur.execute("CREATE TABLE lang(name TEXT, first_appeared INTEGER)")    #타입 지정 안함

def insert_data(data):
    for lang in data:
        cur.execute("INSERT INTO lang VALUES (?,?)",(lang.name, lang.year))
    con.commit()

def select_all():
    cur.execute('SELECT * FROM lang')
    # result = [Lang(*row) for row in cur.fetchall()] 이렇게 줘도 되긴한다..
    result = cur.fetchall()
    return [Lang(name=row[0],year=row[1]) for row in result]

def update_data(name, year):
    cur.execute("update lang set name=?, first_appeared=? where name='C'", (name, year))
    con.commit()

if __name__ == '__main__':
    data = [
        Lang(name="C",year=1972),
        Lang(name="Fortran", year = 1957),
        Lang(name="Python", year = 1991),
        Lang(name="Go",year=2009),
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