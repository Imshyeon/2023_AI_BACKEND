def prn(): #함수선언
    print('prn')    #명령어
        
def prn02():
    print('안녕하세요~')
    
def getA():
    return 100

def getB():
    return 200

prn()
prn02()

print(getA())   
print(getB())   

#print(*args)       문자열 제어문자 \n,\t,\b    연결문자열연산자 +

print('a='+str(getA()))
print('b='+str(getB()))