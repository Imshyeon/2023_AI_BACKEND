import sys
if __name__ == '__main__':
    try:
        res =10/0
    except ZeroDivisionError as ZDE:    #class ZeroDivisionError : __init__(self,args = "division by zero")
                                        #   def __repr__(self) : return self.args
        print(sys.exc_info())
        #(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001CA1E3A79C0>)
        print(format(type(ZDE)))    #<class 'ZeroDivisionError'>
        print(format(ZDE.args))     #('division by zero',)
        print(format(ZDE))          #division by zero
        #traceback
        #sys