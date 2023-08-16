import xml.etree.ElementTree as ET

xml_doc = """
<bookstore>
  <book category="fiction">
    <title lang="en">Harry Potter</title>
    <author>J.K. Rowling</author>
  </book>
  <book category="non-fiction">
    <title lang="en">The Power of Habit</title>
    <author>Charles Duhigg</author>
  </book>
</bookstore>
"""

######찾아오는 애
root = ET.fromstring(xml_doc)
output_root = ET.Element("bookstore")

books = root.findall('book')
for book in books:
    category = book.get('category')
    title = book.find('title').text
    author = book.find('author').text

######패턴을 만들어서 쓰는 애
    output_book = ET.SubElement(output_root, 'book', {'category': category})
    ET.SubElement(output_book, 'title', {'lang': 'en'}).text = title
    ET.SubElement(output_book, 'author').text = author

output_xml = ET.tostring(output_root, encoding='unicode', xml_declaration=True)
print(output_xml)

'''
=>
<?xml version='1.0' encoding='utf-8'?>  # 나 xml이고 utf-8로 인코딩 되어있어 라고 선언
<bookstore><book category="fiction"><title lang="en">Harry Potter</title><author>J.K. Rowling</author></book><book category="non-fiction"><title lang="en">The Power of Habit</title><author>Charles Duhigg</author></book></bookstore>
'''