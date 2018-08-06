# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:16:18 2018

@author: Shanshan
"""

#‘String here {} then also {}’.format('sth1','sth2')

print('This is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox','brown','quick'))

print('The {2} {1} {0}'.format('fox','brown','quick')) #use index

print('The {f} {b} {q}'.format(f='fox',b='brown',q='quick')) #use variable names

#Float formatting follows "{value:width.precision f}"
result = 100/777
print('The result was {r:1.3f}'.format(r = result)) # width is the whitespace

#f string literals
name = 'Shanshan'
print(f'Hello, her name is {name}')

#formatting with placeholders
print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here, and %s text here." %('some','more'))
