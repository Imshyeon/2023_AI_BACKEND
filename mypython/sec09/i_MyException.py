class MyException(Exception):
    pass    #클래스는 생성자를 언급하지 않으면 기본 생성자를 사용함.
            #상속을 할 때는 선조의 생성자를 꼭 보라
            #Exception의 생성자 : __init__(self, /, *args, **kwargs)
def myPrn(a,b):
    if b == 0:
        raise MyException("0이자너")
    return a/b
if __name__ == '__main__':
    try:
        res=myPrn(1,0)
        print(res)
    except MyException as e:
        print('Error :',str(e))