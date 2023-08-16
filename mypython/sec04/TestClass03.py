#__class__ : 인스턴스가 자신을 생성한 클래스 객체를 참조하기 위하여 파이선에서 제공하는 키워드로 클래스영역(heap)에
# 모든 인스턴스 객체에  있는 데이터를 참조하거나 수정할 때 사용한다.
'''
사원 번호    7월 영업실적
a111          850   a1
b111          750   b1
c111          650   c1
Emp 라는 클래스를 만들어서  변수를 2개 선언한 후  a1,b1,c1의 이름으로 객체를 생성한 다음 값을 전달 후 출력 해 보자.
'''

class Emp:
    empno =0
    result=0
if __name__ == '__main__':
    a1=Emp()
    a1.empno ='a111'
    a1.result =850
    print(a1.empno, a1.result)  #a111 850

    b1=Emp()
    b1.empno ='b111'
    b1.result = 750
    print(b1.empno , b1.result) #b111 750

    c1=Emp()
    c1.empno='c111'
    c1.result= 650
    print(c1.empno, c1.result)  #c111 650
    print(Emp.empno, Emp.result)    #0 0

    #클래스 이름을 찾을 때 사용.
    print(Emp.__name__, type(a1.__class__) , b1.__class__ , c1.__class__)
    #Emp <class 'type'> <class '__main__.Emp'> <class '__main__.Emp'>
    print(a1, b1, c1)
    #<__main__.Emp object at 0x00000239C753E950> <__main__.Emp object at 0x00000239C753EB50> <__main__.Emp object at 0x00000239C753EC90>

    d1= a1
    print(a1,d1.empno, d1.result)   #<__main__.Emp object at 0x00000239C753E950> a111 850
