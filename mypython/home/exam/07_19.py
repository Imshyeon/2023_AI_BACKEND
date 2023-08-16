# sum() 내장 함수를 사용해 보자.
import string
def Test01():
    #1. list 객체의 요소의 합을 출력하자.
    listdata =[2,2,1,3,8,4,3,9,2,20]
    result  = sum(listdata)
    print(listdata)
    print(result)

def Test02():
    #2. 짝수번째 요소의 합을 출력 해보자.
    listdata = [2, 2, 1, 3, 8, 4, 3, 9, 2, 20]
    result  = listdata[1::2]
    print(sum(result))

def Test03():
    a = [2,1,5,6,7,9,10,3]
    result = sum(range(1,11)) -sum(a)
    print(result)

def Test04(): #list 요소가 진리값 (all, any)  all( ) = And,And,,,     any() = or,or,,,
    '''
       True  = 1   , False  =0
      all():  인자로 입력되는 리스트의 모든 요소가 참일 경우만 True , 거짓이 하나라도 있으면  False를 리턴
      any() : 인자로 입력되는 리스트의 모든 요소가 거짓인 경우만  False, 참이 하나라도 있으면  True를 리턴
    '''
    listdata1 =[True, True, True]
    listdata2= [True, False,True]
    print(all(listdata1))  #True
    print(all(listdata2))  # False
    print(any(listdata1))  # True
    print(any(listdata2))  # True

def Test05():
    listdata1 = [1, 1, 1]
    listdata2 = [1, 0, 1]
    print(all(listdata1))  # True
    print(all(listdata2))  # False
    print(any(listdata1))  # True
    print(any(listdata2))  # True

def Test06():
    # 문자 코드 구하기  ( ord): 문자를 컴퓨터가 인식하는 코드값으로 변환  A(사람) ----인코딩------> 65(컴퓨터)
    print(ord('A'))
    #알파벳 대문자를 출력 해보자.
    print(string.ascii_uppercase , type(string.ascii_uppercase))
    print(string.digits)
    print("영문자 대문자를 코드값으로 바꾸어 보자.  ")
    for i in string.ascii_uppercase:
        print(i, '-------------------->', ord(i))
def Test07():
    print("영문자 소문자를 코드값으로 바꾸어 보자. string 모듈과 ord()함수를 사용하자.   ")
    for i in string.ascii_lowercase:
        print(i, '-------------------->', ord(i))
def Test08():#chr()인자로 정수를 입력하게 되면 정수값에 해당하는 문자를 리턴한다.
   print( chr(65))
   '''
     65 ---------------->A  
    ...
     90----------------->Z
   '''
   for  i  in range(65,91):
       print(i,'---------------------->',chr(i))

if __name__ == '__main__':
    Test08() 