'''
    4칙 연산을 한 후에 {}로 선언해서 선택구문
'''
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    hap = a + b
    return hap
def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b
def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b
def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b
def choose_menu():
    print('input?')
    print('add, sub, mul, div, quit')   #키 값을 나열
    return input('choice : ')
if __name__ == '__main__':
    menu = {'add': add, 'sub': subtract, 'mul': multiply, 'div': divide}
    choice = choose_menu()  #키 값을 입력
    while choice != 'quit':
        if menu.get(choice):    #dict의 키로 값을 찾아온다
            x = input('first value : ')
            y = input('second value : ')
            print(menu[choice](int(x), int(y))) #함수 실행=****=
            choice = choose_menu()