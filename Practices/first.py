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

print('Soup title:        ')
print(soup.title)
# <title>The Dormouse's story</title>

print('Soup title name:           ')
print(soup.title.name)
# u'title'

print('Title name string:       ')
print(soup.title.string)
# u'The Dormouse's story'

print('Title parent name')
print(soup.title.parent.name)
# u'head'

print('First p element: ')
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

print('')
soup.p['class']
# u'title'

# soup.a
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# soup.find_all('a')
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>