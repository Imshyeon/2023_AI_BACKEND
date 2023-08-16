class Calc:
    def __init__(self, a, b):
        self.__a = a  # 멤버변수를 현재 Calc안에는 메소드에만 공개하겠다. 멤버에게만 공개하겠다.  private 하겠다.
        self.__b = b

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def set_b(self, b):  # __b 의 값만 변경하고 싶은 욕망의 메소드를 선언  = 멤버변수의 값전달 및 변경
        self.__b = b

    def set_a(self, a):  # __a 의 값만 변경하고 싶은 욕망의 메소드를 선언  = 멤버변수의 값전달 및 변경
        self.__a = a

    def get_hap(self):
        return self.__a + self.__b

    def get_sub(self):
        return self.__b - self.__a

    def get_mul(self):
        return self.__a * self.__b

    def get_div(self):
        return self.__b / self.__a

    def __repr__(self):
        string = f"===========================================\n"
        string += f"{self.get_a():>5d} + {self.get_b():>5d}  = {self.get_hap():>5d}\n"
        string += f"{self.get_b():>5d} - {self.get_a():>5d}  = {self.get_sub():>5d}\n"
        string += f"{self.get_a():>5d} * {self.get_b():>5d}  = {self.get_mul():>5d}\n"
        string += f"{self.get_b():>5d} / {self.get_a():>5d}  = {self.get_div():>5.1f}"
        return string
