from functools import partial   #부분함수(=함수분할)
                                #부분으로 나눠서 빠르게 실행을 하기 위해서

#함수의 원본
def power(base, exponent):
    return base ** exponent #제곱

def multiply(a,b):
    return a*b

if __name__ == '__main__':
           # partial(func, *args, **keywords) : 부분함수
           # args : tuple of arguments to future partial calls
           # func : function object to use in future partial calls
           # keywords : dictionary of keyword arguments to future partial calls
    square = partial(power, base=2)     #func : power , keywords : base = 2
    print(square)       #functools.partial(<function power at 0x000001CBBD8904A0>, base=2)
    result = square(exponent=3)
    print(result)       #8
    #----------------------------------
    my_partial = partial(multiply,5)    #부분함수 생성 a=5 // func : multiply, arg : 5
    result = my_partial(3)  #b=3 // 이때 원래 함수를 호출하게 된다.
    print(result)       #15
