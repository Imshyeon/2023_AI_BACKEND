
def case01():
    try:
        res =10/0
    except ZeroDivisionError as ZDE:    #pvm에서 Error의 종류에 해당하는 클래스를 생성해서 리턴되는 것을 except에서 해결한다.
        print('0으로 나누려고 했자너')      #오류가 났다.
        #print(res)
        #프로그램이 중단되면 더이상 진행이 안되기 때문에 try~except를 사용. 경고 및 처리
    else:
        print('else')   #오류가 나지 않았다.
    finally:
        print('오류 유무 상관없이 반드시 수행할 명령 // 백업 파일, db close(), logout')

    print("=========case01=========")
    '''
    1. pvm(python virtual machine)에서 (runtime 시에 발생되는 중단 ~)실행 시에 발생되는 상황에 맞는 클래스를 찾아서 에러 문구로 리턴 : case01을 호출하지 않는 이상 이 문구는 나오지 않는다.
    2. sys가 가진 표준 에러.. ZeroDivisionError를 리턴
    
    Traceback (most recent call last):
      File "C:\pywork\mypython\sec09\b_Exception.py", line 8, in <module>
        case01()
      File "C:\pywork\mypython\sec09\b_Exception.py", line 3, in case01
        res =10/0
             ~~^~
    ZeroDivisionError: division by zero

    Process finished with exit code 1
    '''

def case02():
    L=[1,2,3]
    try:
        num = L[4]
    except IndexError as IE:
        print(f'list index out of range')  #IndexError : list index out of range
        print("IE(__repr__)===>",IE, "\ntype(IE)====>",type(IE))
        IE.with_traceback("abc")
        num=L[0]
    else:
        print('else')
    finally:
        print("=========case02=========")
    print(num)

'''
try_stmt  ::=  try1_stmt | try2_stmt (try 안에 try ,중첩)
try1_stmt ::=  "try" ":" suite
               ("except" [expression ["as" identifier]] ":" suite)+
               ["else" ":" suite]
               ["finally" ":" suite]
try2_stmt ::=  "try" ":" suite
               "finally" ":" suite
'''

if __name__ == '__main__':
    case01()
    print()
    case02()