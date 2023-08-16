class ComplexNumber:
    def __init__(self,a,b) -> None:
        super().__init__()
        self.__a=a
        self.__b=b
    def __add__(self, other):
        if isinstance(other,ComplexNumber):
            a_value = self.__a + other.__a
            b_value = self.__b + other.__b
        return ComplexNumber(a_value,b_value)
    def __eq__(self, other):
        if (self.__a == other.__a) and (self.__b == other.__b):
            return True
        return False
    # def __eq__(self, other):
    #     if self.__a==other.__a:
    #         if self.__b==other.__b:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False
    def __repr__(self):
        return f'ComplexNumber = {self.__a}+{self.__b}j'

if __name__ == '__main__':
    # [2]
    c1 = ComplexNumber(3, 2)
    # print(f'c1:{c1.__repr__()}')
    c2 = ComplexNumber(1, 4)
    # print(f'c2:{c2.__repr__()}')
    c3 = ComplexNumber(3, 2)
    # print(f'c3:{c3.__repr__()}')
    result = c1 + c2
    # print(f'result:{result.__repr__()}')
    print(result)
    print(f'c1:{c1.__repr__()},c2:{c2.__repr__()}', c1 == c2)  # False
    print(f'c1:{c1.__repr__()},c3:{c3.__repr__()}', c1 == c3, '\n')  # True
