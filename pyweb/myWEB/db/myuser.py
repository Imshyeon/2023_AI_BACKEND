from app import *

def  get_all_user():
    users = User.query.all()    # class User(db.Model)
    # users = db.session.execute(db.select(User).order_by(User.name)).scalars()
    return users;

def add_user(name, age, gender, email, message):
    new_user = User(name=name, age=age, gender=gender, email=email, message=message)
    db.session.add(new_user)
    db.session.commit()

def delete_user(user_id):
    user=User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False


def update_user(user_id,name, age, gender, email, message):
    user = User.query.get(user_id)
    if user:
        user.name = name
        user.age=age
        user.gender=gender
        user.email=email
        user.message=message
        db.session.commit()
        return True
    return False