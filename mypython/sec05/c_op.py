#__str__: 객체를 호출할 때 호출되는 자동 메소드 / __repr__
#object.__str__ : 객체클래스이름, 주소를 함께 리턴하는 기능
#object.__repr__ : 멤버 또는 출력하고싶은 서식을 사용자 서식 변환해서 리턴
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

if __name__ == '__main__':
    p1=Person("홍길동",30)
    # print(Person(), p1) #__str__이 리턴되어 출력된다.
    #                     #<__main__.Person object at 0x000001B75019E990> <__main__.Person object at 0x000001B75019E910>
    # print(Person().__str__, p1.__str__) #<method-wrapper '__str__' of Person object at 0x00000281116FE990>
    #                                     # <method-wrapper '__str__' of Person object at 0x00000281116FE910>
    #                                     #똑같이 주소 리턴

    print(p1)   #__repr__의 경우, Person(name=홍길동, age=30) 이렇게 나옴. 이런 경우에만 써라..
    print(p1.__str__)

#__getattr__ : 값의 검증을 하고 싶을 때 재정의. 즉, 유효성 검사용
#제어문(if), [사용자 예외 클래스 생성, 사용자 Error 클래스 정의로 제어.] => 유효성 검사