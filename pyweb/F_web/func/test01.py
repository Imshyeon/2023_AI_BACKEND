from flask import Flask, render_template # app 생성, 페이지 이동
from flask import Blueprint # 분할된 app를 선언
from markupsafe import escape
import numpy as np

app = Blueprint('test01',__name__)

'''
@app.route("/testfor01")
def testfor01():
    return render_template('testfor01.html')
'''


'''
동적 페이지 생성
1. 변수 사용 url/<><>
2. 함수인수에 변수 전달 
3. render_template('testfor01.html', 변수추가 ,변수명=변수)
    *변수의 유형 : string, int, float, path, uuid( 128bit => 16진수, 4비트씩 끊어서 전달하는 방법 )
'''

# '''
# 동적페이지-1
@app.route("/<cat><dog>")
def testfor01(cat='Cat',dog='Dog'):
    return render_template('testfor01.html',cat=cat,dog=dog)
# '''
# '''
# 동적페이지 -2
@app.route("/<page>")
def testfor02(page):
    return render_template('testfor02.html', page=escape(page))
# '''