class A:
    def __init__(self) -> None: #()매개인자 없는 생성자. 기본생성자(default constructor)
        super().__init__()  #super는 object
                            #super() : 선조의 멤버를 엑세스하기 ㄴ위한 키워드

    def f(self):    #클래스의 멤버함수원형을 선언하면 () 첫 매개인자(hidden)는 현재 오브젝트를 지칭하는 연산자가 된다.
        print('A class')

    def f02(self):  #self는 키워드는 아니고 심볼로써 현재 오브젝트를 지칭하는 연산자.
        print('A class f02')

class B(A): #클래스 A의 속성을 모두 상속받는다.
    def __init__(self) -> None: #()매개인자 없는 생성자. 기본생성자(default constructor)
        super().__init__()  #new(hidden), init(객체를 생성할 때 호출됨, init은 최소 (정수 크기의) 메모리 확보)
                            #B의 super는 A

    def prn(self):
        super().f() #상속을 받았기 때문에 f()를 명시 및 구현하지 않아도 호출할 수 있다.
                    #생성을 따로 안하고 호출을 할 수 있다.
                    #A().f()    a1=A(); a1.f()

    def f(self):    #재정의(override) : 외부에서 봤을 때 A의 f를 히든시켰다(덮어쓰기).
                    #                  하지만 B 입장에서 봤을 땐  A의 f를 볼 수 있다. 따라서 super().f()로 다시 호출 가능.
        print('B class')

class MyClass:
    def __add__(self, x):
        print('add {} called.'.format(x))
        return x

if __name__ == '__main__':
    # a1 = A()
    # a1.f()  #A class
    # b=B()
    # b.f()   #현재 self의 주소 참조로 선조 A의 클래스의 멤버를 내 것처럼 호출할 수 있다.
    # b.f02()     #f02
    # b.prn()     #A class

    b1=B() #A()->B()
    b1.f()

    a=MyClass()
    print(a+3)  #+는 add를 부른다.
                #'abc' + 'def' => str class + str class
                # ↑ 그 선조나 object의 __add__