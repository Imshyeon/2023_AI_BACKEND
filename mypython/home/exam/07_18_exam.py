from dataclasses import dataclass, make_dataclass
Address = make_dataclass('Address',
                         [("name",str),
                          ("addr",str),
                          ("tel",str),
                          ("filePosition",str)],
                         namespace={
                                    "write_file" : lambda self : self._write_files(self),
                                    "_write_files" : lambda self : self.__class__._write_files(self),
                                    "read_file": lambda self: self._read_files(self),
                                    "_read_files": lambda self: self.__read__._write_files(self)
                                    })

@staticmethod
def _write_files(self):
    with open(self.filePosition, 'w') as file:
        file.write(f'이름 : {self.name}, 주소 : {self.addr}, 전화번호 : {self.tel}')

@staticmethod
def _read_files(self):
    with open(self.filePosition, 'r') as file:
        data=file.read()
    print(data)


Address._write_files = _write_files
Address._read_files = _read_files

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
    my_name = str(input('이름 : '))
    my_addr = str(input('주소 : '))
    my_tel = str(input('전화번호 : '))
    MyAddr = Address(my_name,my_addr,my_tel,'address.txt')
    MyAddr.write_file()
    MyAddr.read_file()

    # 2. 표준 input()으로 입력을 (+,-,*,/)로 받아서 사칙연산 모듈 호출해서 결과 리턴받아 calc.txt로 저장 후 읽어서 출력
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