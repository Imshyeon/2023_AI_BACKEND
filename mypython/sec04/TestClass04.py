# 캡슐화 : 은닉된 멤버 변수에 오픈된 메소드로 값을 전달(setXX)  및  변경하고(getXX return) 리턴하는 구조
# getter & setter
class Test:
    __b=100 #객체 생성후 호출할 수 없고, Test의 멤버만 접근 가능하다.
    __nic_name__ = 'Zoe' #강한 private 이면서 의미있는 속성 ~ 객체로 호출 가능하다. 외부에서는 안된다...
    _a=200  #약한 private -> 클래스 내부에서만 사용하자. 직접 접근하지 않았으면 좋겠다. 암묵적 지시 [호출은 가능하지만 안했으면 좋겠다.]

    def _zoe(self):
        return '_zoe'

    def __zz__(self):
        return '__zz__'

    def exam(self):
        print(self._zoe(),self.__zz__())

    def __m(self): #한문자를 리턴하는 private 메소드
        return 'a'
    def k(self):
        print(self.__m(), self.__b) #같은멤버니까 자기가 자기꺼는 호출이 가능하다.


if __name__ == '__main__':
    my = Test()
    my.k()
    #print(my.__b__) #모듈에서만 공개하겠다.
    #print(my.__b)   #오류 ,,!!Test.__b
    print(dir(Test))
    print(help(Test)) #dir과 help 모두 공개가 가능한 것들만 출력. 즉, 강한 private인 변수나 함수는 출력하지 않았다.
    print(my.__nic_name__)
    print(Test.__nic_name__)

    print(Test._a)
    print(my._a)
    print(my.__zz__())
    print(my._zoe())
    #maker가 builtin으로(ex. __name__)은 가져다가 써서 확인할 수있다. 하지만 사용자가 class 안에 __한 거는 호출x