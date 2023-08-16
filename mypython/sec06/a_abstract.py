#추상클래스 : abc.py/ dataclasses.py / collections.abc(https://docs.python.org/3/library/collections.abc.html#module-collections.abc)
#https://docs.python.org/3/glossary.html#term-abstract-base-class
#강제추상화
from abc import abstractmethod, ABCMeta
#abc는 추상클래스와 추상메소드를 사용하겠다...

'''
    추상메소드를 가진 클래스는 추상 클래스가 되고 객체 생성 불가능. 후손을 위한 추상 메소드를 가진다.
    추상클래스는 반은 만들어져 있고 반은 설계되어있다. 따라서 따로 변수나 메소드 등을 줄 수 있다.
    
    1. 선조가 가진 추상 메소드를 후손이 재정의하지 않으면 객체를 생성할 수 없다.
    2. 재정의 하지 않는 후손은 추상 클래스가 된다.
'''
#추상클래스
class Base(metaclass=ABCMeta):  # 난 객체 생성 안하는 추상 클래스. 단, 후손에게 강제로 추상메소드를 재정의 시킨다.

    #추상화 @을 함수 위에 지정할 수 있다. => 메소드로 후손을 제어.
    @abstractmethod #추상메소드
    def start(self):
        print('Base Start') #pass

    @abstractmethod
    def stop(self):
        print('Base Stop')  #pass

class Cat(Base):
    def start(self):
        print('Cat Start')
    def stop(self):
        print('Cat Stop')

class Duck(Base):
    def start(self):
        print('Duck Start')
    def stop(self):
        print('Duck Stop')

class Puppy(Base):
    def start(self):
        print('Puppy Start')
    def stop(self):
        print('Puppy Stop')

def my_class(m : Base): #나 Base 아니면 안쓰겠다 // 동적바인딩 : 선조의 시작 주소로 후손을 제어할 수 있도록 만듦.
    print(m)
    m.start()
    m.stop()

if __name__ == '__main__':
    my_class(Cat())
    my_class(Duck())
    my_class(Puppy())

    my_class(Cat())
    my_class(Cat())
    # my_class(Base()) #Can't instantiate abstract class Base with abstract methods start, stop