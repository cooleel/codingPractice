# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 21:28:42 2018

@author: Shanshan
"""

#arbitrary arguments
#args is arbitrary but convention

def myfunc(*args):
    print(args)
    
myfunc(1,2,3,4,5)
#(1,2,3,4,5)  a tuple