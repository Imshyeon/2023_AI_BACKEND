from com.test.Calc import Calc

if __name__ == '__main__':
    # 1.
    # c1 = Calc(100,50)
    # print(c1)

    # 2.
    mlist =[Calc(100,50),Calc(200,150),Calc(300,250)]
    #a의 값이 100인 값을 찾아서 777로 바꾼 후 출력.
    for res in mlist:
        if res.get_a() == 100:
            res.set_a(777)
            print(res)
        else:
            print(res)
    print('\n\n')
    #b의 값이 150인 값을 찾아서 888로 바꾼 후 출력하자.
    for res in mlist:
        if res.get_b() == 150:
            res.set_b(888)
            print(res)
        else:
            print(res)
