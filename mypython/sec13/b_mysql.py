import mysql.connector
def my_conn() :
    config = {
      'user': 'root',
      'password': '^Kimjml5v2!',
      'host': '127.0.0.1',
      'database': 'my_emp',
      'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)
    print(cnx)
    return cnx

def select_All(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM emp")    #return 없이 실행되는 구문이다.
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    select_All(my_conn())