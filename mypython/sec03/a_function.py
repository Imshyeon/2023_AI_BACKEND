x = 10  #G
y = 11
def foo():
    x = 20    #foo 함수의 L에 해당, bar 함수의 E에 해당
    print(f"foo's x={x} at {id(x)} ")

    def bar():
        a=30
        print(a, x, y)
    bar()   #내 방에서는 내거가 우선순위이다..
    x=40
    print(f"foo's x={x} at {id(x)} ")
    bar()

def test():
    print(f"test's x={x} at {id(x)} ")


if __name__ == '__main__':
    #1~100 출력, 100줄 출력 -> 반복문 -> 함수(기능 = 메시지) -> class -> 상속 -> 다형성 -> 모듈 -> 패키지 -> 프로젝트
    #   -> 배포

    foo()
    test()