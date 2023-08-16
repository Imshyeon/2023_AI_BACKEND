from bs4 import BeautifulSoup
import urllib.request
from collections import Counter

def Test01():
    list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    # print(result)
    soup = BeautifulSoup(result, 'html.parser')
    ##board_list > div.postList > ul > li:nth-child(1) > p.con
    res = soup.find_all('p',class_= 'con')
    print(res[0].get_text())

def Test02():
    list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")

    soup = BeautifulSoup(result, 'html.parser')
    ##board_list > div.postList > ul > li:nth-child(1) > p.con
    res = soup.find_all('p',class_= 'con')
    dat = []
    for r in res:
        dat.append(r.get_text(" ",strip=True))
    print(dat)
    # print(res[0].get_text())

def Test03():   #ㅅㅂ
    list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")

    # container > div > div.wrap_secMenu > div > div.gnb.on > ul
    # container > div > div.wrap_secMenu > div > div.gnb.on > ul > li.lnb_8
    soup = BeautifulSoup(result, 'html.parser')
    res = soup.find_all('ul', class_= "main lst_gnb")
    my_list=[]
    for item in res:
        anchor_tags = item.find_all('a')
        for a_tag in anchor_tags:
            href=a_tag.get_text()
            print(href)
            my_list.append(href)

    print(my_list)


def Test04():
    list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, 'html.parser')
    #css를 선택해서 <ul>요소를 선택하고 그 안에 있는 모든 a태그를 찾아라

    ul_e = soup.select_one("#container > div > div.wrap_secMenu > div > div.gnb.on > ul")
    if ul_e:
        a_tags = ul_e.find_all('a')
        for a_tag in a_tags:
            print(a_tag.get_text())

def Test05():
    list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")

    soup = BeautifulSoup(result, 'html.parser')
    # board_list > div.postList > ul > li:nth-child(1) > p.info > span.date
    # board_list > div.postList > ul > li:nth-child(1)
    date = soup.find_all('span', class_="date")
    res = soup.find_all('p', class_='con')

    list1=[]
    list2=[]

    for d in date:
        list1.append(d.get_text(strip=True))
    for r in res:
        list2.append(r.get_text(strip=True))

    for k, h in zip(list1,list2):
        print(k + ' : ' + h)

def Test06():
    list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")

    soup = BeautifulSoup(result, 'html.parser')
    # board_list > div.postList > ul > li:nth-child(1) > p.info > span.userid > img
    res = soup.find_all('ul', class_="list noThumb spot_")
    name = soup.find_all('span', class_="userid")
    listN=[]
    for n in name:
        listN.append(n.get_text(strip=True))
    print(listN)

def Test08():
    #게시판 저장 res.txt로 q
    #전체 단어가 몇 개 인지
    #res가 가진 txt 파일에 가장 많이 사용한 단어를 추출한다.
    #read()->split()->sort() => Counter
    #most_common()

    list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, 'html.parser')
    res = soup.find_all('p', class_='con')
    dat = []
    for r in res:
        dat.append(r.get_text(" ", strip=True))
    print(dat)

    with open('res.txt','w',encoding='utf-8') as f:
        for text in dat:
            f.write(text+'\n')
    res= open('res.txt',encoding='utf-8')
    data= res.read().split()
    data.sort()
    #텍스트 단어의 발생횟구 계산 -> Tuple로 리턴(요소, 개수), 내림차순(default)
    countText= Counter(data)#data 리스트 안에 어절별로 각각 몇건씩 있는지 계산
    c=countText.most_common(10)

    for i in c:
        print(i[0],i[1])


def Test09():
    with open('res.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()

        word_counts = Counter(words)
        for word, count in word_counts.items():
            print(word, count, '문자의 길이 =', len(word))

def Test10():
    with open("res.txt", encoding="utf-8") as file:
        text_content = file.read().split()
        countlist = Counter(text_content)

    result = countlist.most_common()
    for word, count in result:
        print(f"{word}: {count}, 글자수 : {len(word)}")

if __name__ == '__main__':
    Test08()

#모듈 임포트 -> 수집 -> list.append -> 통계분석 -> 출력
#웹클로링 기술 + 축적된 데이터 -> 통계로 데이터 분석 -> 머신러닝(수동) 데이터분석 -> 딥러닝(자동) : 분류(CNN, RNN), 특징 추출(object detection ~ yolo), 세그먼테이션(배경과 대상 분리)