#page 121.
class Person:   #object 클래스가 Person의 선조
    def __init__(self,name,age,addr):   #생성자
        self.name=name
        self.age=age
        self.addr=addr
        print("------>init")
        
    def __new__(self,name,age,addr):
        print("------>new")
        instance=super().__new__(self)  #opject 클래스의 new에다가 현재 값을 올려서 생성.
        return instance

p=Person('길동',10,'서울')     #객체 생성 : __new__ (객체 생성) -> __init__ (객체 초기화) 
#object.attribute
print(p.name, p.age, p.addr)

print(dir(p))
print(p.__dict__)   #속성을 dict라는 데이터타입으로 리턴

#__dict__: 객체의 네임 스페이스, 속성의 dict
#object.attribute, getattr(), setattr() 를 통해 동적으로 access 하기 편함

p1=Person('길동02',20,'서울02') #객체 생성 : __new__ (객체 생성) -> __init__ (객체 초기화) 
print(id(p),id(p1))
#new 호출 -> init으로 멤버 변수 초기화

