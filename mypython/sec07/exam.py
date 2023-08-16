####################문제 1#######################
class Address:
    def __init__(self,name,addr,tel):
        self.__name= name
        self.__addr= addr
        self.__tel = tel

    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name

    def setaddr(self,addr):
        self.__addr = addr
    def getaddr(self):
        return self.__addr

    def settel(self,tel):
        self.__tel = tel
    def gettel(self):
        return self.__tel

    def file(self):
        with open('address.txt','w') as f:
            f.write(f'이름 : {self.__name}, 주소: {self.__addr}, 전화번호 : {self.__tel}')
        with open('address.txt', 'r') as f:
            data=f.read()
        return print(data)

def Num1():
    my_name = input(f"이름 : ")
    my_addr = input(f"주소 : ")
    my_tel = input(f"전화번호 : ")
    my_data=Address(my_name,my_addr,my_tel)
    my_data.setname(my_name)
    my_data.setaddr(my_addr)
    my_data.settel(my_tel)
    my_data.file()

####################문제 2#######################

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def calc(operator,a,b):
        operations={
            '+' : add,
            '-' : sub,
            '*' : mul,
            '/' : div
        }
        return operations.get(operator,None)(a,b)

if __name__ == '__main__':
    # 1. 이름,주소,전화번호를 표준 input()으로 입력받아서 address.txt로 저장 후 읽어서 출력한다.
    Num1()

    #2. 표준 input()으로 입력을 (+,-,*,/)로 받아서 사칙연산 모듈 호출해서 결과 리턴받아 calc.txt로 저장 후 읽어서 출력
    # 실행결과
    # input(+,-,*,/,quit) : +
    # input a : 100
    # input b : 200
    # ...
    # quit -> 저장..출력.. =>txt
    # my_file=File()
    with open('calc.txt','w') as f:
        f.write(f'')
    while True:
        my_op = input(f'\ninput operator(+,-,*,/,quit) : ')
        if my_op.lower() == 'quit':
            break
        else:
            my_a = int(input(f'input a : '))
            my_b = int(input(f'input b : '))
            data=calc(my_op,my_a,my_b)
            # print(data)
            with open('calc.txt','a') as f:
                f.write(f'{my_a} {my_op} {my_b} = {data}\n')

    with open('calc.txt','r') as f:
        my_cal=f.read()
    print(my_cal)


