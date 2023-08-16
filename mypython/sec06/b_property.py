class My:
    def __init__(self):
        self.x = 0
    # @property   #get // 버전 낮은 경우에 써줘야 함
    def myFun(self):
        return self.x

    # @myFun.setter   #set // 버전 낮은 경우에 써줘야 함
    def myFun(self,x):
        self.x=x

######################## 클래스 외부에서 함수를 선언하고
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1  #클래스 내부에서 참조하는 방법
    def g(self):
        return 'hello world'
    h = g

if __name__ == '__main__':
    a=My()
    a.myFun = 100   #setter // 함수를 변수처럼 쓸 수 있다
    print("->",a.myFun)  #getter

    ########################
    c = C()
    y=c.g()
    print(y)
    r=c.f(3,4)
    print(r)
    k=c.h()
    print(k)