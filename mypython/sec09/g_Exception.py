import traceback
from datetime import datetime
import json

def f1(a,b):
    return f2(a) + f2(b)

def f2(x):
    return 1.0/x

if __name__ == '__main__':
    try:
        f1(1.0, 0.0)
    except (ZeroDivisionError,IOError) :
        now = datetime.now()  # 현재 시간 객체 생성 now()
        current_time = now.strftime("%Y-%m-%d_%H-%M-%S")  # 포맷 패턴을 생성
        error_message = traceback.format_exc()  # 에러의 정보를 문자열로 리턴 받는다.
    #######Data를 json 형식으로
        data={"timestamp" : current_time,
              "err_msg" : error_message}

        filename=f'traceback_{current_time}.json'
        with open(filename,'w',newline="") as file:
            json.dump(data, file,indent=2)

        print(f'정보 {filename}')
