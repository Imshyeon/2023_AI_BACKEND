class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        new_value = self.value + other.value
        return MyClass(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return MyClass(new_value)

class Vector2D:
    def __init__(self,a,b) -> None:
        super().__init__()
        self.__a=a
        self.__b=b
    def __add__(self, other):
        a_value = self.__a + other.__a
        b_value = self.__b + other.__b
        return Vector2D(a_value,b_value)
    def __repr__(self):
        return f'Vector2D(x={self.__a},y={self.__b})'

class ComplexNumber:
    def __init__(self,a,b) -> None:
        super().__init__()
        self.__a=a
        self.__b=b
    def __add__(self, other):
        a_value = self.__a + other.__a
        b_value = self.__b + other.__b
        return ComplexNumber(a_value,b_value)
    def __eq__(self, other):
        if self.__a==other.__a:
            if self.__b==other.__b:
                return True
            else:
                return False
        else:
            return False
    def __repr__(self):
        return f'ComplexNumber = {self.__a}+{self.__b}j'

class Matrix:
    def __init__(self,a=[]) -> None:
        super().__init__()
        self.__a=a
    def __add__(self, other):
        a_mat = []
        for i in range(len(other.__a)):
            a_row = []
            for j in range(len(other.__a[i])):
                a_value = self.__a[i][j] + other.__a[i][j]
                a_row.append(a_value)
            a_mat.append(a_row)
        return Matrix(a_mat)
    def __repr__(self):
        return f'Matrix(rows={self.__a})'

if __name__ == '__main__':
    obj1 = MyClass(100)
    obj2 = MyClass(200)

    result = obj1 + obj2
    final_result = result - MyClass(50)

    print(final_result.value)   #결과 : 250
    # (MyClass(100)+MyClass(200)-MyClass(50))

    #번외로 많이 해보기--
    #[1]
    vector1 = Vector2D(3,5)
    vector2 = Vector2D(2,7)
    result = vector1 + vector2
    print(result,'\n')
    # vector3 = Vector2D(1, 2)
    # vector4 = Vector2D(3, 4)
    # result2 = vector3 + vector4
    # print(result2, '\n')
    # Vector2D(x=5,y=12)라고 출력되게 작성. __add__, __repr__, __init__ 사용

    #[2]
    c1 = ComplexNumber(3,2)
    # print(f'c1:{c1.__repr__()}')
    c2 = ComplexNumber(1,4)
    # print(f'c2:{c2.__repr__()}')
    c3 = ComplexNumber(3,2)
    # print(f'c3:{c3.__repr__()}')
    result = c1 + c2
    # print(f'result:{result.__repr__()}')
    print(result)
    print(f'c1:{c1.__repr__()},c2:{c2.__repr__()}', c1==c2 ) #False
    print(f'c1:{c1.__repr__()},c3:{c3.__repr__()}', c1==c3 ,'\n') #True

    # [3]
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])
    result_addition = matrix1 + matrix2
    print("Result:")
    print(result_addition)   #결과   ===> Matrix(rows=[[8, 10, 12], [14, 16, 18]])