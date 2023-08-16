from bs4 import BeautifulSoup
import requests


# naver -> 웹툰 -> 웹소설
resp = requests.get('https://novel.naver.com/webnovel/weekday')
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

lanking_list = soup.find('div', class_='component_section')
# print(lanking_list)

item_list = lanking_list.find_all('li', class_='item')
# print(item_list)

for item in item_list:
    lank = item.p.text.strip()
    # lank = item.select('p.ranking')[0].select('em.rank')[0].text
    # title = item.find_all('p')[1].find('span', class_='title').text
    # integrationRaking > ul:nth-child(1) > li:nth-child(1) :: li->item에서 selector 복사
    title = item.select('span.title')[0].text
    print(f'{lank}위 : {title}')

#번외편 : 연령별 인기작




###나중에 다시 한번 해보기