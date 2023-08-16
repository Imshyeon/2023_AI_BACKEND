from ArrayTest import ArrayTest

if __name__ == '__main__':
    m1=ArrayTest(30,1)
    a=m1.getA()
    b=m1.getB()
    c=m1.getC()
    d=m1.prn()
    print(d)
'''
###################sol###################
from arraytest_re import ArrayTest

if __name__ == '__main__':
    a = [[30, 30, 30, 30],
         [40, 40, 40, 40],
         [50, 50, 50, 50]]
    b = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]
    m1 = ArrayTest()
    c = m1.sub(a, b) 
    m1.prn(c)
'''

