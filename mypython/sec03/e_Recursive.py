'''하노이탑 알고리즘 만들어볼까?'''


def fibonacci(n):
    print(f'---------{n}')
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def recursive_sum(numbers):
    '''목록의 합'''
    print(f'========={numbers}')
    if len(numbers)==0:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])
        # 0+10=10
        # 10+9 = 19
        # 19+8=27
        # 27+7 = 34
        # 34+6 = 40
        # 40+5 = 45
        # 45+4 = 49
        # 49+3 = 52
        # 52+2 = 54
        # 54+1 = 55

def recursive_string(string):
    '''문자열 반전'''
    print(f'========={string}')
    if len(string) <= 0:
        return string
    else:
         return recursive_string(string[1:])+string[0] #문자열 반전
        #
        # return string[0]+recursive_string(string[1:]) 문자열 그대로

if __name__ == '__main__':
    print(fibonacci(5))
    numbers=[1,2,3,4,5,6,7,8,9,10]
    print(recursive_sum(numbers))
    string='abcdefg'
    print(recursive_string(string))