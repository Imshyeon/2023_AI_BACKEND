from bs4 import BeautifulSoup
import urllib.request

def Test():
    list_url = "https://www.donga.com/"
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, 'html.parser')
    news1 = soup.find('div', class_="only_wrap")
    a_tags = news1.find_all('li')

    for a in a_tags:
        res=a.get_text()
        lines=res.split('\n')
        print(lines[3])
    # 같은결과---
    # for a in a_tag:
    #     res=a.get_text().strip()
    #     print(res)

def Test01():
    #검색 -> 인공지능 -> 제목만
    list_url="https://www.donga.com/news/search?query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5"
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(result,'html.parser')
    news= soup.find('div',class_="schcont_wrap")
    a_tags = news.find_all('a')

    for a_tag in a_tags:
        res=a_tag.get_text()
        lines=res.split("\n")
        filtered_lines = [line for line in lines if not line.startswith(('...','동아일보','더보기','PDF'))]
        result = '\n'.join(filtered_lines)
        print(result)

#review
    # result = [a_tag.get_text() for a_tag in a_tags if not a_tag.get_text().startswith(('...', '동아일보', '더보기'))]
    # for res in result:
    #     res.strip()
    #     print(res)

if __name__ == '__main__':
    Test01()