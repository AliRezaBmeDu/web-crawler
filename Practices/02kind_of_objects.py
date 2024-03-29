# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:05:56 2024

@author: User
"""
from bs4 import BeautifulSoup

# Kinds of objects
# Beautiful Soup transforms a complex HTML document
# into a complex tree of Python objects. 
# But you’ll only ever have to deal with about four kinds of objects: 
# Tag, NavigableString, BeautifulSoup, and Comment. 
# These objects represent the HTML elements that comprise the page.

# class bs4.Tag
# A Tag object corresponds to an XML or HTML tag in the original document.

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print('Tag: ', tag)
print('type of tag: ',type(tag))
print('Tag name: ', tag.name)
tag.name = "blockquote"
print('After changing the name of tag, Tag: ', tag)
# <class 'bs4.element.Tag'>

######     Attributes   ##########
# An HTML or XML tag may have any number of attributes. 
# The tag <b id="boldest"> has an attribute “id” whose value is “boldest”.
#  You can access a tag’s attributes by treating the tag like a dictionary:

tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
print('Tag id: ',tag['id'])
# 'boldest'

# You can access the dictionary of attributes directly as .attrs:

tag.attrs
# {'id': 'boldest'}
print('Tag attribute tags: ', tag.attrs.keys())
# dict_keys(['id'])

# You can add, remove, and modify a tag’s attributes. Again, this is done by treating the tag as a dictionary:

tag['id'] = 'verybold'
tag['another-attribute'] = 1
print('After adding another attribute, Tag: ', tag)
# <b another-attribute="1" id="verybold"></b>

del tag['id']
del tag['another-attribute']
print('After deleting another attribute, Tag: ', tag)
# <b>bold</b>

# tag['id']
# KeyError: 'id'

# None
