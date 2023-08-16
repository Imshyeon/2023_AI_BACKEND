import sqlite3
con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")    #이거 리턴하는게 커서다.. 한번 쓰는거니까 따로 커서 선언하지 않음

# This is the named style used with executemany():
data = (
    {"name": "C", "year": 1972},
    {"name": "Fortran", "year": 1957},
    {"name": "Python", "year": 1991},
    {"name": "Go", "year": 2009},
)#데이터가 튜플 안 dict로 ,로 나열되어있다. // list로 해도 됨
cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)
#executemany는 iterable로 넣어야하는데.. dict는 키와 밸류로 있는 말그대로 dict일뿐.. 그러니까 tuple로 감싸야한다.

# This is the qmark style used in a SELECT query:
params = (1972,)
cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params) #select을 하면서 auto commit을 하게되면서 결과 출력..
print(cur.fetchall())
con.close()
