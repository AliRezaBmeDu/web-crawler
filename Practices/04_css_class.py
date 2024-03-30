# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:46:19 2024

@author: User
"""

html_doc = """
<html><head><title>The Dormouse's story</title></head>
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

# This code finds all the tags whose names start with the letter “b”; 
# in this case, the <body> tag and the <b> tag
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
    
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

print(soup.find_all(has_class_but_no_id))

# Using class as a keyword argument will give you a syntax error.
# As of Beautiful Soup 4.1.2, 
# you can search by CSS class using the keyword argument class_:

print('Find by class: ', soup.find_all("a", class_="sister"))












