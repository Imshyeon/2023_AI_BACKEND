from com.test.MyScore import *

if __name__ == '__main__':
    my_list = [MyScore('홍길동',100,100,100), MyScore('최길동',90,90,90), MyScore('박길동',80,80,80)]
    #홍길동의 국어점수를 50으로 바꾼뒤 전체 출력
    for res in my_list:
        if res.getName() == '홍길동' :
            res.setKor(50)
            print(res)
        else :
            print(res)