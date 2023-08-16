# https://flask.palletsprojects.com/en/2.3.x/quickstart/#html-escaping
from flask import Flask , render_template   # render_template: template으로 이동
from markupsafe import escape
from func import test   #분할된 app 객체가 있는 모듈 추가. func이 가지고 있는 test 모듈 추가
from func import test01


# 명령페이지를 제어하는 Controller -> app.py
app = Flask(__name__)   #플라스크 웹을 시작하겠다. 객체를 생성

app.register_blueprint(test.app)    # 분리된 모듈 app 명을 선언한다.
app.register_blueprint(test01.app)

@app.route("/")
def index():
    my_dict = {}
    my_dict ['name'] = 'hong-gil-dong'
    my_dict ['age'] = 30
    return render_template('index.html',message=my_dict) #templetes 하위의 index.html로 감


if __name__ == '__main__':
    app.run(host='localhost', port = 8000, debug= True)   #실행
    # debug : flask 스타트, debug 모드 on, detail..--
    # debug=False 면 *Restarting with stat같은 디테일이 나오지 않음...
    # * Serving Flask app 'app' : app.py
    # * Debug mode: on
    # *Restarting with stat
    # *Debugger is active!
    # *Debugger PIN: 135 - 019 - 003
    # *Detected change in 'C:\\pywork\\pyweb\\F_web\\app.py', reloading
    # *Restarting with stat
    # *Debugger is active!
    # *Debugger PIN: 135 - 019 - 003
#     ----------------------------------
# debug=False라도 print 됨.
# 127.0.0.1 - - [07/Aug/2023 10:57:15] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [07/Aug/2023 10:57:24] "GET /hello HTTP/1.1" 200 -

