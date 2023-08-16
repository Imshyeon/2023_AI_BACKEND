from abc import abstractmethod, ABCMeta
class Human(metaclass=ABCMeta):
    def __init__(self,name="",age=0,height=0,weight=0):
        self.__name=name
        self.__age=age
        self.__height=height
        self.__weight=weight

    @abstractmethod
    def printInformation(self):
        # return f'name : {self.getName()} , age: {self.getAge()}, height: {self.getH()}, weight: {self.getW()}'
        pass

    def setH(self,name,age,height,weight):
        self.__name=name
        self.__age=age
        self.__height=height
        self.__weight=weight
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getH(self):
        self.__height
    def getW(self):
        self.__weight

class Student(Human):
    def __init__(self, name="",age=0,height=0,weight=0,number=0,major=""):
        super().__init__(name, age, height, weight)
        self.__number = number
        self.__major = major

    def printInformation(self):
        return print(f"name : {super().getName()} , age: {super().getAge()}, height: {super().getH()}, weight: {super().getW()}, "\
                     f"number: {self.getNum()}, major: {self.getMajor()}")


    def setS(self,number,major):
        self.__number=number
        self.__major=major
    def getNum(self):
        return self.__number
    def getMajor(self):
        return self.__major

if __name__ == '__main__':

    s1 = Student("홍길동",15,171,81,201101,"영문")
    s2 = Student("한사람", 13, 183, 72, 201102, "건축")
    s3 = Student("임걱정", 16, 175, 65, 201103, "무용")

    s1.printInformation()
    s2.printInformation()
    s3.printInformation()
