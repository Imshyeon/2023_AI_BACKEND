import mysql.connector
def conTest01() :
    config = {
      'user': 'root',
      'password': '^Kimjml5v2!',
      'host': '127.0.0.1',
      'database': 'my_emp',
      'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)

    cnx.close()

def conTest02():
  import mysql.connector

  cnx = mysql.connector.connect(user='root', password='^Kimjml5v2!',
                                host='127.0.0.1',
                                database='my_emp')
  cnx.close()

def conTest03():
  from mysql.connector import (connection)

  cnx = connection.MySQLConnection(user='root', password='^Kimjml5v2!',
                                   host='127.0.0.1',
                                   database='my_emp')
  cnx.close()

def conTest04():
  import mysql.connector
  from mysql.connector import errorcode

  try:
    cnx = mysql.connector.connect(user='scott',
                                  database='employ')
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()

if __name__ == '__main__':
    conTest04()