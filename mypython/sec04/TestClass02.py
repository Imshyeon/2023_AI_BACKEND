#이름 , 주소 , 전화 번호를 관리하는 Address 라는 클래스를 선언해서 변수로 값을 저장해 보자
# 정적 변수  static 변수   [클래스.멤버변수] => 클래스 변수
# python에서는 static 이라는 키워드가 없다. 객체 앞에 static을 줄 수 없으니까
# const도 안된다. 그래서 python에서는 완벽한 상수가 없다.(decimal.ROUND_DOWN)
# 관례적으로, math.pi
class Address:
    name="Dominica"
    addr = "seoul"
    tel ="02-0000-000"
    def prn(self):  # 멤버 메소드
        print(Address.name, Address.addr, Address.tel)

if __name__ == '__main__':
    print(Address.name, Address.addr, Address.tel)  #정적으로 먼저 실행
                                                    #Dominica seoul 02-0000-000
    Address.name ="1111111111111"
    print(Address.name, Address.addr, Address.tel)  #1111111111111 seoul 02-0000-000
#-------생성된 객체
    a1 = Address()
    a1.prn()    #1111111111111 seoul 02-0000-000


