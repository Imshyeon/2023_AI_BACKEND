import traceback
from datetime import datetime
import csv
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
    #################Data를 json형식으로
        data=[[current_time,error_message,current_time]]    #엑셀이니까

        filename=f'traceback_{current_time}.csv'
        with open(filename,'w',newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print(f'정보 {filename}')

        # csv 파일을 로드해서 화면에 출력
        with open(filename,newline='') as file:
            my_csv = csv.reader(file, delimiter=' ', quotechar='|')
            for row in my_csv:
                print(' '.join(row))