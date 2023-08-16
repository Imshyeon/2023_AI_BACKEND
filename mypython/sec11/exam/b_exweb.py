from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<table>
<tr>
  <th>Name</th>
  <th>Age</th>
  <th>City</th>
</tr>
<tr>
  <td>John</td>
  <td>25</td>
  <td>London</td>
</tr>
<tr>
  <td>Alice</td>
  <td>30</td>
  <td>Paris</td>
</tr>
</table>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
headers = [th.get_text() for th in soup.select('table th')]

#이렇게 쓰는거는 depth 2까지만..
for th in soup.select('table th'):
    rows = [[td.get_text() for td in row.select('td')]
            for row in soup.select('table tr')[1:]]

print(f'Headers: {headers}')
print(f'Headers: {rows}')

#header 출력
'''table_head=[]
rows=soup.find_all('tr')
for row in rows:
    cells = row.find_all('th')
    head = [cell.get_text() for cell in cells]
    table_head.append(head)

table_data = []
for row in rows:
    cells = row.find_all('td')
    data = [cell.get_text() for cell in cells]
    table_data.append(data)

for data in table_head:
    head_data=data
for data in table_data:
    data = data

print(f'Headers: {table_head}')
print(f'Headers: {table_data}')'''