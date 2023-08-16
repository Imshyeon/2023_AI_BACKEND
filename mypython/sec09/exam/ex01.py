from collections import defaultdict

def case01():
    artist = ['빅뱅','임윤찬','blur','지드래곤']
    music = ['we like 2 party','라흐마니노프 교향곡 3번','the universial', 'crayon']
    res=defaultdict(list)   #기본 dict를 만들고 안의 객체를 키, value로 생성된 것을 추가해서 출력해보자
    #dict로 생성
    print(res)
    for li, m in enumerate(artist):
        res[m].append(music[li])
    print(res)
    for i in res.values():
        print(i)


def case02():
    counter = defaultdict(int)
    my_list = [1,2,3,4,5]
    print(counter)
    for li in my_list:
        counter[li] += 1
    for num,count in counter.items():
        print(f'{num} : {count}')

if __name__ == '__main__':
    # case02()
    case01()