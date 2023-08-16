# 1. 1~100을 1줄에 10개씩 출력
#    1.1 제어문만 이용하여 작성(시퀀스 자료형 사용안함)
import random


def q1_1():
    print('==pattern==')
    for i in range(1,101,10):
        cnt=1
        pattern =""
        if cnt == 10:
            cnt = 0
        else :
            pattern += f'{i} {i+1} {i+2} {i+3} {i+4} {i+5} {i+6} {i+7} {i+8} {i+9}'
            print(f'{pattern}')
            cnt += 1

#    1.2 시퀀스 자료형을 이용하여 작성(list 내장)
def q1_2():
    print('\n==list==')
    for i in range(1,101,10):
        cnt=1
        if cnt == 10:
            cnt=0
        else:
            mylist=f'{i} {i+1} {i+2} {i+3} {i+4} {i+5} {i+6} {i+7} {i+8} {i+9}'
            print(mylist)
            cnt+=1

# 2. 1~n 까지의 합을 출력 하는 프로그램(제어문 사용)
def q2():
    numbers=int(input('숫자입력 : '))
    result=0
    for num in range(1,numbers+1,1):
        result += num
    print(result)

# 3. 1~n 까지 짝수합과 홀수합을 출력하는 프로그램(제어문 사용)
def q3():
    numbers = int(input('숫자입력 : ')) #5
    even = 0  #2,4 =6
    odd = 0   #1,3,5=9
    for num in range(1,numbers+1):
        if num == numbers+1:
            break
        else :
            if num%2 == 0:
                even += num
            elif num%2 != 0:
                odd += num
    print(f'짝수합 : {even}, 홀수합: {odd}')

# 4. 1~n 까지 3의 배수와 5의 배수를 제외한 수의 합을 출력하는 프로그램(제어문 사용)
#10 => 1,2,4,7,8 => 22
def q4():
    numbers = int(input('numbers: '))
    num=1
    result = 0
    while True:
        if num == numbers:
            break
        else:
            if (num%3==0) | (num%5==0):
                pass
            else:
                result += num
                print(num, result)
        num += 1
    print(f'합 : {result}')

# 5. 구구단표 출력 프로그램
# 5.1 제어문만 이용하여 작성(시퀀스 자료형 사용안함)
def q5_1():
    gugu = 1
    print(f'gugu * i = 값')
    while True:
        if gugu == 10:
            break
        else:
            for i in range(1,10):
                print(f'{gugu} * {i} = {gugu*i}', end='\t')
            print()
        gugu += 1

# 5.2 리스트와 제어문을 이용하여 작성
def q5_2():
    gugu = 1
    GUGU= []
    print(f'[gugu i 값]')
    while True :
        if gugu == 10:
            break
        else :
            for i in range(1,10):
                GUGU += [[gugu,i,gugu*i]]

        gugu += 1
    print(GUGU)

# 6.
def q6():
    m_up=0
    m_down=0
    even=0
    odd=0
    while True:
        numbers = int(input('numbers: '))
        if numbers == -999:
            m_down += 1
            break
        else:
            if numbers > 0:
                m_up += 1
                if numbers%2==0:
                    even += 1
                else:
                    odd += 1
            else :
                m_down += 1
    print(f'[양수 개수 : {m_up}, 짝수 개수 : {even}, 홀수 개수 : {odd}], 음수 개수 : {m_down}')

# 7.
def q7():
    g = {1: '+', 2: '-', 3: '*', 4: '/'}
    while True:
        num1 = input('num1: ')
        num2 = input('num2: ')
        G = int(input('연산(1:+, 2:-, 3:*, 4:/) : '))
        if G == 0:
            break
        result = eval(num1+g[G]+num2)
        print('{0} {2} {1} = {3}'.format(num1,num2,g[G],result))

if __name__ == '__main__':
    # q1_1()
    # q1_2()
    # q2()
    # q3()
    # q4()
    # q5_1()
    # q5_2()
    # q6()
    q7()
