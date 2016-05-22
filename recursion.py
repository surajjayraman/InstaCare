# -*- coding: utf-8 -*-
"""
Created on Sun May 08 10:43:07 2016

@author: Suraj
"""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)
    
# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)