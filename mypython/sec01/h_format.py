#page 40.
#print("출력서식")

import datetime #날짜 시간 모듈

def case01():
    #정수, 실수, 문자열 각 10자리씩 확보해서 출력해보자
    #pass    #블럭 코드에서 명령어 아무것도 안하고싶을 때 그냥 패스
    print("%10d %5d"%(100, 200)) # 전체 정수 10자리 확보 후 정수 출력 ,5 자리 확보 후 200 출력 (공백도 같이 출력되는 걸 잊지 말자)
    print("%-5d %5d %-5.1f"%(1,2,3.14)) 
    print("%-10s : %10s"%('aaaaa','bbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    ##정수, 8진수, 16진수 출력
    print("%d %o %x %5f"%(100, 100, 100, 3.14)) # 소수점 기본 정밀도(6) 자리가 출력
    
    print('--------------------------')
    print("%10d"%(100))
    print("%010d"%(100))
    print("%-10d"%(100))
    print("%.2f"%(3.141592))
    print("%10.2e"%(3.141592))
    print("%d / %d = %.2f"%(5,3,5/3))
    print('--------------------------')
    
def case02():
    #str's format : S.format(*args, **kwargs) -> str(return)
    print('{0} {1}'.format('apple',7.77))
    print('{1} {0}'.format('apple',7.77))
    print('{0} {0}'.format('apple',7.77))
    print('{0:10s} {1:<10f}'.format('apple',7.77))
    print('{0:<10} {1:5.2f}'.format('apple',7.77)) # < 왼쪽 정렬 // > 오른쪽 정렬
    print('{0:>10} {1:5.2f}'.format('apple',7.77))
    print('{0:=^10}'.format('hi'))
    
    
def case03():
    #str.format() 정수 활용
    num=42
    f="the number is {}".format(num)
    print(f)
    
def case04():
    #str.format() 실수 활용
    pi=3.141592
    f="the number is {:.2f}".format(pi)
    print(f)
    
def case05():
    #str.format() zero padding 활용
    num=42
    f="the number is {:0<10d}".format(num)
    print(f)
    
def case06():
    #str.format() 16진수 활용
    num=42
    f="the binary is {:x}".format(num)
    print(f)
    
def case07():
    #날짜서식
    date = datetime.date(2023,7,7)
    f="Date : {:%y-%m-%d}".format(date)
    print(f)
    
    
def case08():
    #tuple -> * : 0 or more..라서
    point=(1,2,3,4)
    f="Point:(  {},{},{},{}   )".format(*point)
    print(f)
    
def case09():
    #사전형 dict **
    person={'name':'홍길동', 'age77':20}
    f="Person:(  Name:{name}, Age:{age77}  )".format(**person)  #dict는 키 값으로 한다...
    print(f) 
    
def case10():
    # 인수 위치
    f="{0} {2} {1}".format(1,2,3)
    print(f)    
    
#case01()
#case02()
#case03()
#case04()
case05()
case06()
case07()
case08()
case09()
case10()