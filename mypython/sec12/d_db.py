import sqlite3

con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

def insert_data(data):
    cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)
    con.commit()

def select_all():
    cur.execute('SELECT * FROM lang')
    result = cur.fetchall()
    return result

def update_data(name, year):
    #1. ADD COLUMN 해서 UPDATE하자. TYPE 때문에 오류나니까
    # cur.execute("ALTER TABLE lang ADD COLUMN year INTEGER")
    # cur.execute("update lang set name=?, year=? where name='C'",(name, year))

    #2. 타입변경해보자***
    year = int(year)
    cur.execute("update lang set name=?, first_appeared=? where name='C'", (name, year))
    con.commit()

if __name__ == '__main__':
    data = [
        {"name": "C", "year": 1972},
        {"name": "Fortran", "year": 1957},
        {"name": "Python", "year": 1991},
        {"name": "Go", "year": 2009},
    ]
    insert_data(data)
    all=select_all()
    for row in all:
        print(row)
    print('------------')
    update_data('Java', 2008)   #name C를 찾아서 각각 변경해본다.
    all = select_all()
    for row in all:
        print(row)

con.close() #close하는 순간 db자체가 사라짐..