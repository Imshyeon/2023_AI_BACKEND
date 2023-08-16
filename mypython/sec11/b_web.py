from bs4 import BeautifulSoup

# 요소의 속성 값 찾는 방법
html_doc = """
<html>
<body>
<h1>Links</h1>
<a href="https://www.example.com">Example 1</a>
<a href="https://www.google.com">Example 2</a>
<a href="https://www.openai.com">Example 3</a>
</body>
</html>
"""


soup = BeautifulSoup(html_doc, 'html.parser')

#[속성] 이렇게 이용
links = [a['href'] for a in soup.find_all('a')]
print(links)

for link in links:
    print(link)
