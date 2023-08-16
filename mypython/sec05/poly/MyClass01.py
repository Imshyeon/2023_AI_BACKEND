#간단한  구조의 상속을  구현해 보자.
# 이름과 나이를 관리하는  Person 클래스있다.
# Student클래스 Person을 상속을 받아 학년만 추가해서  이름, 나이, 학년을 모두 출력하는 클래스를 만들고 싶다.
'''
 1. 상속관계 : 단일상속/다중상속 확인, 기능을 확장/재정의 인지, 확인어떤거를 상속받았는지(변수, 메소드)
 2. 생성자 호출 : 값 전달하면서 생성
 3. 객체 생성
'''
import inspect
from inspect import *

class Person:
    __b = 10 #강한 private 형식은 멤버만 호출이 가능하다 후손은 호출이 불가능하다.
    def __init__(self, name, age,b): #5. 선조의 객체가 생성되면서 멤버변수에게 값전달
        self.name = name
        self.age = age
        self.__b=b
    # def personInfo(self):  #멤버변수 출력용 메소드  + 연결연산자는 시퀀스의 같은 객체끼리 연결이 가능하다. str+str
    #     return  self.name  +": (age :" +  str(self.age) +")"
    def __repr__(self):
        return f"{self.name}: (age : {self.age})"
        # return self.name + ": (age :" + str(self.age) + ")"

class Student(Person): #2
    def __init__(self,name, age, b, grade=5):#3
       # Person.__init__(self,name,age) #4 선조의 생성자
        super().__init__(name,age,b)
        self.grade = grade #6. 객체 생성 하면서 grade변수 값전달

    # def GetStudent(self):
    #     #print("b= " ,  self.__b)   #상속 관계라도 private는 호출이 불가능하다.
    #     return  self.personInfo() + ",grade :"+ str(self.grade)
    def __repr__(self):
        # return self.__repr__() + ",grade :" + str(self.grade)
        return f"{super().__repr__()}, grade : {self.grade}"

if __name__ == '__main__':
    x=Student("Ruri",7,3,5) #1.Student("Ruri",7,3) 7.생성된 선조의 주소를 리턴
    # print(x.GetStudent())
    print(x)    #Ruri: (age : 7), grade : 5
    '''
        1. 클래스 객체 확인
        2. 매개인자 확인
        3. 상속 계층 확인
    '''

    print('1. 클래스객체 확인 :', isclass(Student)) #클래스 객체 확인 => True
    print('2. 매개인자 확인 :',getfullargspec(Student))#매개인자확인
    print('3. 계층관계 확인 :',getmro(Student))#계층관계
    print('4. 모듈 확인 :',ismodule(Student))#모듈확인 => False
    print('5. 멤버 확인 :',getmembers(Student))#멤버확인