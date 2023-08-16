#파일을 readline() 메소드를 읽어 보자.
print("========case 1====readline()")
f=open("data02.txt",'r')
line = f.readline() #하나의 라인만 리턴 받는다.
print(line)
f.close()

print("======case 2 ======readline()")  #유효성 검사에 쓰이는 방법
f=open("data02.txt",'r')
line = f.readline() #하나의 라인만 리턴 받는다.
while line:
    print(line)
    line = f.readline()
f.close()

print("====case 3========readline()")   #무조건 출력을 하는 것.
f=open("data02.txt",'r')
while 1:
        line = f.readline()
        if not line:
            break
        print(line)
f.close()

print("====case 4========readline()")   #통으로 읽어서 출력
f=open("data02.txt",'r')
for line in f:
        print(line)
f.close()
