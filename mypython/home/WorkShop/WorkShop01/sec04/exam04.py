i = int(input('input 1,2,3,4,5(End): '))

while True:
    if i==5:
        break
    else:
        if i==1:
            print(f'case{i}=============')
            a = []
            for j in range(1, 26, 5):
                row = []
                for k in range(j, j + 5):
                    row.append(k)
                a.append(row)
            result = '\n'.join(map(str, a))
            print(result)
            break
        elif i==2:
            print(f'case{i}=============')
            a = []
            for j in range(1,6):
                row = []
                for k in range(j, j+21, 5):
                    row.append(k)
                a.append(row)
            result = '\n'.join(map(str, a))
            print(result)
            break
        elif i==3:
            print(f'case{i}=============')
            a = []
            for j in range(25,1,-5):
                row = []
                for k in range(j, j-5, -1):
                    row.append(k)
                a.append(row)
            result = '\n'.join(map(str, a))
            print(result)
            break
        elif i==4:
            print(f'case{i}=============')
            a = []
            for j in range(25,20,-1):
                row = []
                for k in range(j, j-24, -5):
                    row.append(k)
                a.append(row)
            result = '\n'.join(map(str, a))
            print(result)
            break
        else:
            break