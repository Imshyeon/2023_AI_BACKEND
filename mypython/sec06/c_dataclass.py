from dataclasses import dataclass, make_dataclass, field
#__init__ / __repr__ 을 편하게 하기 위해서..

@dataclass  #init, repr, eq 도 됨.
class Person:   #db 표현법
    name : str  #이 타입으로만 get,set. 기능형 메소드랑 연동할 수 있다.
    age : int
#################################################################3
#line 20-24(make_dataclass)과 같은 내용
# @dataclass
# class C:
#     x: int
#     y: 'typing.Any'
#     z: int = 5
#
#     def add_one(self):
#         return self.x + 1
#

C = make_dataclass('C', #make_dataclass는 함수. 이 함수 안에 init, repr, eq 등이 있다(도움말 참고).
                    [('x', int),    #field ==> tuple[str,type]
                    'y',            #field ==> str
                    ('z', int, field(default=5))],  #field ==> tuple[str,type,Field]
                    namespace={'add_one': lambda self: self.x + 1}) #namespace : dict[str,Any]
'''
def make_dataclass(cls_name: str,
                   fields: Iterable[str | tuple[str, type] | tuple[str, type, Any]],
                   *(0 or more),
                   bases: tuple[type, ...](상속) = ...,
                   (sec06)namespace: dict[str, Any] | None = ...,
                   init: bool(True) = ...,
                   repr: bool = ...,
                   eq: bool = ...,
                   order: bool = ...,
                   unsafe_hash: bool = ...,
                   frozen: bool = ...) -> type

'''

if __name__ == '__main__':
    p1= Person('홍길동',20)
    p2 = Person('최길동', 30)
    print(p1.name, p2.age)  #홍길동 15
    print(p1)   #Person(name='홍길동', age=20)

    #make_dataclass
    c=C(1,'python') #C(x=1, y='python',z=5)
    print(c.x)  #1
    print(c.add_one())  #2
    print(c)    #C(x=1, y='python', z=5)