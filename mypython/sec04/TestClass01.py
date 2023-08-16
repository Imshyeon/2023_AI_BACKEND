#[Step 01:  클래스 선언 ]
class Test: # object의  후손 클래스가 되어 선조의 메소드들을 참조하고 있다.    object <- Test
    def empty(self):    #메소드
       self.data = []   #빈 리스트 객체 선언

    def add(self, x):
       self.data.append(x)  #리스트에 요소를 추가하겠다.

if __name__ == '__main__':
#[Step 02:  클래스 객체 생성  ]
    my01 = Test()
    my02 = Test()

#[Step03 :  멤버 호출]
    my01.empty()    #각각의 빈 리스트 생성
    my02.empty()    #빈 리스트 생성
    for  i in range(1,6):   #my01에다가 요소를 1~5까지 append
        my01.add(i)

    #list 객체를 출력해본다
    print(my01.data)    #[1, 2, 3, 4, 5]
    print(my02.data)    #빈 list // []
    print(my01, my02)   #주소가 다름. = 다른 객체
    my03= my01          #my03이라는 객체 변수에 my01주소를 대입해서 얕은 카피를 했다, 같은 공간을 참조한다.
    print(my03.data)    #my01 동일한 값 // [1, 2, 3, 4, 5]
    print(my01, my03)   #각 주소를 호출해본다. 같은 주소가 나온다. 왜?
    print(id(my01), id(my03))

