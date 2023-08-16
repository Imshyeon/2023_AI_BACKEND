import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}

    @classmethod
    def from_dict(cls, data):  # cls인수는 클래스 자체를 참조하는 Python의 규칙
        return cls(data["name"], data["age"])


def write_objects_to_file(objects, file_path):
    data = [obj.to_dict() for obj in objects]   #객체를 Person의 to_dict()를 통해 json type으로 변환
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def read_objects_from_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return [Person.from_dict(item) for item in data]

if __name__ == '__main__':
    person1 = Person("홍길동", 30)
    person2 = Person("정길동", 35)
    persons = [person1, person2]


    write_objects_to_file(persons, "e.json")
    read_data = read_objects_from_file("e.json")

    for person in read_data:
        print(f"Name: {person.name}, Age: {person.age}")
