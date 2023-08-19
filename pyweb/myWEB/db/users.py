from flask import g

def get_db():
    if "db" not in g:  # db속성이 있는지 확인
        from app_db2_sqlite import get_db
        return get_db()

def get_all_users():
    db = get_db()
    cur = db.execute("SELECT * FROM users")
    users = cur.fetchall()
    return users

def add_user(name, age, gender, email, message):
    db = get_db()
    db.execute(
        "INSERT INTO users (name, age, gender, email, message) VALUES (?,?,?,?,?)",
        (name, age, gender, email, message)
    )
    db.commit()