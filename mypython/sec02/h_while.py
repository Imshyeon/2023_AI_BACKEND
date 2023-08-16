import random


def while_test():
    #난수 연습
    #난수를 10줄만 출력하고 싶다.
    #제어변수, if문 이용 ~ break
    num = 0
    while True:
        r = random.random()     #0.0 <= r < 1.0 범위의 실수 하나를 추출
        r2 = random.randint(1,10) # 1~10 사이의 정수 하나를 추출
        print(num, ':   r=', round(r, 3), '// r2=', r2)
        num += 1
        if num == 10:
            break

def while_test02():
    #10~1
    num=10
    while num > 0:
        print(num)
        num -= 1

if __name__ == '__main__':
    while_test()