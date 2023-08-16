#page 173.
def prn(a=10, *res, **mydict):  #(일반 데이터 변수,,,, *변수, **변수) -> 선언순서, 단일변수(*, **)
    "00000000000000"
    print(a,"\t", res,'\t', mydict)

if __name__ == '__main__':
    #선언 -> dir() -> help -> 사용법
    #선언 -> dir() G확인 -> help 특성 -> 사용법[내장 속성 = 컴파일 속성값]
    # .py-> .pyc -> 컴파일 속성값 확인
    prn(1,(2,3),[4],'5',6, b=123, d=(4,5,6), y='37', k=[3,3,3])
    print(prn.__code__,type(prn.__code__))  #<code object prn at 0x0000019D7C1F0F30, file "C:\pywork\mypython\sec03\b_function.py", line 2>
                                            # <class 'code'>
    print(prn.__name__)                     #prn
    print(prn.__defaults__)                 #(10,)
    print(prn.__doc__)                      #00000000000000
    print(prn.__class__)                    #<class 'function'>
    print(prn.__globals__)
    print('----------------')
    res=prn.__code__
    print(dir(res))
    print('\n-------co_---------')
    print(f'res.co_name: {res.co_name}')    #prn
    print(f'res.co_argcount: {res.co_argcount}')    #1
    print(f'res.co_nlocals: {res.co_nlocals}')      #3
    print(f'res.co_varnames: {res.co_varnames}')    #('a', 'res', 'mydict')
    print(f'res.co_code: {res.co_code}')
    print(f'res.co_names: {res.co_names}')          #('print',)
    print(f'res.co_filename: {res.co_filename}')    #C:\pywork\mypython\sec03\b_function.py
    print(f'res.co_flags & 0x04: {res.co_flags & 0x04}')
    print(f'res.co_flags & 0x08: {res.co_flags & 0x08}')
    print(f'res.co_flags & 0x20: {res.co_flags & 0x20}')