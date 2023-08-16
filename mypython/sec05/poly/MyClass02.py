#super() : 선조 클래스를 의미한다. 명시적으로 후손 클래스에서 선조의 변수나 메소드를 참조할때 사용한다.
#후손클래스에서 후손이 가진 값을 선조 클래스의 생성자를 호출해서 대입하려면 super()키워드를 사용한다.
from inspect import *

class AA:
    def __init__(self):
        print("나 AA 생성자 ")
    def my_DD(self):
        print("-------> AA'myDD()")

class DD:
    def __init__(self):
        print("나 DD 생성자 ")
    def my_DD(self):
        print("-------> DD'myDD()")

class BB(AA,DD):
    def __init__(self):
        # super().__init__() #선조의 기본 생성자를 호출
        AA.__init__(self)
        DD.__init__(self)
        print("나 BB 생성자 ")
    def my_DD(self):
        AA.my_DD(self)
        DD.my_DD(self)

if __name__ == '__main__':
    #a1 = AA()  #생성자를 호출하면서 객체가 생성되면 자유영역공간 메모리 할당된다.
    b1=BB()  # AA()  <- BB() 선조가 생성 된후  후손이 생성
    b1.my_DD() #재정의, AA's myDD()가 나옴
    '''
    => 결과
    나 AA 생성자 
    나 DD 생성자 
    나 BB 생성자 
    -------> AA'myDD()
    -------> DD'myDD()  
    '''


    print('계층관계:',getmro(BB))
    #계층관계: (<class '__main__.BB'>, <class '__main__.AA'>, <class '__main__.DD'>, <class 'object'>)
