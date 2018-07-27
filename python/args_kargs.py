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


#**kwargs return a dictionary
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('No fruit')
        
myfunc(fruit = 'apple', veggie = 'lettuce')
#{'fruit':'apple','veggie':'lettuce'}
#My fruit of choice is apple



#using both * and **
def myfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))
    
myfunc(10,20,30,fruit = 'orange', food='eggs',animal='dog')
#I would like 10 eggs
