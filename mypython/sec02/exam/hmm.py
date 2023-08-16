def getTot(a,b,c):
    sum = a+b+c
    return sum
def getAvg(value):
    Avg= value / 3
    return Avg
def getGrad(value):
    grad_dict ={
        range(90,101): 'A',
        range(80,90):'B',
        range(70,80):'C'
    }
    return grad_dict.get(value // 1,'D')
name = "홍길동"
kor = 90
eng = 80
mat = 75
tot = getTot(kor,eng,mat)
avg = getAvg(tot)
grad = getGrad(avg)
# print(f'Name: {name}\nKorean: {kor}\nEnglish: {eng}\nMath: {mat}\nTotal: {tot}\nAverage: {avg:.1f}\nGrade: {grad}')
def Prn(name,kor,eng,mat,tot,avg,grad):
    print (f'Name: {name}\nKorean: {kor}\nEnglish: {eng}\nMath: {mat}\nTotal: {tot}\nAverage: {avg:.1f}\nGrade: {grad}')
Prn(name,kor,eng,mat,tot,avg,grad)