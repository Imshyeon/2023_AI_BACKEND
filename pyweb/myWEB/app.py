from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from db import myuser

app = Flask(__name__)
# 1. db 세팅
app.config['SECRET_KEY'] = "dev"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myweb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 2. 인스턴스 객체가 프로젝트 객체로 전달되어 세팅
db = SQLAlchemy(app)

# 3. db 모델을 생성한다.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)

# #4. 데이터 베이스 생성 , 테이블생성
# def init_db():
#     with app.app_context():
#         db.create_all()

# # 5. 데이터 베이스 실행
# @app.cli.command("init-db")
# def init_db_command():
#     init_db()


@app.route("/users")
def show_users():
    users_data = myuser.get_all_user()   # db모듈에서 호출되는 메소드
    return render_template("users.html", users=users_data)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        email = request.form["email"]
        message = request.form["message"]
        myuser.add_user(name, age, gender, email, message) # db모듈에서 호출되는 메소드
        return redirect(url_for("show_users"))
    return render_template("add_user.html")

@app.route("/")
def index():
    return render_template("index.html")

#
# def  get_all_user():
#     users = User.query.all()    # class User(db.Model)
#     # users = db.session.execute(db.select(User).order_by(User.name)).scalars()
#     return users;
#
# def add_user(name, age, gender, email, message):
#     new_user = User(name=name, age=age, gender=gender, email=email, message=message)
#     db.session.add(new_user)
#     db.session.commit()
#
# def delete_user(user_id):
#     user=User.query.get(user_id)
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         return True
#     return False
#
#
# def update_user(user_id,name, age, gender, email, message):
#     user = User.query.get(user_id)
#     if user:
#         user.name = name
#         user.age=age
#         user.gender=gender
#         user.email=email
#         user.message=message
#         db.session.commit()
#         return True
#     return False

if __name__ == '__main__':
    app.run(debug=True)
