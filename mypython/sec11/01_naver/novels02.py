from bs4 import BeautifulSoup
import requests
import json


resp = requests.get('https://novel.naver.com/webnovel/weekday')
soup = BeautifulSoup(resp.text, 'html.parser')

lanking_list = soup.find('div', class_='component_section')

item_list = lanking_list.find_all('li', class_='item')

novel_list = list() #[]
for item in item_list:
    lank = item.p.text.strip()
    title = item.select('span.title')[0].text

    #dict type으로 데이터 타입 지정
    tmp = dict()
    tmp['lank'] = lank  #int(lank)
    tmp['title'] = title

    novel_list.append(tmp)

result = dict()
result['novels'] = novel_list
# print(result)

result_json = json.dumps(result, ensure_ascii=False)
print(result_json)

with open('novels.json', 'w', encoding='utf-8') as f:
    f.write(result_json)

