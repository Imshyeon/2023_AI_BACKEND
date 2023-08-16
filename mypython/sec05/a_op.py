#객체간의 연산[산술, 관계, 비교] -> 사용자 객체 정렬 을 구현하는 재정의 메소드
class MyClass:

    def __init__(self,value) -> None:
        self.value = value
    def __add__(self,other):
        return self.value + other
    def __sub__(self, other):
        return self.value - other
    def __radd__(self,other):
        return other+self.value
    #---ex
    def __gt__(self, other):
        return self.value > other.value
    def __lt__(self, other):
        return self.value < other.value

obj=MyClass(5)  #숫자 하나 관리하는 클래스
# result = obj+3   #obj+3 이렇게 하고싶다..
# print(result) #8
# result = obj-2
# print(result) #3
# #---------------------
# result=10+obj
# print(result) #15

#---ex
# res=obj > 10
# print(res)

obj01 = MyClass(10)
res=obj>obj01
print(res)  #False
res=obj<obj01
print(res, type(res))   #True
#(MyClass(5)+MyClass(10)-MyClass(20))