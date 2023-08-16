class MyClass:
    def __init__(self, name):
        self.name=name
    def __repr__(self):
        return f"MyClass(name = '{self.name}')"

if __name__ == '__main__':
    '''
    1.
    obj1 = MyClass("Object 1")
    obj2 = MyClass("Object 2")
    obj3 = MyClass("Object 3")
    my_list=[obj1, obj2, obj3]
    
    '''

    #2.
    my_list=[MyClass("Object 1"), MyClass("Object 2"), MyClass("Object 3")]
    #만일 객체 중 Object 1의 이름이 있다면 홍길동으로 변경하자.
    for obj in my_list:
        if obj.name == "Object 1":
            obj.name = '홍길동'
            print(f'find object : {obj}')
        else :
            print(f'other object : {obj}')

    '''
    => 결과
        find object : MyClass(name=홍길동)
        other object : MyClass(name=Object 2)
        other object : MyClass(name=Object 3)
    '''