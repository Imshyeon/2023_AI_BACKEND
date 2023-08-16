#app에서 나누자!
from flask import g
from flask import Flask

def get_db():
    if "db" not in g:  # db속성이 있는지 확인
        from app_db4 import db
        return db
def get_user():
    db=get_db()
    if "User" not in g:
        from app_db4 import Model as User
        return User

def get_all_user():
    db = get_db()
    User=get_user()

    users  = User.query.all()   # class User(db.Model):
    #users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return users

def add_user(name, age, gender, email, message):
    db = get_db()

    new_user  = User(name=name, age=age,gender=gender, email=email, message = message)
    db.session.add(new_user)
    db.session.commit();

def delete_user(user_id):
    db = get_db()

    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

#user.html <a href="{{url_for('edit_user', user_id=user.id)}}" class="btn btn-danger">Edit</a>
#수정할 내용의 ID로 한 줄의 레코드를 찾아서 리턴
def get_user_by_id(user_id):
    db = get_db()

    user=User.query.get(user_id)
    return user

def update_user(user_id, name, age, gender, email, message):
    db = get_db()

    user = User.query.get(user_id)
    if user:
        user.name = name
        user.age = age
        user.gender  = gender
        user.email  = email
        user.message  = message
        db.session.commit()
        return True
    return False