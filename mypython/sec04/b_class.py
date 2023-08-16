from typing import Iterable

class My:

    def __init__(self) -> None:
        #super().__init__()  #객체를 선조 생성(object를 먼저 메모리에 올림) -> 후손 생성(My)
                             #super~를 적던 안적던 메모리 올림. 그래서 주석해도 상관없다
        print('My__init')

if __name__ == '__main__':
    m1 = My()   #My class의 __new__()를 통해 동적할당 객체를 생성하면서 __init__()를 호출한다.
                #__init__()은 뭐라도 채움. 그리고 __new__()와 __init__()은 더이상 호출되지 않음

    m2 = My()   #My class의 __new__()를 통해 동적할당 객체를 생성하면서 __init__()를 호출한다.
    print(id(My),id(m1),id(m2)) #선언된 클래스의 id값,  m1,  m2 => 각각의 아이디가 다름