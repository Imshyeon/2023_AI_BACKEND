import json #비정형 데이터를 처리할 때 사용
def test():
    with open('a.json','r') as file:
        data=json.load(file)
        return data

def test01():
    with open('b.json', 'r') as file:
        data=json.load(file)
        return data

def test02():   #key값으로 정렬
    with open('c.json', 'r') as file:
        data=json.load(file)
        return data

if __name__ == '__main__':
    print(test())
    print(test01())
    print(test02())
