import json
def Test01():
    data=[{'a':'A', 'b':(2,4), 'c':3.0}]    #data[0]을 만듦. 리스트객체
    print('data :', data , 'repr(data) : ' ,repr(data), str(data))
    print(type(data) ,   type(repr(data)))#repr(data) 는 str 타입
    data_string = json.dumps(data)
    print('json :', data_string , type(data_string))#키는 ""로 표현되고, ()이 []로 됨, 타입결과

def Test02():
    data ={'a': 'A', 'b': (2, 4), 'c': 3.0}#리스트 객체가 아님
    data_string = json.dumps(data, indent=4,sort_keys=True)
    print('Encoded :', data_string,type(data_string))   #str 타입
    #repr(data_string))
    decoded  = json.loads(data_string)
    print("decoded :", decoded, type(decoded))#dict 타입
def Test03():
    obj_json = '{"str": [42.2], "str01": 42}'
    obj = json.loads(obj_json)
    print(obj)
    print(json.dumps(obj, indent=4, sort_keys=True))

def Test04():
    obj_json = {"str": [42.2], "str01": 42, "str02":'대한민국'}

    file  = "data.json"
    json.dump(obj_json,fp=open(file,'w'),indent=4, sort_keys=True)

    #파일에서 읽어서 화면 출력 하기
    #file = open("data.json", 'r') #r+b
    result = json.load(fp=open(file, 'r'))
    print(result)


if __name__ == '__main__':
    Test04()


