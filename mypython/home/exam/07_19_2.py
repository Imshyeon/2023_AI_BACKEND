#numpy
import numpy as np
import random
#한개의 주사위를 360번 던져서 3의 배수의 눈이 나오는 회수를 구하는 것을 1000 번하고,
# 1000개를  x =[] 라는 변수에 넣고  x에 대한 평균, 분산, 표준편차를 구하자.
def Test():
    dice = [1,2,3,4,5,6] #주사위 생성
    x =[]
    for j in range(1,1001): #1000번 반복수행
        cnt =0;
        for i  in range(1,361):#360번 반복 수행
            result  = random.choice(dice) #주사위에서 눈을 하나 출력해서 result에 담는다.
            if result % 3 == 0:# 그 주사위의 눈을 3으로 나눈 나머지 값이  0이면
                cnt +=1  #cnt를 1씩 증가시키겠다
        x.append(cnt) #  주사위를 360번 던져서 3의 배수가 나온 횟수가 x리스트에 추가 된다.

    print(np.mean(x))
    print(np.var(x))
    print(np.std(x))
if __name__ == '__main__':
    Test()
#몬테 카를로 알고리즘 / 베르누이 확률