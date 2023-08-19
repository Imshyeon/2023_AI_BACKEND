import pathlib
from flask import Flask
from . import database, user  #import database [.parent.parent 쓸 때는..]  // from login import 해도 된다.
from .user import bp as user_bp
# from datetime import timedelta
# from flask import session

def create_app():
    #pathlib.Path(__file__) : 현재 위치
    # instance_path = pathlib.Path(__file__).parent.parent / 'data'
    instance_path = pathlib.Path().resolve()/'data'

    app = Flask(
        __name__,
        instance_path=instance_path,  # 절대 경로 지정 추가.
        instance_relative_config=True   # 상대 경로 설정도 읽을 수 있다.
    )
    app.config.from_pyfile('config.py') #app.config가 세팅 및 업데이트 됨
    app.teardown_appcontext(database.close_db)  # 현재 웹이 종료하게 되면 데이터베이스 클로즈 하자. ,process 마무리 되는 시점에서 db.close

    #환경설정 다 끝나고 나면, 함수 안에 함수 호출해서 index..
    @app.route('/')
    def index():
        # from datetime import timedelta
        # from flask import session
        # session.permanent = True
        # app.PERMANENT_SESSION_LIFETIME = timedelta(seconds=30)
        # session['text'] = "abcde"
        return '<h1> Index Page </h1>'


    app.register_blueprint(user_bp)  # User Blueprint 추가    // 만약 from .user 없다면 user.bp 해도 된다..
    return app


if __name__ == '__main__':
    app = create_app()  #flask 그 자체
    app.run()

'''
[기본 config]

from flask import Flask
app = Flask(__name__)
app.config
<Config {'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'SECRET_KEY': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>
'''