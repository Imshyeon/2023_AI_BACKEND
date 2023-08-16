'''
이름과 세 과목의 총점, 평균, 학점을 내고 싶다.
조건 1. 시그니처 변경하지 않는다.
조건 2. 평균은 소수 이하 한자리
조건 3. 학점은 A,B,C 나머지 D
'''

class Prn :
    def __init__(self,name, kor, eng, mat, tot, avg, grad):   #생성자
        print("Name :", name)
        print("Korean :", kor)
        print("English :", eng)
        print("Math :", mat)
        print("Total :", tot)
        print("Average :", avg)
        print("Grade :", grad)
        
def getTot(kor, eng, mat):
    return kor+eng+mat

def getAvg(tot):
    return round(tot/3,1)

''' 
def getGrad(avg):
    if avg>=90:
        return 'A'
    elif avg>=80:
        return 'B'
    elif avg>=70:
        return 'C'
    else:
        return 'D'
    
'''


def getGrad(value):
    value=value//10
    print(value)
    grad_dict={
        range(8,10) : 'A',
        range(6,8) : 'B',
        range(4,6) : 'C'
    }
    print(grad_dict.get(range(8,10)))
    print(grad_dict.get(value))
    return grad_dict.get((value//10)*10,'D')  #avg//10 : 정수로 리턴..



name = "홍길동"
kor = 90
eng = 80
mat = 75
tot =getTot(kor,eng,mat)
avg = getAvg(tot)
grad = getGrad(avg)

Prn(name,kor,eng,mat,tot,avg,grad)
