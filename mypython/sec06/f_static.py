
class Test:
    @staticmethod
    def get_hap(a,b):   #완전 정적. static 영역, self가 없다
        return a+b
    @classmethod
    def get_mul(self,a,b):  #자유영역 공간에서 참조됨, self가 있다.
        return a * b

    @classmethod
    def set_mul(self,a,b):
        self.a=a
        self.b=b

if __name__ == '__main__':
    print(Test.get_hap(1,2))
    print(Test.get_mul(2,3))

    #호출은 되지만 영역은 다르게 바운드 된다. Test.get_hap(2,3) 으로 생각하고 컴파일한다.
    t1=Test()
    print(t1.get_hap(2, 3)) #이렇게 부르지 않는다.
    # t1.set_mul(10,10)
    # print(t1.a, t1.b)
    # print(t1.get_mul(t1.a, t1.b))