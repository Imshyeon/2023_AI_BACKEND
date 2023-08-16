from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template_string    #render_template의 태그같은 것들을 string으로..

from . import database

bp = Blueprint('user', __name__)    #지금부터 나는 blueprint고 밑에 있는 애들은 user로 생각하겠어.


@bp.route('/signup')    #user가 가지고 있는 route
def sign_up():
    return render_template('signup.html')

@bp.route('/register', methods=('GET', 'POST'))
def register(): #signup.html에서 button type="summit" 하면, 값을 user.register에게 전달 (request객체에 넣어서 보낸다)
    if request.method == 'POST':
        username = request.form['username'] #signup.html의 name 값
        password = request.form['password'] #signup.html의 name 값
        db = database.get_db()  #db -> table 생성한 객체 리턴
        user = db.execute(
            "SELECT * FROM USERS WHERE USERNAME = ?", (username,)
        ).fetchone()    #이름을 조건으로 이름과 패스워드 한줄을 리턴한다.

        if user:
            flash(f'사용자「{username}」가 이미 존재합니다.')    #메시지 플래시 표시 : 메시지를 세션에 보관
            return redirect(url_for('user.sign_up'))    #redirect: 제어권없이 그냥 페이지 전환 무조건 전환! => redirect는 request(요청)를 못가져온다.

        db.execute(
            "INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)",
            (username, generate_password_hash(password))
        )   #generate_password_hash : 내가 입력한 pw를 내부적으로 다른 걸로 바꿔서 돌아다닌다.. => 보안
        db.commit()
        return '사용자등록완료'

    return redirect(url_for('index'))

@bp.route('/login')
def log_in():
    return render_template('login.html')

@bp.route('/auth', methods=('GET', 'POST'))
def auth(): #여기에서 실제로 db에 값이 있는지 아닌지를 본다. // login은 정말 입력만 처리하고 login에 한꺼번에 넣으면 안된다.. 되게 복잡해짐
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = database.get_db()

        user = db.execute(
            "SELECT * FROM USERS WHERE USERNAME = ?", (username,)
        ).fetchone()

        if user is None:
            flash('사용자 이름이 잘못되었습니다')
        elif not check_password_hash(user['PASSWORD'], password):   #generate_password_hash에 넣었으니까 check_password_hash로 확인
            flash('비밀번호가 잘못되었습니다')
        else:
            session.pop('username', None)   #가입된 계정과 pw가 있다면 세션에 저장한다.
            session['username'] = username  #session['username'] 세션변수를 만들어 저장함. 만약 session['test']면 세션변수는 test가 됨
            return redirect(url_for('user.member')) #가입된 회원만 사용할 수 있는 화면으로 이동

    return redirect(url_for('user.log_in'))

@bp.route('/member')
def member():
    if 'username' in session:   #만약 세션변수를 session['test']로 하면 => if 'test' in session 이렇게 됨
        return  render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Member Page</title>
            </head>
            <body>
                <h1 style="font-size:2em;">Hello, {{ username }}</h1>
            </body>
            </html>
        ''', username=session['username'])  #만약 render_template을 사용한다면 {{ session['username'] }} 이렇게 해야한다.
    else:
        flash('회원 페이지에 액세스하려면 로그인하십시오')
        return redirect(url_for('user.log_in'))

@bp.route('/logout')
def log_out():
    session.clear() #session['username'] = username 이렇게하면 client가 브라우저를 떠나기 전까지는 계속 보관하고 있는데 logout을 하겠다하면 session을 clear함
    return redirect(url_for('index'))
