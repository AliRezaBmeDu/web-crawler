# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:25:37 2024

@author: User
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print('tag string:  ', tag.string)
# 'Extremely bold'
print('type of tag string:  ', type(tag.string))

unicode_string = str(tag.string)
print('Unicode string Tag text', unicode_string)
# 'Extremely bold'
print('type of tag string in unicode:  ', type(unicode_string))
# <type 'str'>

# The BeautifulSoup object represents the parsed document as a whole. 
# For most purposes, you can treat it as a Tag object. 
# This means it supports most of the methods 
# described in Navigating the tree and Searching the tree.

# You can also pass a BeautifulSoup object into one of the methods 
# defined in Modifying the tree, just as you would a Tag.
# This lets you do things like combine two parsed documents:

doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(string="INSERT FOOTER HERE").replace_with(footer)
# 'INSERT FOOTER HERE'
print('After replacing footer: ', doc)
# <?xml version="1.0" encoding="utf-8"?>
# <document><content/><footer>Here's the footer</footer></document>



## Comments
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print('Comment: ', comment)
print('type of comment:  ', type(comment))
print('pretty comment:  ', soup.b.prettify())
# <class 'bs4.element.Comment'>

















