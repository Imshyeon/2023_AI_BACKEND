code = 100

#case1 :dict-> 선택문
discount_codes ={ 50:'SAVE20',
                100:'DISCOUNT50',
                200:'BIGSALE' ,
                500:'MEGADEAL'
                 }
#코드작성
result = discount_codes.get(code,0)
print(f'세일 코드{code}의 세일은 {result}이다')

#case2 : if~elif~else ->조건문

if code == 50:
    result = 'SAVE20'
elif code == 100:
    result = 'DISCOUNT50'
elif code == 200:
    result = 'BIGSALE'
elif code == 500:
    result = 'MEGASALE'
else:
    result = 0

print(f'세일 코드{code}의 세일은 {result}이다')

#case -> 함수 변형
#return -> 함수 종료시키는 키워드
def sale(code):
    if code == 50:
        result = 'SAVE20'
    elif code == 100:
        result = 'DISCOUNT50'
    elif code == 200:
        result = 'BIGSALE'
    elif code == 500:
        result = 'MEGASALE'
    else:
        result = 0
    return result

def sale02(code):
    if code == 50:
        return 'SAVE20'
    elif code == 100:
        return 'DISCOUNT50'
    elif code == 200:
        return 'BIGSALE'
    elif code == 500:
        return 'MEGASALE'
    else:
        return 0

code = 500
res=sale(code)
print(f'세일 코드{code}의 세일은 {res}이다')

code = 200
res2=sale02(code)
print(f'세일 코드{code}의 세일은 {res2}이다')