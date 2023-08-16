#
# txt, csv, xml, json, sql -> pandas
# json 파일에 {} 형식으로 저장하는 직렬화 함수
#
# 도움말 꼭 찾아보기
# json.dump(data, ---------> {}, [].. 키,밸류로 관리하는...
#           file_object, -->파일 대상, io.StringIO
#           skipkeys=False,-->True // 데이터유형 제한
#           ensure_ascii=True, --> ascii가 아닌 문자들 ex. \uXXX(유니코드) // False이면 그냥 리턴해버림
#           check_circular=True,-> 순환참조 // type이 잘못되면 TypeError를 리턴함.
#           allow_nan=True,------> None(py) == Nan, Infinithy, InfinityJSON
#           cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)


import json #비정형 데이터를 처리할 때 사용
def test():
    data = {"name" : "Zoe",
            "age" : 20,
            "city" : "Gunpo"}
    with open('a.json','w') as file:
        json.dump(data,file)


def test01():
    data = [{"name": "Zoe1","age": 20,"city": "London1"},
            {"name": "Zoe2", "age": 21, "city": "London2"},
            {"name": "Zoe3", "age": 22, "city": "London3"}
            ]
    with open('b.json', 'w') as file:
        json.dump(data, file, indent=4)

def test02():   #key값으로 정렬
    data = {"name": "Zoe",
            "age": 20,
            "city": "Gunpo"}
    with open('c.json', 'w') as file:
        json.dump(data, file, indent=5, sort_keys=True, ensure_ascii=False)



if __name__ == '__main__':
    test02()

