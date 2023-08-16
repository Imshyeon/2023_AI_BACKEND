def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def calculate(operator, a, b):
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    return operations.get(operator, None)(a, b) #add(a,b)

if __name__ == '__main__':
    while True: #무한루프
        operator= input('Enter a op ( +  -  *  / ) or quit ')
        if operator.lower() =='quit':  #입력된 모든 값을 소문자로 변형후 =='quit'
            break
        a = int(input('a :'))
        b = int(input('b :'))

        result  = calculate(operator, a,b)
        print(result)

