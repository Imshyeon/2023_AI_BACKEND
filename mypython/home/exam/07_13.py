from MyCalc import *
#from MyCalc import MyCalc
'''
1.변수 설정 : 생성자
2.변수 getter&setter
3.계산함수
4.출력함수
5.소멸자 재정의
'''
if __name__ == '__main__':
    a=100
    b=200
    #조건1
    m1=MyCalc(a,b)
    print(m1)   #m1.__repr__이 리턴
    print('=============')
    #조건2
    m2=MyCalc()
    print(m2)
    print('=============')
    #조건3
    m1.setA(500)
    print(m1)
    print('=============')
    m2.setA(40000)
    print(m2)
    #---원래는..
    # print(f'{m2.getA()}+{m2.getB()} = {m2.getHap()}')
    # print(f'{m2.getA()}+{m2.getB()} = {m2.getSub()}')
    # print(f'{m2.getA()}+{m2.getB()} = {m2.getMul()}')
    # print(f'{m2.getA()}+{m2.getB()} = {m2.getDiv()}')