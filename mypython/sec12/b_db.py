import sqlite3
import datetime

#connect() -> 데이터 베이스에 연결
# ":memory:" -> 특수 문자열, 실제 데이터베이스가 디스크의 실제 파일이 아닌 RAM에 생성 및 저장된다.
#detect_types -> 데이터 유형을 제어하는 처리 방법
#sqlite3.PARSE_DECLTYPES : sqlite3 모듈이 CREATE TABLE 문에서 선언된 유형을 기반으로 열의 데이터를 자동 감지(가상으로 만들어지는 거니까)
#                          create table test(  ), 제약조건도 앎. 테이블과 관련된 것 앎.
#sqlite3.PARSE_COLNAMES : 열의 유형을 자동 감지 , date와 timestamp 감지.
#                         date라고 선언하게 되면 sqlite3의 date 타입으로 처리한다.

#date, timestamp으로 선언을 하게 되면 python의 datetime모듈의 객체로 관리된다.(내장이라서)

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = con.cursor() #커서는 :memory:를 db라고 생각하지 않음(.db가 아니니까) 그래서 detect_types를 적어주는 것.
cur.execute("create table test(d date, ts timestamp)")#date와 timestamp는 함수임..sqlite가 제공해준다

today = datetime.date.today()
now = datetime.datetime.now()

cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
cur.execute("select d, ts from test")
row = cur.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
row = cur.fetchone()
print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))

con.close()