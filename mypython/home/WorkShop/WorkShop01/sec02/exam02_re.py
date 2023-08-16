from arraytest_re import ArrayTest

if __name__ == '__main__':
    a=[[30, 30, 30, 30],
       [40, 40, 40, 40],
       [50, 50, 50, 50]]
    b=[[1,  2,  3,  4],
       [5,  6,  7,  8],
       [9, 10, 11, 12]]
    m1=ArrayTest()
    c= m1.sub(a,b)
    m1.prn(c)