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
  <td class = 'my' >John</td>
  <td>25</td>
  <td class = 'my' >London</td>
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

# my_texts = [td.get_text(strip=True) for td in soup.select('td.my')]
my_texts = [td.get_text(strip=True) for td in soup.select('table tr td.my')]
#같은 결과
#my_text = [td.get_text(strip=True) for td in soup.select("td[class='my']")]
print("Texts:",my_texts)

output_text = ','.join(my_texts)
print("output Text:", output_text)

