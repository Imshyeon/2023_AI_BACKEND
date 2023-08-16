class Vector2D:
    def __init__(self,a,b) -> None:
        super().__init__()
        self.__a=a
        self.__b=b
    def __add__(self, other):
        if isinstance(other,Vector2D):
            a_value = self.__a + other.__a
            b_value = self.__b + other.__b
        return Vector2D(a_value,b_value)
    # def __add__(self, other):
    #     a_value = self.__a + other.__a
    #     b_value = self.__b + other.__b
    #     return Vector2D(a_value,b_value)

    def __repr__(self):
        return f'Vector2D(x={self.__a},y={self.__b})'

if __name__ == '__main__':
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

'''
class Vector2D: # Vector2D 클래스 정의

    def __init__(self, x, y) -> None: # init 생성자 재정의: x, y 매개변수 2개 필요
        super().__init__()
        self.x = x
        self.y = y

    def __add__(self, other): # __add__() 메소드 재정의: + 연산자가 하는 역할 재정의
        if isinstance(other, Vector2D): # other과 self 간 동일한 지 검사
            return Vector2D(self.x + other.x, self.y + other.y) # 이제 Vector2D에서 + 연산자는 self와 other의 x와 y를 각각 더함

    def __repr__(self): # Vector2D 클래스를 어떤 문자열로 표현할 지 재정의
        return f"Vector2D(x = {self.x}, y = {self.y})" # 이제 Vector2D() 호출시 Vector2d(x = n, y = n)꼴로 출력

if __name__ == '__main__':
    vector1 = Vector2D(3, 5)
    vector2 = Vector2D(2, 7)
    result = vector1 + vector2
    print(result) # Vector2D(x = 5, y = 12)
'''