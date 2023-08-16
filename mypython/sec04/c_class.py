class S1:
    a=1

if __name__ == '__main__':
    sa=S1()
    sb=S1()
    print(f'sa.a : {sa.a}, sb.a : {sb.a}')  #sa.a : 1, sb.a : 1
    sa.a = 100  #sa.a에 값 전달
    print(f'sa.a : {sa.a}, sb.a : {sb.a}')  #sa.a : 100, sb.a : 1
    print(f'S1.a : {S1.a}') #클래스 영역에 있음. // S1.a : 1
    sb.a = 20
    print(f'sa.a : {sa.a}, sb.a : {sb.a}')  #sa.a : 100, sb.a : 20
    print(f'S1.a : {S1.a}') #S1.a : 1


    '''
    S1.b=2
    S1.c=100
    print(S1.a, S1.b)
    print(S1.__name__)
    print(help(S1))
    print(dir(S1))
    del S1.a, S1.b, S1.c    #원래 멤버였던 a도 지울 수 있다.
    print(help(S1))
    '''
