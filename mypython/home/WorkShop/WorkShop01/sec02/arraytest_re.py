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