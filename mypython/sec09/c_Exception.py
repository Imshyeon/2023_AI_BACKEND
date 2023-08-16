#import traceback -> help(traceback)->
'''
print_exc(limit=None, file=None, chain=True)
        Shorthand for 'print_exception(*sys.exc_info(), limit, file)'.

    print_exception(exc, /, value=<implicit>, tb=<implicit>, limit=None, file=None, chain=True)
        Print exception up to 'limit' stack trace entries from 'tb' to 'file'.

'''

import traceback
#프로그램이 중단된 걸 아는 애는 traceback과 sys다
def f1(a,b):
    return f2(a) + f2(b)

def f2(x):
    return 1.0/x #=>ZeroDivisionError이 날 거 같은데?

if __name__ == '__main__':
    try:
        f1(1.0, 0.0)
    except (ZeroDivisionError,IOError) :
        # pass
        traceback.print_exc()   #어떤 에러가 실행된거야? => ZeroDivisionError야
