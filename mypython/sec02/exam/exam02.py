'''
이름과 세 과목의 총점, 평균, 학점을 내고 싶다.
조건 1. 시그니처 변경하지 않는다.
조건 2. 평균은 소수 이하 한자리
조건 3. 학점은 A,B,C 나머지 D
'''

#exam01을 for문 이용..

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

def getGrad(avg):
    grade_table={
        (90, float('inf')) : 'A',
        (80,90) : 'B',
        (70,80) : 'C',
        (-float('inf'),70) : 'D'
    }
    print(grade_table.items())  
    for(lower,upper), grade in grade_table.items():
        if lower <= avg < upper:
            return grade
    return 'D'

name = "홍길동"
kor = 90
eng = 80
mat = 75
tot =getTot(kor,eng,mat)
avg = getAvg(tot)
grad = getGrad(avg)
Prn(name,kor,eng,mat,tot,avg,grad)
print(name, tot, avg, grad)
