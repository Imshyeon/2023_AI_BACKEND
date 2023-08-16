#int 클래스를 상속받아 기능을 확장하자
class MyInt(int):
    #기능확장 : 홀짝을 판별하는 bool
    def is_even(self):
        return self%2==0
    def is_odd(self):
        return self%2!=0
    def squard(self):
        return self**2

if __name__ == '__main__':
    '''
    선조 int의 생성자.
    int([x]) -> integer
    int(x, base=10) -> integer // base는 진법
    '''
    my_number=MyInt(10) #int(x, base=10) -> integer
    print(f'Is even? {my_number.is_even()}')
    print(f'Is odd? {my_number.is_odd()}')
    print(f'Squard : {my_number.squard()}')