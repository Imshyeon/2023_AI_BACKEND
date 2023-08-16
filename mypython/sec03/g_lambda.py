#----------for문 lambda
#1. 목록을 주면 요소**2를 구한 후 다시 []로 리턴
def examfor():
    print('======examfor()======')
    numbers=[1,2,3,4,5]
    squared_numbers = [lambda x : x**2 for x in numbers]
    #x의 제곱값을 계산하기 위한 func(x)
    result=[func(x) for func, x in zip(squared_numbers, numbers)]
    print(type(squared_numbers), squared_numbers)
    print(result)

#zip
def examzip():  #입력 목록의 길이가 다른 경우, zip은 가장 짧은 애를 기준으로, tuple로 리턴.
    print('======examzip()======')
    name = ['a', 'e', 'i', 'p', 'y', 't', 'h']
    age = [1,2,3,4,5]
    tel = [11,22,33,44,55,66,77,88,99]
    zip_res= zip(name,age,tel)
    print(zip_res)
    for name, age, tel in zip_res:
        print(f'{name} : {age}, {tel}')

#2. 문자열 목록을 대분자로 변환
def examfor02():
    print('======examfor02()======')
    strings=['apple','banana','cherry']
    uppercase_strings = [lambda s : s.upper() for s in strings]
    results = [func(s) for func, s in zip(uppercase_strings,strings)]
    print(results)

#3. 목록에서 짝수를 필터링*****
def examfor03():
    print('======examfor03()======')
    numbers=[1,2,3,4,5]
    even_numbers=[lambda li : li for li in numbers if li%2!=0]
    results=[func(li) for func,li in zip(even_numbers,numbers)]
    print(results)  #[1,2,3] => li%2!=0 은 홀수.. 홀수는 총 3개 그래서 3개

#4.목록에서 하위 문자열 찾기*****
def examfor04():    #apple
    print('======examfor04()======')
    strings = ['apple', 'banana', 'cherry']
    substring = 'ch'
    # lambda s: s => 문자열 자체를 리턴(an을 포함하던, 하지 않던)
    filtered_strings=[lambda s: s for s in strings if substring in s]   #strings의 각 문자열 반복
    results=[func(s) for func, s in zip(filtered_strings,strings)]  
    print(results)

def examfor04_2():    #apple*********
    print('======examfor04_2()======')
    strings=['def','kji''abc']
    substring='bc'
    filtered_strings=[lambda s:s for s in strings if substring in s]
    results=[func(s) for func, s in zip(filtered_strings,strings)]
    print(results)

def examfor04_res():    #banana
    print('======examfor04_res()======')
    strings = ['apple', 'banana', 'cherry']
    substring = 'an'
    filtered_strings = [s for s in strings if substring in s]
    results = filtered_strings
    print(results)

#각 문자열에서 마지막 문자를 추출
def examfor05():
    print('======examfor05()======')
    strings=['apple','banana','cherry']
    last_s=[lambda s : s[len(s)-1] for s in strings]
    results= [func(s) for func,s in zip(last_s,strings)]
    print(results)

#각 단어의 첫 글자를 대문자로 표시******
def examfor06():
    print('======examfor06()======')
    str='process finished with exit code'
    strTitle=[lambda s : s.capitalize() for s in str.split() ]
    results = [func(s) for func, s in zip(strTitle,str.split())]
    print(results)

if __name__ == '__main__':
    examfor()
    examzip()
    examfor02()
    examfor03()
    examfor04()
    examfor04_2()
    examfor05()
    examfor06()