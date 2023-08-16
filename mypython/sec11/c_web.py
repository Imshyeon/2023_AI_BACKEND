from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<table>
<tr>
  <th>Name</th>
  <th>Age</th>
</tr>
<tr>
  <td>John</td>
  <td>25</td>
</tr>
<tr>
  <td>Alice</td>
  <td>30</td>
</tr>
</table>
</body>
</html>
"""


soup = BeautifulSoup(html_doc, 'html.parser')   #전체 문서 객체로 리턴

table_data = []
#현재 웹 페이지에서 table이 여러개 -> table의 id나 table을 둘러싸는 div(하지만 div는 잘 없다..)나 css로 객체를 하위로 탐색
#단일이면 table 자체를 가져옴
rows = soup.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    data = [cell.get_text() for cell in cells]
    table_data.append(data)


for data in table_data:
    print(data)
