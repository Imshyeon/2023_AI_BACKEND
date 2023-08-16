def forTest():
    #1+2+3+4+~ = hap    // 번외편 (1+2)*3 + (4+5)*6 ...
    hap=0
    for i in range(1,101):
        #1. hap
        # if i==100:
        #     print(f'{i}=',end='\t')
        # else:
        #     print(f'{i}+',end='\t')
        if i==98:
            print(f'({i}+{i+1})*{i+2}=',end='\t')
            break
        else:
            print(f'({i}+{i+1})*{i+2} +', end='\t')
        #1. hap += i
        hng = (i+(i+1))*(i+2)

    print(f'{hng}')

if __name__ == '__main__':
    forTest()