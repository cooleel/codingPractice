# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 17:44:10 2018

Define a function first_unique that takes a string as input and 
returns the first non-repeated (unique) character in the input string. 
If there are no unique characters return None. 

@author: Shanshan
"""

def first_unique(string):
    lists = []
    counts = {}
    for i in string:
        if i in counts:
            counts[i]+=1
        else:
            counts[i] =1
            lists.append(i)
    for x in lists:
        if counts[x] ==1:
            return x
    return None


first_unique('aaadp')





#alternative
def first_unique(string):
    return (a for a in string if string.count(a)==1).next()
    
