# 정수형 변수 a,b 를 관리하는 클래스를 만들어 보자. 단 캡슐화로 구현 해보자.
# 은닉된 멤버 변수에게  setxx으로 값 전달 및 변경하고   getxx return 메소드로 리턴하는 구조
class Test:
    # __a=0  #주소 히든 private 초기값은 생성자에서 대입 혹은 이렇게 직접 주거나..
    # __b=0

    #여기 안에다가 초기화를 해준다. 엄밀히 말하면 외부에서 값을 받지 않음. 그럴때는 처음부터 이렇게 되어있다.
    def __init__(self) -> None:
        super().__init__()
        self.__a=0
        self.__b=100

    #name ="abc"   def setName():~~
    def setA(self, a):
        self.__a =a  # 객체 생성후 값을 a 로 전달받아  멤버__a 에게 값전달 및 변경
    def getA(self):
       return self.__a

    def setB(self,b):
        self.__b=b
    def getB(self):
        return self.__b

if __name__ == '__main__':
    t1 = Test()
    # t1.setA(100)
    print(t1.getA())    #0
    # t1.setB(200)
    print(t1.getB())    #100

    #t1.setA(100)와 t1.setB(200)을 주석처리하고, def __init__을 주면 출력은 0 100이 나온다.
    #read only만 하면 누군가는 값을 적어줘야한다. 초기화를 안해주면 python은 None을 할당한다.
    #def __init__과 명시적(__a=0,__b=0)을 주석처리하고 출력하면 100 200이 나온다.