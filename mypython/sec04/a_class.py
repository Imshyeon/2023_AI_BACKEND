#class a1(builtins.object)
#class 후손(선조클래스명 object) : pass

#dir(object)
#object : class의 CRUD기능, 클래스의 정보(__class__, __doc__, __str__,__new__, __getattr__,,), 오브젝트 연산(__ge__,__ne__,,)
#a1 a, b1 b => a > b인가? ~ gt, eq, ge,,,
class a1:   #class a1(object) :
    pass

class b1:   #class b1(object) :
    pass

if __name__ == '__main__':
    print(id(a1))   #객체 생성은 안했으나(pass) 자료형은 있음.
    print(id(b1))
    print(dir(a1)) #object로 상속받은 메소드들이 존재한다.
    print(help(a1))