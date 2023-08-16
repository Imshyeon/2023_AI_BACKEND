from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<div class="container">
  <h1>Heading</h1>
  <div class="content">
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
  </div>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

heading = soup.find('h1').get_text()
paragraphs = [p.get_text() for p in soup.select('.content p')]
# ResultSet[Tag] ; ResultSet은 테이블형태..
print("Heading:", heading)
print("Paragraphs:", paragraphs)

###위의 html 코드를 css 의사결정으로 선택해서 데이터 추출해보자
para_child = soup.select('p:nth-child(1)')
print(para_child[0].get_text())
para_child2 = soup.select('p:last-child')
print(para_child2[0].get_text())
para_extra = soup.select('p:nth-of-type(2)')
print(para_extra[0].get_text())
para = soup.select('p:first-child')
print(para[0].get_text())
para_hover = soup.select('p:hover')
print(para_hover[0].get_text())