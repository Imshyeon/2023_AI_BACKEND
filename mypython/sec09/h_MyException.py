import sys
class MyException(Exception):
    pass

    # def __init__(self, value) -> None:
    #     self.value=value
    # def __str__(self) -> str:
    #     return self.value + "zoe"

def raise_exception(err_msg):
    raise MyException(err_msg)  #프로그램 중단

if __name__ == '__main__':
    try:
        raise_exception("My Error12345")
    except MyException as ME:
        print("Me.args ==> ",ME.args)
        print('sys.exc_infor()==>',sys.exc_info())
        print("예외유형",sys.exc_info()[0])
        print("예외 인스턴스 객체", sys.exc_info()[1])
        print("예외에 대한 traceback = stackframe, 호출 내용", sys.exc_info()[2])
        print("예외 원래 trackback 예외 ME와 연결해서 사용하는 내용")
        print(ME.with_traceback(sys.exc_info()[2]))

