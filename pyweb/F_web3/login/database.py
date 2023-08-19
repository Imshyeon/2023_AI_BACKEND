import os
import sqlite3

from flask import current_app, g
#g : global로 db의 패스나 데이터베이스 있는 곳 갖고오기

def get_db():
    if 'db' not in g:
        # 현재 스크립트의 위치를 기반으로 DATABASE 경로 설정
        #os.path.abspath(__file__) : 자기자신
        print(current_app)
        # db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'users.db')
        db_path = current_app.config['DATABASE']
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
        print(db_path)
    return g.db


def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    # db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'users.db')
    db_path = current_app.config['DATABASE'] #current_app : 전체적으로 실행을 해야지 그게 잡힌다..
    # print("db_path : ", db_path)
    # get_db()