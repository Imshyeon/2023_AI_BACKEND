from arraytest import ArrayTest
if __name__ == '__main__':
    a = [[30, 30, 30, 30],
         [40, 40, 40, 40],
         [50, 50, 50, 50]]

    b = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]

    t1 = ArrayTest()
    c = t1.sub(a, b)
    t1.prn(c)
