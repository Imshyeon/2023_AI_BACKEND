from flask import Flask, render_template # app 생성, 페이지 이동
from flask import Blueprint # 분할된 app를 선언
from markupsafe import escape
import numpy as np

app = Blueprint('test',__name__) # 분할될 app 객체 생성 (모듈명 혹은 폴더명, __name__), func(폴더명)안에 있는 blueprint야..

# 분할하고자하는 라우터들을 놓는다.
#url 라우터
@app.route('/hello')
@app.route('/hello/<name>') #http://localhost:8000/hello/zoe
def hello_world(name=None):
    return render_template('hello.html',name=name)

@app.route("/test/<name>")   # /<string:name> 이렇게 준 거랑 똑같다
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/testfor")
def testfor():
    num_list = np.arange(10)
    return render_template('testfor.html', message=num_list)
