from functools import singledispatch    #함수의 overloading을 만드는데 사용하는 것.(변수만 다르게 해서 출력)
#https://docs.python.org/3/library/functools.html => functools
@singledispatch #1. @가 만들어지는 얘한테 single~을 건다.
def my_data(data):
    print("Error")

@my_data.register   #function의 decorator로 참조해서 타입으로 찾아감  => 얘의 목적은 overload
def a(data : int, t : int):    #data를 int만 받음
    print("int",data,t)
@my_data.register
def b(data : str,t:int):
    print("str",data,t)
@my_data.register
def c(data : list):
    print("list",data)

if __name__ == '__main__':

    my_data(10,100)
    my_data("abc",7)
    my_data([1,2,3])
    my_data(90.9)