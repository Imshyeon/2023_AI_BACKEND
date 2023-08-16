# for문, while문
# range(stop): 기본값으로 start는 0, step은 1
# range(start, stop): 기본값으로 step은 1
# range(start, stop-1, step)
def forTest():
    print(' 1~n까지 1씩 증가하면서 모두 출력하는 프로그램')
    print('사용자에게 정수 1개를 입력받아 n에 대입하여 작성!')
    n = int(input('정수 입력: '))
    for x in range(1, n+1, 1):
        print('x =', x, end='\t')

def forTest01():
    print('문자열 반복')
    text="Hello Python!!"
    for ch in text:
        #print(ch,' (',ord(ch),')',end='\t')  #H (ascii code)
        print(f'{ch} ({ord(ch)})', end='\t')

def forTest02():
    print('최대수 찾기')
    numbers=[3,7,2,5,9,10]
    max_num = numbers[0] #비교값
    for num in numbers:
        if num > max_num:
            max_num = num
    print('max_number : ', max_num)

def forTest03():
    print('factorial')
    num=5
    factorial = 1
    for i in range(1,num+1,1):
        factorial *= i
        print(i,factorial)
    print('factorial of ',num,'is : ', factorial)

def forTest04():
    #dict
    student_scores = {"a" : 100, "b" : 90, "c" : 80}
    #dict에서 key로 value를 리턴, ,
    #items() -> key, value로 분할
    for name, score in student_scores.items():
        print(f'name : {name}, score : {score}', end='\t')

    #keys() -> list => value 찾기, values() -> list => value
    #해보기
    # KV = list(student_scores.keys())
    # VT = list(student_scores.values())
    # print('\n',KV[0], type(VT))
    # for k in KV:
    #      print(f'name : {k}, score : {k}',end='\t')

def forTest05():
    #tuple
    coordinates=[(1,2),
                 (3,4),
                 (5,6),
                 (7,8)]   #x=(1,3,5,7)  y=(2,4,6,8)
    for x, y in coordinates:
        print(f'x= {x}   y= {y}')

def forTest06():
    #구구단
    #1~9까지 임의의 단을 입력받아 구구단을 출력
    num = int(input('단을 입력하시오(1~9): '))
    for i in range(1,10):
        print(f'{num}*{i}={num*i}')

def forTest07():
    #1~100까지 출력
    #짝수를 출력, 개수를 출력하자
    cnt=0
    for i in range(1,101):
        if i%2 == 0:
            print(f'{i}',end='\t')
            cnt+=1
    else:
        print('\n')
        print(f'cnt={cnt}')
def forTest08():
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
def forTest08():
    #1+2+3+4+~ = hap    // 번외편 (1+2)*3 + (4+5)*6 ...
    hap=0
    for i in range(1,101):
        #1. hap
        if i==100:
            print(f'{i}=',end='\t')
        else:
            print(f'{i}+',end='\t')
        hap += i


    print(f'{hap}')

def forTest09():
    #소수확인
    num=int(input('숫자입력 : '))
    for i in range(2,num):
        if num % i ==0 :
            print(num, 'is not a prime number')
            break
        else:
            print(num, 'is a prime number')

def forTest10():
    #(1+2)*(3+4)
    result = 1
    pattern = ""

    for start in range(1,100,2):
        pair_sum= start + (start+1)
        result*=pair_sum
        pattern += f'({start}+{start+1})*'

    pattern = pattern[:-1]
    pattern += ' ='
    print('pattern: ',pattern, result)

def forTest11(): #(1+2*3) + (4+5*6)
    result=0
    pattern=""

    for start in range(1,100,3):
        pair=start+(start+1)*(start+2)
        result += pair
        pattern += f'({start}+{start + 1}*{start + 2}) + '

    pattern = pattern[:-3]
    pattern += ' ='
    print('pattern: ',pattern, result)

if __name__ == '__main__':
    # forTest()
    # print()
    # forTest01()
    # print()
    # forTest02()
    # print()
    # forTest03()
    # print()
    # forTest04()
    # print()
    # forTest05()
    # print()
    # forTest06()
    # print()
    # forTest07()
    # print()
    # forTest08()
    # print()
    # forTest09()
    # print()
    # forTest10()
    # print()
    forTest11()