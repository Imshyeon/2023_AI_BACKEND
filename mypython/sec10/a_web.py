from bs4 import BeautifulSoup
import urllib.request   #웹의 url을 파이썬이 인식할 수 있도록 해주는 모듈

def Test():
    with open("myweb.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        print(soup,type(soup))

def Test02():
    #문서 파싱해서 class 이름, name에 접근해서 데이터를 리턴받자.
    with open("myweb.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        result=soup.find_all(class_ = "name")
        print(result)

def Test03():
    #문서 파싱해서 class 이름, name에 접근해서 데이터를 리턴받자.
    with open("myweb.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        result=soup.find_all(class_ = "name")   #list 객체의 요소에서 텍스트를 리턴받고 싶다.
        for i in result:
            print(i.get_text())

def Test04():
    #문서 파싱해서 class 이름, number에 접근해서 데이터를 리턴받자. 단 숫자만 받아오자
    with open("myweb.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        result=soup.find_all(class_ = "number")
        for i in result:
            print(i.get_text())

def Test05():
    #문서 파싱해서 class 이름, number에 접근해서 데이터를 리턴받자. 단 숫자만 받아오자
    #[]리스트 객체를 만들어서 숫자를 추가하자, 정렬하자
    my_list=[]
    with open("myweb.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        result=soup.find_all(class_ = "number")
    for i in result:
        my_list.append(int(i.get_text()))

    my_list.sort()
    print(my_list)

def Test06():
    list_url ='https://www.multicampus.com/'
    url = urllib.request.Request(list_url)  #Request 클래스로 list_url을 알아볼수있게함
                                            #웹페이지를 Request 객체로 변환
    print(url,type(url))

    #url를 가져와서 리턴을 해보자
    result = urllib.request.urlopen(url).read().decode("utf-8")
    print(result,type(result))
    #html 파싱해서 문자열을 받아오자
    soup = BeautifulSoup(result, 'html.parser')
    data=soup.find_all(class_ = "des-type1 pre-line")
    print(data)
    print(data[0])
    print(data[0].get_text())

def Test07():
    #<div class="navItem section3"> 이너의 주소만 리턴해서 my=[]에 담아서 출력해보자
    list_url = 'https://www.multicampus.com/'
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    # print(result)
    soup = BeautifulSoup(result, 'html.parser')
    nav_items = soup.find_all('div',class_="navItem section3")
    my = []
    for item in nav_items:
        anchor_tags=item.find_all('a')
        # print(anchor_tags)
        for a_tag in anchor_tags:
            #a_tag의 get()을 통해서 href속성을 추출한다.
            my.append(a_tag.get("href"))
            #==강사==
            # href=a_tag.get("href")
            # if href:
            #     my.append(href)
    print(my)


if __name__ == '__main__':
    Test07()
