#파일의 임의 접근을 해보자

f=open("test.txt","r")
str  = f.read()  # 전체 파일의 내용을 읽어서 리턴
print(str)
print("=================================")
f.seek(0) #파일 포인터의  위치를  0으로 이동
while (1):
    l =f.readline() #한줄씩 읽어서 리턴
    if(l):
        print(l ) #출력을 한다.
    else:
        break

print("=================================")
f.seek(1)
print("f.tell() : ",f.tell())
ls= f.readlines()
print(ls) #전체 출력
print(ls[3][2], ls[3][4])
print(f.tell())
print("===============================")
f.seek(20)
print(f.read())
f.close()



