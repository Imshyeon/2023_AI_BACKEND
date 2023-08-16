class U:
    x = 10  #static
    def __init__(self,a,x) -> None:     # -> None : 아무것도 리턴 안하겠다.
        #super().__init__()
        self.a=a  #self.__a=100    #self는 키워드가 아니다.
        self.x=x    #non-static

    # def __str__(self) -> str:   #객체를 호출할때 자동으로 호출..
    #     return "내꺼"

    
if __name__ == '__main__':
    u1 = U(1,20)    #__new__ -> __init__[object->U]
    print(u1.a, u1.x,U.x) #1 20 10
    print(u1)   #u1.__str__() --> 현재 객체의 주소를 리턴(object 메소드가)
                #<__main__.U object at 0x000001CBF019E810>