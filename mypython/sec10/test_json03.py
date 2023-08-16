import json

def prn01():
    #data.json 파일을 read해보자
    with open('data.json') as f:
        s=f.read()
        print(s, type(s))

    result = json.load(fp=open('data.json', 'r'))
    print('\nresult :',result)

def prn02():
    '''
        1. json 모듈을 사용해서 STUDENT.json을 읽어오자
        2. Object_hook Student 클래스를 만들어서 데이터를 대입한다
        3. 파일을 오픈된 파일 read()를 이용해서 출력을 먼저 해본다
        4. 이름 : 총점 으로 출력한다.
            ex.RuRe : 270 점
    '''
    with open('STUDENT.json') as f:
        result=f.read()
    print(result)

    data = json.loads(result, object_hook=Object_hook_Student)
    for my in data.STUDENT:
        hap = my.SCORE.KOR + my.SCORE.ENG + my.SCORE.MATH
        print(my.NAME + " : %3d 점"%hap)

class Object_hook_Student:
    def __init__(self,res):
        self.__dict__=res
        print(self.__dict__)

if __name__ == '__main__':
    prn02()
