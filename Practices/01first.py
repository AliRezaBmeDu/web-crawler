# -*- coding: utf-8 -*-

# Here’s an HTML document I’ll be using as an example throughout this document. 
# It’s part of a story from Alice in Wonderland:

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

print('\nSoup title:        ')
print(soup.title)
# <title>The Dormouse's story</title>

print('\nSoup title name:           ')
print(soup.title.name)
# u'title'

print('\nTitle name string:       ')
print(soup.title.string)
# u'The Dormouse's story'

print('\nTitle parent name')
print(soup.title.parent.name)
# u'head'

print('\nFirst p element: ')
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

print('\nP class name')
print(soup.p['class'])
# u'title'

print('\na element: ')
print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print('\nAll a elements: ')
print(soup.find_all('a'))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print('\nFindindg specific element with id: ')
print(soup.find(id="link3"))
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


print('\nFinding All the links: ')
for link in soup.find_all('a'):
    print(link.get('href'))
    
# Another common task is extracting all the text from a page:
print('Extracting all the text from a site')
print(soup.get_text())