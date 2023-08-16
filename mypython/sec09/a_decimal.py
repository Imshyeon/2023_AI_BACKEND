import decimal
from decimal import * # 부동소수점 정밀도 계산하는 모듈
#부동 소수점 정밀도 -> 부동소수점 숫자는 이진수로 표시 / 특정 소수점을 2진수로 표시가 안되는 경우가 발생한다.
#(90.7+30.2)+0.0002, print(120.9) -> 부동 소숫점 반올림 오류 (120.90020000000001)

def case01():
    res = Decimal("90.7") + Decimal("30.2") + Decimal("0.0002")
    print(res,type(res))    #120.9002 <class 'decimal.Decimal'>
    print(1/3)              #0.3333333333333333

    print(decimal.getcontext()) #부동소수점 환경설정값을 출력, Context라는 클래스로 속성 리턴
    decimal.getcontext().prec=3
    a, b = Decimal("1"), Decimal("3")
    print(a/b)  #0.333
    a, b = Decimal("5"), Decimal("7")
    print(a / b)    #0.714
    # print(Decimal("5")/Decimal("7"))
    '''
    
    c = Context(prec=28, Emin=-425000000, Emax=425000000,
       ...             rounding=ROUND_HALF_EVEN, capitals=1, clamp=1,
       ...             traps=[InvalidOperation, DivisionByZero, Overflow],
       ...             flags=[])
    '''
    c=Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-425000000, Emax=425000000, capitals=1, clamp=0, flags=[],\
            traps=[InvalidOperation, DivisionByZero, Overflow])
    decimal.setcontext(c)
    print(decimal.getcontext())
    print(decimal.ExtendedContext)#normal한거 하나 보여줌... 이렇게 설정할래? 라는 느낌
    decimal.setcontext(decimal.ExtendedContext)
    print(decimal.getcontext())

if __name__ == '__main__':
    case01()