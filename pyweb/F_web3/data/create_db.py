import sqlite3

def main():
    con = sqlite3.connect('users.db')
    con.execute("DROP TABLE IF EXISTS USERS")
    con.execute("CREATE TABLE USERS (\
        USERNAME TEXT PRIMARY KEY UNIQUE NOT NULL, \
        PASSWORD TEXT NOT NULL)"
    )
    #primary key = unique + not null 이지만 sqlite는 언급하라는 게 있어서 언급함

if __name__ == '__main__':
    main()