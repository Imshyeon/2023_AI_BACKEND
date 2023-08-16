import inspect
import pprint


class AA:
    def my_method(self):
        print("AA's my_method")
class BB:
    def my_method(self):
        print("BB's my_method")
class CC(AA,BB):    #메모리에는 다 올라감
    def my_method(self):
        # super(AA,self).my_method() #얘는 좀 모호하다..(다중상속의 경우)
        AA.my_method(self)
        BB.my_method(self)
class DD:
    pass

if __name__ == '__main__':
    c1=CC()
    c1.my_method() # 실제 상속받으면 BB로 재정의 되서 BB's my_method가 나옴
    print(CC.__mro__)  # (<class '__main__.CC'>, <class '__main__.AA'>, <class '__main__.BB'>, <class 'object'>)
    print(CC.mro())  # [<class '__main__.CC'>, <class '__main__.AA'>, <class '__main__.BB'>, <class 'object'>]
    print(c1.__class__)  # <class '__main__.CC'>
    print(isinstance(c1, AA))  # True
    print(isinstance(c1, BB))  # True
    print(isinstance(c1, CC))  # True
    print(isinstance(c1, DD))  # False
    print(issubclass(CC, BB))  # True
    print(issubclass(CC, AA))  # True
    print(CC.__bases__)  # (<class '__main__.AA'>, <class '__main__.BB'>) == 바로 위의 상위클래스 목록
    print(inspect.getmro(CC))   #(<class '__main__.CC'>, <class '__main__.AA'>, <class '__main__.BB'>, <class 'object'>)

    pp=pprint.PrettyPrinter(indent=4)
    pp.pprint(inspect.getclasstree([CC]))
    '''
    [   (<class '__main__.AA'>, (<class 'object'>,)),
    [(<class '__main__.CC'>, (<class '__main__.AA'>, <class '__main__.BB'>))],
    (<class '__main__.BB'>, (<class 'object'>,)),
    [(<class '__main__.CC'>, (<class '__main__.AA'>, <class '__main__.BB'>))]]
    '''

