from bs4 import BeautifulSoup

'''
nth-of-type() 부모 요소 내의 위치에 따라 요소를 선택할 수 있는 CSS 의사 클래스
name = row.select_one('td.my').get_text(strip=True)
age = row.select_one('td:nth-of-type(2)').get_text(strip=True)  # td가 가진 2번째 애
city = row.select_one('td:nth-of-type(3)').get_text(strip=True) # td가 가진 3번째 애
=> table, 중첩된 div나 목록에서 주로 사용
'''

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
data=[]
rows=soup.select('table tr')
for row in rows[1:]:
    name = row.select_one('td:nth-of-type(1)').get_text(strip=True)
    age = row.select_one('td:nth-of-type(2)').get_text(strip=True)
    city = row.select_one('td:nth-of-type(3)').get_text(strip=True)
    data.append({'Name':name, 'Age':age, 'City': city})

print(data) #[{'Name': 'John', 'Age': '25', 'City': 'London'}, {'Name': 'Alice', 'Age': '30', 'City': 'Paris'}]

for item in data:
    print(item)     #1. {'Name': 'John', 'Age': '25', 'City': 'London'}
                    #2. {'Name': 'Alice', 'Age': '30', 'City': 'Paris'}
    print(f"Name: {item['Name']}, Age:{item['Age']}, City:{item['City']},")