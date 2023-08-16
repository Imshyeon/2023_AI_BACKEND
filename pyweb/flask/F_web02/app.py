from flask import Flask,render_template
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydb"
mongo = PyMongo(app)

class User:
    def __init__(self,name,age,gender,email,message):
        self.name=name
        self.age=age
        self.gender = gender
        self.email=email
        self.message=message

#########CRUD
def add_user(name,age,gender,email,message):
    new_user=User(name,age,gender,email,message)
    mongo.db.users.insert_one(new_user.__dict__)

def get_all_users():
    return list(mongo.db.users.find({}))

@app.route("/users")
def show_users():
    user_data=get_all_users()
    return jsonify(user_data)

@app.route("/result")
def home_page():
    online_users = mongo.db.Score.find({ })
    return render_template("result.html",online_users=online_users)

if __name__ == '__main__':
    app.run()