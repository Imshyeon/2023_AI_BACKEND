'''
    1. 내장함수를 사용해서 호출 : ord('a'); unicode로 리턴, chr(97); 글자로 리턴
    2. 값전달 후 리턴을 받자.
'''
# 숫자를 입력 받아  getMych()함수로 전달 하게 되면 영문자를 리턴하는 코드를 작성하자.  단 65~ 80까지만 받자
def getMych(su):
    return chr(su) #내장함수 chr()을 이용해서 숫자를 영문자로 변환해서 리턴

def repeat_msg(msg, repeat =3):
    for i in range(repeat):
        print(msg)

if __name__ == '__main__':
    su  = int(input("input 65~80 :"))
    res  = getMych(su)  #문자를 리턴
    print("su = %5d   res =%s"%(su,res))

    repeat_msg("python")
    repeat_msg("spring", repeat=5)