class ArrayTest:
    def __init__(self,a,b) -> None:
        super().__init__()
        self.a=a
        self.b=b

    def getA(self):
        a=[]
        for i in range(30,51,10):
            row=[]
            for j in range(4):
                row.append(i)
            a.append(row)
        return a

    def getB(self):
        b=[]
        for i in range(1,10,4):
            row=[]
            for j in range(i,i+4,1):
                row.append(j)
            b.append(row)
        return b

    def getC(self):
        c=[]
        return c

    def sub(self, a, b, c):
        for i in range(len(a)):
            row = []
            for j in range(len(a[i])):
                row.append(a[i][j] - b[i][j])
            c.append(row)

        return c

    def prn(self):
        m1=ArrayTest(30,1)
        a=m1.getA()
        b=m1.getB()
        c=m1.getC()
        d=m1.sub(a,b,c)
        d = '\n'.join(map(str,d))
        # d=' '.join(map(str,d))

        # print(' '.join(d))
        # return '\n'.join(map(str,d))
        return d

'''
######################sol#######################
class ArrayTest:
    def sub(self,a,b):
        c=[]
        for i in range(len(a)):
            row =[]
            for j in range(len(a[i])):
                row.append(a[i][j] - b[i][j])
            c.append(row)
        return c
    def prn(self,c):
        for i in c:
            print(' '.join(str(e) for e in i))
'''