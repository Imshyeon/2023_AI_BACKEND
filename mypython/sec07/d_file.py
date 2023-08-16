import json
from typing import Callable, Any


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class MyEncoder(json.JSONEncoder):  #JSONEncoder : 자기 형식인지 아닌지 확인. -> key:value를 만들어줌
    def default(self, o: Any) -> Any:   #자동호출이 되면서 main에서 [객체주소, 객체주소]를 받아서 -> line 14
        if isinstance(o,Person):
            return {"name" : o.name, "age" : o.age} #key값은 Person의 self.name으로 맞출 필요가 없다.. key를 직접 만드는 거니까
                                                    #{key : value}를 만들어서 리턴해준다.
        return super().default(o)

def my_json_write():    #쓰기
    p1 = Person("aaaaaaa", 15)
    p2 = Person("bbbbbbb", 18)
    data = [p1, p2]  # 주소가 넘어온다. json은 {key:value}로 줘야함
    print(data)
    with open('d.json', 'w') as file:
        json.dump(data, file, indent=4, cls=MyEncoder)

def My_decoder(obj):
    return Person(obj["name"], obj["age"])

if __name__ == '__main__':
   #파일을 읽어온다. d.json
   with open('d.json','r') as file:
       data=json.load(file,object_hook=My_decoder)  #object_hook에는 함수를 줘야함
   print(data)

   for item in data :
       # print(item, type(item))
       print(f"name: {item.name}, age:{item.age}",type(item))