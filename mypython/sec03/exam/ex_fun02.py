# 두수를 받아서   start ~ end 까지 출력하는 함수를 prn()으로 만들어 보자.
def prn(start, end):
    end  = end +1
    for i in range(start, end):
        print("%3d"%(i),end ="\t")

# 두수를 받아서   start ~ end 까지 출력하고 합을 구하는  함수를 prn_sum()으로 만들어 보자.
def prn02(start, end):
    end  = end +1
    sum  = 0
    for i in range(start, end):
        print("%3d"%(i),end ="\t")
        sum += i
    else:
        print("sum =", sum)

if __name__ == '__main__':
     prn02(1,10) #1~10 까지 출력
     print("\n\n")
     prn02(5,25) # 5~25 까지 출력하고 합을 구해보자.